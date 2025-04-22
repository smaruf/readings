# Object-Oriented Programming

### 1. Explain the code of Object-Oriented Programming in Java.
Object-Oriented Programming (OOP) is a paradigm that organizes software design around data, or objects, rather than functions and logic. Core principles include encapsulation, inheritance, polymorphism, and abstraction.

Example:
```
class Animal {
    String name;

    Animal(String name) {
        this.name = name;
    }

    void makeSound() {
        System.out.println("Some sound...");
    }
}

class Dog extends Animal {
    Dog(String name) {
        super(name);
    }

    @Override
    void makeSound() {
        System.out.println(name + " says: Woof!");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Dog("Buddy");
        animal.makeSound(); // Output: Buddy says: Woof!
    }
}
```
---

### 2. Discuss the differences between an abstract class and an interface in Java.
| Feature                  | Abstract Class                         | Interface                          |
|--------------------------|-----------------------------------------|------------------------------------|
| Definition               | A class that can have abstract methods and concrete methods. | A reference type with only abstract methods (prior to Java 8). |
| Inheritance              | Can extend only one abstract class.    | Can implement multiple interfaces.|
| Methods                  | Can have concrete methods.             | From Java 8, can have default and static methods.|
| Fields                   | Can have instance variables.           | Fields are implicitly public, static, and final.|

---

### 3. How can polymorphism be implemented and utilized in Java?
Polymorphism allows methods to perform different tasks based on the object that it is acting upon. It is implemented using method overloading (compile-time polymorphism) and method overriding (runtime polymorphism).

Example:
```
class Shape {
    void draw() {
        System.out.println("Drawing a shape.");
    }
}

class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a circle.");
    }
}

public class Main {
    public static void main(String[] args) {
        Shape shape = new Circle();
        shape.draw();  // Output: Drawing a circle.
    }
}
```
---

### 4. Explain Java's method overloading and method overriding, and how they differ.
| Feature            | Method Overloading                          | Method Overriding                  |
|--------------------|---------------------------------------------|------------------------------------|
| Definition         | Same method name, different parameter list. | Same method name and parameters, but different implementation. |
| Compile-Time       | Resolved at compile-time.                   | Resolved at runtime.              |
| Inheritance        | Not required.                               | Requires inheritance.             |

Example of Overloading:
```
class MathOperations {
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }
}
```
Example of Overriding:
```
class Parent {
    void show() {
        System.out.println("Parent class method.");
    }
}

class Child extends Parent {
    @Override
    void show() {
        System.out.println("Child class method.");
    }
}
```
---

### 5. Discuss the concept of immutability in Java and how to create immutable objects.
An immutable object is an object whose state cannot be modified after it is created. To create such objects:
1. Declare the class as final.
2. Mark all fields as private and final.
3. Provide no setter methods.
4. Use deep copies for mutable fields.

Example:
```
final class Immutable {
    private final String name;

    Immutable(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
```
---

### 6. Explain the principles and implementation of the Singleton design pattern in Java.
Singleton ensures that only one instance of a class is created and provides a global access point to it.

Example:
```
class Singleton {
    private static Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```
---

### 7. How does Java support the Model-View-Controller (MVC) design pattern?
Java supports MVC by separating the application into three interconnected components:
- Model: Represents data and business logic.
- View: Displays data to the user.
- Controller: Handles user input and updates the model.

Example:
```
class Model {
    private String data;

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
}

class View {
    void print(String data) {
        System.out.println("Data: " + data);
    }
}

class Controller {
    private Model model;
    private View view;

    Controller(Model model, View view) {
        this.model = model;
        this.view = view;
    }

    void updateData(String data) {
        model.setData(data);
        view.print(model.getData());
    }
}
```
---

### 8. Explain the role of JavaBeans in Java development and how they differ from regular classes.
JavaBeans are reusable software components for Java, which adhere to specific conventions:
- A public no-argument constructor.
- Getter and setter methods for accessing properties.
- Serializable interface implementation.

Example:
```
public class PersonBean implements java.io.Serializable {
    private String name;

    public PersonBean() {}

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```
# Java Collections Framework

### 1. What are the main differences between List, Set, and Map in the Java Collections Framework?
- **List**: An ordered collection that allows duplicate elements.
- **Set**: An unordered collection that does not allow duplicate elements.
- **Map**: A collection of key-value pairs where keys are unique.

