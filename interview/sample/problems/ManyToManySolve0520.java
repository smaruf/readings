import java.util.*;
import lombok.Value;

public class ManyToManySolve0520 {
    /*
     * 
     * You are given three lists:
     * 
     * `List<Task>` – each task has an `id` and a `title`.
     * 
     * `List<Developer>` – each developer has an `id` and a `name`.
     * 
     * `List<Assignment>` – each assignment maps a `developerId` to a `taskId`.
     * 
     * # Goal:
     * 
     * Write a method that returns a `Map<String, List<String>>` where:
     * 
     * The 'key' is the developer's 'name'.
     * 
     * The 'value' is the list of 'titles of tasks' assigned to that developer.
     * 
     * # Requirements:
     * 
     * 1. Include all developers in the result, even if they have no assignments.
     * 
     * If a developer has no valid assignments, map their name to an empty list.
     * 
     * 2. Skip any assignments that:
     * 
     * Refer to a `taskId` not found in the list of tasks.
     * 
     * Refer to a `developerId` not found in the list of developers.
     * 
     * # Example:
     * 
     * If:
     * 
     * Developer: `Alice(id=1)`, `Bob(id=2)`
     * 
     * Tasks: `Login(id=10)`, `Dashboard(id=20)`
     * 
     * Assignments: `(developerId=1, taskId=10)`, `(developerId=3, taskId=20)`,
     * `(developerId=2, taskId=99)`
     * 
     * Then output:
     * 
     * {
     * 
     * "Alice": ["Login"],
     * 
     * "Bob": []
     * 
     * }
     * 
     */

    public static Map<String, List<String>> report(
            List<Task> tasks,
            List<Developer> developers,
            List<Assignment> assignments) {
        // Create a map for quick lookup of tasks by their ID
        Map<Integer, String> taskMap = new HashMap<>();
        for (Task task : tasks) {
            taskMap.put(task.id, task.title);
        }

        // Create a map for quick lookup of developers by their ID
        Map<Integer, String> developerMap = new HashMap<>();
        for (Developer developer : developers) {
            developerMap.put(developer.id, developer.name);
        }

        // Initialize the result map with all developers and empty task lists
        Map<String, List<String>> result = new HashMap<>();
        for (Developer developer : developers) {
            result.put(developer.name, new ArrayList<>());
        }

        // Process assignments
        for (Assignment assignment : assignments) {
            String developerName = developerMap.get(assignment.developerId);
            String taskTitle = taskMap.get(assignment.taskId);

            // Only add the task if both the developer and task exist
            if (developerName != null && taskTitle != null) {
                result.get(developerName).add(taskTitle);
            }
        }

        return result;
    }

    @Value
    public static class Task {
        int id;
        String title;
    }

    @Value
    public static class Developer {
        int id;
        String name;
    }

    @Value
    public static class Assignment {
        int taskId;
        int developerId;
    }

    public static void main(String[] args) {
        // Example data
        List<Task> tasks = List.of(
                new Task(10, "Login"),
                new Task(20, "Dashboard"));

        List<Developer> developers = List.of(
                new Developer(1, "Alice"),
                new Developer(2, "Bob"));

        List<Assignment> assignments = List.of(
                new Assignment(10, 1),
                new Assignment(20, 3),
                new Assignment(99, 2));

        // Generate the report
        Map<String, List<String>> report = report(tasks, developers, assignments);

        // Print the result
        System.out.println(report);
    }
}
