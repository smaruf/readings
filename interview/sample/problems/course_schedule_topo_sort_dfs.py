def canFinish(numCourses, prerequisites):
    # Build the adjacency list
    adj_list = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
    
    # Track visited nodes
    visited = [0] * numCourses  # 0 = not visited, 1 = visiting, 2 = fully visited

    def dfs(course):
        if visited[course] == 1:  # Cycle detected
            return False
        if visited[course] == 2:  # Already processed
            return True
        
        visited[course] = 1  # Mark as visiting
        for neighbor in adj_list[course]:
            if not dfs(neighbor):
                return False
        
        visited[course] = 2  # Mark as fully visited
        return True

    # Check each course for cycles
    for course in range(numCourses):
        if not dfs(course):
            return False
    
    return True

# Example Usage
numCourses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]
print(canFinish(numCourses, prerequisites))  # Output: True
