from collections import deque

def canFinish(numCourses, prerequisites):
    # Build the adjacency list and in-degree array
    adj_list = {i: [] for i in range(numCourses)}
    in_degree = [0] * numCourses
    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
        in_degree[course] += 1
    
    # Add all courses with in-degree 0 to the queue
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    processed_courses = 0

    while queue:
        course = queue.popleft()
        processed_courses += 1
        for neighbor in adj_list[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If all courses are processed, return True
    return processed_courses == numCourses

# Example Usage
numCourses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]
print(canFinish(numCourses, prerequisites))  # Output: True
