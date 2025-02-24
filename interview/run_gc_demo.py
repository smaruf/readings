import subprocess
import os
import matplotlib.pyplot as plt

# Define the Java program file and class name
JAVA_FILE = "GCDemo.java"
CLASS_NAME = "GCDemo"

# Define the list of GC options to test
GC_OPTIONS = [
    "-XX:+UseSerialGC",
    "-XX:+UseParallelGC",
    "-XX:+UseConcMarkSweepGC",
    "-XX:+UseG1GC",
    "-XX:+UseZGC",
    "-XX:+UseShenandoahGC",
    "-XX:+UseEpsilonGC"
]

# Function to compile the Java program
def compile_java_program():
    print("Compiling Java program...")
    result = subprocess.run(["javac", JAVA_FILE], capture_output=True, text=True)
    if result.returncode != 0:
        print("Compilation failed:")
        print(result.stderr)
        return False
    return True

# Function to run the Java program with the specified GC option
def run_gc_demo(gc_option):
    log_file = f"gc_demo_{gc_option.replace('+', '').replace(':', '').replace('XX', '').replace('Use', '').replace('GC', '').lower()}.log"
    print(f"Running GC demo with option {gc_option}...")
    with open(log_file, "w") as logfile:
        result = subprocess.run(["java", gc_option, CLASS_NAME], capture_output=True, text=True)
        logfile.write(result.stdout)
        logfile.write(result.stderr)
    return log_file

# Function to extract GC pause times from the log file
def extract_gc_times(log_file):
    gc_times = []
    with open(log_file, "r") as logfile:
        for line in logfile:
            if "Pause" in line:
                parts = line.split()
                time_ms = float(parts[-2])
                gc_times.append(time_ms)
    return sum(gc_times)

# Compile the Java program
if compile_java_program():
    gc_results = {}
    # Run the Java program with each GC option
    for gc_option in GC_OPTIONS:
        log_file = run_gc_demo(gc_option)
        total_gc_time = extract_gc_times(log_file)
        gc_results[gc_option] = total_gc_time

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.bar(gc_results.keys(), gc_results.values(), color='skyblue')
    plt.xlabel('GC Options')
    plt.ylabel('Total GC Pause Time (ms)')
    plt.title('Garbage Collection Performance Comparison')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('gc_performance_comparison.png')
    plt.show()

else:
    print("Java program compilation failed. Exiting.")