---

### 2. How does the implementation of HashMap work in Java?
HashMap uses a hash table to store key-value pairs. Keys are hashed to determine the bucket index, and collisions are handled using linked lists or trees (since Java 8).

Example:
```
HashMap<String, Integer> map = new HashMap<>();
map.put("Key1", 1);
map.put("Key2", 2);
System.out.println(map.get("Key1")); // Output: 1
```
---

### 3. Explain the difference between ArrayList and LinkedList.
- **ArrayList**: Backed by a dynamic array, provides fast random access but slow insertion and deletion.
- **LinkedList**: Backed by a doubly linked list, provides efficient insertion and deletion but slower random access.

Example:
```
ArrayList<Integer> arrayList = new ArrayList<>();
LinkedList<Integer> linkedList = new LinkedList<>();

arrayList.add(10);
linkedList.add(20);
```
---

### 4. What is the difference between HashSet and TreeSet?
- **HashSet**: Uses a hash table for storage, does not maintain order.
- **TreeSet**: Implements a red-black tree, maintains elements in sorted order.

Example:
```
HashSet<Integer> hashSet = new HashSet<>();
TreeSet<Integer> treeSet = new TreeSet<>();

hashSet.add(3);
treeSet.add(3);
```
---

### 5. How can you make a collection thread-safe in Java?
You can use `Collections.synchronizedCollection()` or concurrent collections like `ConcurrentHashMap`.

Example:
`List<Integer> synchronizedList = Collections.synchronizedList(new ArrayList<>());`

---

### 6. What are the advantages of using ConcurrentHashMap over a synchronized HashMap?
- Improved performance in a multi-threaded environment.
- Locks are applied only at the bucket level, not the entire map.

---

### 7. Explain the concept of fail-fast and fail-safe iterators in Java collections.
- **Fail-Fast**: Throws `ConcurrentModificationException` if the collection is modified during iteration (e.g., `ArrayList` iterators).
- **Fail-Safe**: Works on a copy of the collection, allowing modifications (e.g., `ConcurrentHashMap` iterators).

---

### 8. How do you sort a collection in Java?
You can use `Collections.sort()` for lists or provide a custom comparator.

Example:
```
List<Integer> list = new ArrayList<>();
list.add(3);
list.add(1);
list.add(2);
Collections.sort(list); // Output: [1, 2, 3]
```
---

### 9. What is the difference between Iterator and ListIterator?
- **Iterator**: Can traverse a collection in one direction and remove elements.
- **ListIterator**: Can traverse in both directions and add elements.

---

### 10. How do you remove duplicates from a collection in Java?
You can use a `Set` to store unique elements or use `stream().distinct()` for streams.

Example:
```
List<Integer> list = Arrays.asList(1, 2, 2, 3);
Set<Integer> uniqueSet = new HashSet<>(list); // Output: [1, 2, 3]
```
# Java Threads and Concurrency

### 1. What are Java threads and how do you create and manage them?
Java threads enable concurrent execution of two or more tasks within a program. Threads can be created by:  
1. Extending the `Thread` class.  
2. Implementing the `Runnable` interface.  

Example using `Runnable`:  
```
class MyRunnable implements Runnable {  
    public void run() {  
        System.out.println("Thread is running.");  
    }  
}  

public class Main {  
    public static void main(String[] args) {  
        Thread thread = new Thread(new MyRunnable());  
        thread.start();  
    }  
}  
```
---

### 2. How does the synchronized keyword work and when should it be used?
The `synchronized` keyword ensures that only one thread can access a block of code or method at a time. It is used to prevent race conditions.

Example:  
```
class Counter {  
    private int count = 0;  

    public synchronized void increment() {  
        count++;  
    }  

    public int getCount() {  
        return count;  
    }  
}  
```
---

### 3. Explain the concept of a thread pool and its advantages.
A thread pool is a collection of pre-instantiated reusable threads. It improves performance by reusing existing threads instead of creating new ones for each task.

Example:  
```
ExecutorService executor = Executors.newFixedThreadPool(5);  
executor.execute(() -> System.out.println("Task executed"));  
executor.shutdown();  
```
---

### 4. What is the difference between the wait() and sleep() methods in Java?
- **wait()**: Releases the lock on the object and pauses the thread until `notify()` or `notifyAll()` is called.  
- **sleep()**: Pauses the thread for a specific duration but does not release the lock.  

