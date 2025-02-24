import java.io.File
import kotlin.system.exitProcess

// Define the Java program file and class name
const val JAVA_FILE = "GCDemo.java"
const val CLASS_NAME = "GCDemo"

// Define the list of GC options to test
val GC_OPTIONS = listOf(
    "-XX:+UseSerialGC",
    "-XX:+UseParallelGC",
    "-XX:+UseConcMarkSweepGC",
    "-XX:+UseG1GC",
    "-XX:+UseZGC",
    "-XX:+UseShenandoahGC",
    "-XX:+UseEpsilonGC"
)

// Function to compile the Java program
fun compileJavaProgram(): Boolean {
    println("Compiling Java program...")
    val process = ProcessBuilder("javac", JAVA_FILE).start()
    val exitCode = process.waitFor()
    if (exitCode != 0) {
        println("Compilation failed:")
        println(process.errorStream.bufferedReader().readText())
        return false
    }
    return true
}

// Function to run the Java program with the specified GC option
fun runGcDemo(gcOption: String): String {
    val logFile = "gc_demo_${gcOption.replace("+", "").replace(":", "").replace("XX", "").replace("Use", "").replace("GC", "").toLowerCase()}.log"
    println("Running GC demo with option $gcOption...")
    val process = ProcessBuilder("java", gcOption, CLASS_NAME).redirectOutput(File(logFile)).redirectError(File(logFile)).start()
    process.waitFor()
    return logFile
}

// Function to extract GC pause times from the log file
fun extractGcTimes(logFile: String): Double {
    val log = File(logFile)
    return log.readLines().filter { it.contains("Pause") }
        .sumOf { it.split(" ").last().removeSuffix("ms").toDouble() }
}

// Function to create plot using gnuplot
fun createPlot(gcResults: Map<String, Double>) {
    val plotData = "gc_results.dat"
    File(plotData).printWriter().use { out ->
        gcResults.forEach { (gcOption, time) ->
            out.println("${gcOption.replace("-XX:+", "")} $time")
        }
    }
    val plotScript = """
        set terminal png size 800,600
        set output 'gc_performance_comparison.png'
        set title 'Garbage Collection Performance Comparison'
        set xlabel 'GC Options'
        set ylabel 'Total GC Pause Time (ms)'
        set xtics rotate by -45
        plot '$plotData' using 2:xtic(1) with histograms title 'GC Pause Time' lc rgb 'skyblue'
    """.trimIndent()
    File("plot_script.gp").writeText(plotScript)
    ProcessBuilder("gnuplot", "plot_script.gp").start().waitFor()
}

fun main() {
    if (!compileJavaProgram()) {
        println("Java program compilation failed. Exiting.")
        exitProcess(1)
    }
    
    val gcResults = GC_OPTIONS.associateWith { gcOption ->
        val logFile = runGcDemo(gcOption)
        extractGcTimes(logFile)
    }

    createPlot(gcResults)
    println("GC performance comparison plot generated: gc_performance_comparison.png")
}
