# Java Interview Topics

## 1. Object-Oriented Programming

- **Explain the code of Object-Oriented Programming in Java.**
  - Object-Oriented Programming (OOP) in Java involves creating classes that represent objects with attributes and methods. It incorporates principles like encapsulation, inheritance, polymorphism, and abstraction. For example:
    ```java
    public class Animal {
        private String name;
        
        public Animal(String name) {
            this.name = name;
        }
        
        public void makeSound() {
            System.out.println("Some sound");
        }
    }
    
    public class Dog extends Animal {
        public Dog(String name) {
            super(name);
        }
        
        @Override
        public void makeSound() {
            System.out.println("Bark");
        }
    }
    ```

- **Discuss the differences between an abstract class and an interface in Java.**
  - An abstract class can have both abstract methods (without implementation) and concrete methods (with implementation), while an interface can only have abstract methods (Java 8 onwards allows default and static methods). Abstract classes can have fields, constructors, and can provide partial implementation. Interfaces are used to define a contract that implementing classes must follow.

- **How can polymorphism be implemented and utilized in Java?**
  - Polymorphism in Java can be implemented through method overriding and method overloading. It allows objects to be treated as instances of their parent class rather than their actual class. For example:
    ```java
    Animal myDog = new Dog("Buddy");
    myDog.makeSound(); // Outputs: Bark
    ```

- **Explain Java's method overloading and method overriding, and how they differ.**
  - Method overloading occurs when multiple methods in the same class have the same name but different parameters. Method overriding occurs when a subclass provides a specific implementation for a method that is already defined in its superclass.

## 2. Java Collections Framework

- **What are the main differences between List, Set, and Map in the Java Collections Framework?**
  - List: An ordered collection that allows duplicate elements. Example: `ArrayList`.
  - Set: An unordered collection that does not allow duplicate elements. Example: `HashSet`.
  - Map: A collection of key-value pairs with unique keys. Example: `HashMap`.

- **How does the implementation of HashMap work in Java?**
  - `HashMap` in Java uses an array of buckets to store key-value pairs. Each bucket is essentially a linked list. When a key-value pair is added, the hash code of the key is computed and used to determine the bucket index. If multiple keys hash to the same index, they are stored in the same bucket using a linked list.

- **Explain the difference between ArrayList and LinkedList.**
  - `ArrayList` is backed by a dynamic array, providing O(1) time complexity for random access but O(n) for insertions and deletions. `LinkedList`, on the other hand, is a doubly linked list, providing O(1) for insertions and deletions but O(n) for random access.

## 3. Java Threads and Concurrency

- **What are Java threads and how do you create and manage them?**
  - Java threads allow concurrent execution of code. They can be created by extending the `Thread` class or implementing the `Runnable` interface. Managing threads can be done using thread pools from the `Executor` framework.

- **How does the synchronized keyword work and when should it be used?**
  - The `synchronized` keyword ensures that only one thread can execute a block of code or method at a time, preventing race conditions. It should be used when accessing shared resources from multiple threads.

- **Explain the concept of a thread pool and its advantages.**
  - A thread pool manages a pool of worker threads, reusing them to execute tasks, reducing the overhead of creating and destroying threads. It improves performance and resource management.

- **What is the difference between the wait() and sleep() methods in Java?**
  - The `wait()` method is used for inter-thread communication and releases the lock on the object, while `sleep()` pauses the current thread for a specified time without releasing the lock.