---

### 5. How can you avoid deadlock in a multi-threaded Java application?
Deadlocks can be avoided by:  
1. Acquiring locks in a consistent order.  
2. Using tryLock() with a timeout.  
3. Minimizing the use of multiple locks.  

---

### 6. What is the purpose of the java.util.concurrent package?
The `java.util.concurrent` package provides classes for managing concurrency, such as `Executor`, `ConcurrentHashMap`, `BlockingQueue`, and more.  

---

### 7. Explain the difference between the Executor framework and creating new threads manually.
- **Executor Framework**: Manages thread lifecycle, provides thread pooling, and reduces overhead.  
- **Manual Threads**: Requires manual management of thread creation and lifecycle.  

---

### 8. What are the benefits of using java.util.concurrent.locks.ReentrantLock over synchronized blocks?
- Allows more control, such as tryLock() for non-blocking attempts.  
- Supports conditions for signaling threads.  
- Can be used with fair locking to ensure thread fairness.  

Example:  
```
ReentrantLock lock = new ReentrantLock();  
lock.lock();  
try {  
    // Critical section  
} finally {  
    lock.unlock();  
}  
```
---

### 9. How do you implement a producer-consumer problem using blocking queues?
Blocking queues like `ArrayBlockingQueue` handle producer-consumer scenarios efficiently.  

Example:  
```
BlockingQueue<Integer> queue = new ArrayBlockingQueue<>(10);  

Thread producer = new Thread(() -> {  
    try {  
        queue.put(1);  
    } catch (InterruptedException e) {  
        Thread.currentThread().interrupt();  
    }  
});  

Thread consumer = new Thread(() -> {  
    try {  
        int item = queue.take();  
        System.out.println("Consumed: " + item);  
    } catch (InterruptedException e) {  
        Thread.currentThread().interrupt();  
    }  
});  

producer.start();  
consumer.start();  
```
---

### 10. What is the difference between CyclicBarrier and CountDownLatch?
- **CyclicBarrier**: Allows a group of threads to wait for each other to reach a common point. It can be reused.  
- **CountDownLatch**: Allows one or more threads to wait until a set of operations are completed. It cannot be reused.  

Example of CountDownLatch:  
```
CountDownLatch latch = new CountDownLatch(3);  

Thread worker = new Thread(() -> {  
    latch.countDown();  
});  

worker.start();  
latch.await(); // Waits until the count reaches zero  
```
---

# Java Memory and Garbage Collection

### 1. Describe the Java memory model and garbage collection process.
The Java memory model divides memory into the following regions:
- **Heap**: Stores objects and class instances.
- **Stack**: Stores method-specific values and references.
- **Metaspace**: Stores metadata of classes.

Garbage collection is the process of identifying and reclaiming unused objects in the heap to free memory.

---

### 2. How does Java handle memory leaks?
Java handles memory leaks by relying on garbage collection. However, memory leaks can still occur when objects are referenced unnecessarily, preventing garbage collection. Tools like VisualVM or profilers can help detect and resolve memory leaks.

---

### 3. How does Java's garbage collector work and what are the different types of garbage collectors available in Java?
Java's garbage collector works by marking objects that are no longer reachable and reclaiming their memory. Common garbage collectors include:
- **Serial GC**: Single-threaded garbage collection.
- **Parallel GC**: Multi-threaded garbage collection.
- **CMS (Concurrent Mark-Sweep) GC**: Low-latency garbage collection.
- **G1 GC (Garbage First)**: Balances throughput and low latency.
- **ZGC**: Scalable, low-latency garbage collection introduced in Java 11.
- **Shenandoah GC**: Reduces pause times by concurrent compaction.

---

### 4. Discuss the continuous improvements in garbage collection mechanisms in Java, focusing on recent updates like G1 and ZGC collectors.
- **G1 GC**: Introduced in Java 9, it divides the heap into regions and prioritizes garbage collection of regions with the most garbage. It reduces pause times compared to CMS.
- **ZGC**: Introduced in Java 11, it performs most of the garbage collection work concurrently, resulting in low pause times even on large heaps.
- **Shenandoah GC**: Introduced in Java 12, it reduces pause times by compacting the heap while the application is running.

