import java.nio.file.Files
import java.nio.file.Paths

// Define the Java program file and class name
def JAVA_FILE = 'GCDemo.java'
def CLASS_NAME = 'GCDemo'

// Define the list of GC options to test
def GC_OPTIONS = [
    '-XX:+UseSerialGC',
    '-XX:+UseParallelGC',
    '-XX:+UseConcMarkSweepGC',
    '-XX:+UseG1GC',
    '-XX:+UseZGC',
    '-XX:+UseShenandoahGC',
    '-XX:+UseEpsilonGC'
]

// Function to compile the Java program
def compileJavaProgram() {
    println 'Compiling Java program...'
    def proc = ['javac', JAVA_FILE].execute()
    proc.waitFor()
    if (proc.exitValue() != 0) {
        println 'Compilation failed:'
        println proc.err.text
        return false
    }
    return true
}

// Function to run the Java program with the specified GC option
def runGcDemo(gcOption) {
    def logFile = "gc_demo_${gcOption.replaceAll('[+:]', '').replaceAll('XX', '').replaceAll('Use', '').replaceAll('GC', '').toLowerCase()}.log"
    println "Running GC demo with option $gcOption..."
    def proc = ['java', gcOption, CLASS_NAME].execute()
    proc.waitForProcessOutput(new File(logFile).newOutputStream(), System.err)
    return logFile
}

// Function to extract GC pause times from the log file
def extractGcTimes(logFile) {
    def totalGcTime = 0.0
    new File(logFile).eachLine { line ->
        if (line.contains('Pause')) {
            def timeMs = line.split().last().replace('ms', '').toDouble()
            totalGcTime += timeMs
        }
    }
    return totalGcTime
}

// Function to create plot using gnuplot
def createPlot(gcResults) {
    def plotData = 'gc_results.dat'
    def plotScript = 'plot_script.gp'
    
    new File(plotData).withWriter { writer ->
        gcResults.each { gcOption, time ->
            writer.println("${gcOption.replace('-XX:+', '')} $time")
        }
    }

    new File(plotScript).text = """
        set terminal png size 800,600
        set output 'gc_performance_comparison.png'
        set title 'Garbage Collection Performance Comparison'
        set xlabel 'GC Options'
        set ylabel 'Total GC Pause Time (ms)'
        set xtics rotate by -45
        plot '$plotData' using 2:xtic(1) with histograms title 'GC Pause Time' lc rgb 'skyblue'
    """

    def proc = ['gnuplot', plotScript].execute()
    proc.waitFor()
}

if (compileJavaProgram()) {
    def gcResults = [:]
    GC_OPTIONS.each { gcOption ->
        def logFile = runGcDemo(gcOption)
        def totalGcTime = extractGcTimes(logFile)
        gcResults[gcOption] = totalGcTime
    }

    createPlot(gcResults)
    println 'GC performance comparison plot generated: gc_performance_comparison.png'
} else {
    println 'Java program compilation failed. Exiting.'
}
