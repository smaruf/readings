### GC Operation and Options:
| Garbage Collection Operation | Description                                                                                            | JVM Option                          |
|------------------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------|
| **Marking**                  | Identifies used objects that are still reachable from the application.                                | N/A                                 |
| **Normal Deletion**          | Removes objects that are marked as unreachable, freeing up the heap space occupied by them.            | N/A                                 |
| **Deletion with Compaction** | Performs both deletion of unreachable objects and compaction to organize memory and prevent fragmentation. | N/A                             |
| **Types of GC Algorithms**   | Various algorithms used for garbage collection, optimized for different scenarios.                     |                                     |
| ↳ **Serial GC**              | Uses a single thread for GC operations, suitable for small applications with limited resources.        | `-XX:+UseSerialGC`                  |
| ↳ **Parallel GC (Throughput Collector)** | Uses multiple threads for handling the young and old generations, aiming for high throughput.    | `-XX:+UseParallelGC`                |
| ↳ **Concurrent Mark Sweep (CMS) GC** | Minimizes the pauses by performing most of the garbage collection work concurrently with application threads. | `-XX:+UseConcMarkSweepGC`      |
| ↳ **Garbage-First (G1) GC**  | Organizes heap into a set of regions to manage them efficiently, aiming for predictable GC pauses.      | `-XX:+UseG1GC`                      |
| ↳ **Parallel Compacting GC** | An extension of Parallel GC that improves the compacting phase by using multiple threads, suitable for multi-processor machines. | `-XX:+UseParallelOldGC`        |
| ↳ **ZGC (Z Garbage Collector)** | A scalable low-latency garbage collector that aims for a max pause time of about 10ms.                | `-XX:+UseZGC`                       |
| ↳ **Shenandoah GC**          | Focuses on reducing GC pause times by performing more work concurrently with the application threads.   | `-XX:+UseShenandoahGC`              |
| ↳ **Epsilon GC**            | A no-op garbage collector useful for performance testing. It handles memory allocation but does not do garbage collection. | `-XX:+UseEpsilonGC`            |
