### Memory Model:
| JVM Memory Allocation    | Description                                                                                  |
|--------------------------|----------------------------------------------------------------------------------------------|
| **Java Heap**            | Stores all the objects created by the application.                                           |
| ↳ **Young Generation**   | Where new objects are allocated and aged before possibly moving to the old generation.       |
|   ↳ **Eden Space**       | The pool from where memory is initially allocated for most objects.                          |
|   ↳ **Survivor Space 1** | Objects are moved here from Eden after surviving one garbage collection cycle.               |
|   ↳ **Survivor Space 2** | Objects are moved here from Survivor Space 1 after surviving another cycle.                  |
| ↳ **Old Generation**     | Stores longer-lived objects that have survived several garbage collection cycles.            |
| **Method Area (Metaspace)** | Stores per-class structures containing runtime metadata classes in the JVM.              |
|   ↳ **Static Data**      | Stores static member of classes.                                                             |
|   ↳ **Constant Pool**    | Stores constant values referenced within the classes.                                        |
|   ↳ **Class Information**| Stores class and interface information.                                                      |
| **Java Stacks (Per Thread)**| Each JVM thread has its own stack that stores frames needed to execute Java bytecode.   |
| ↳ **Frame**              | Each frame stores data and partial results, as well as perform dynamic linking and returning. |
| **Native Method Stack**  | Specific for native methods used in the application (non-Java calls).                         |
