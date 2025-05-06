from collections import deque

def wordBreak(s, wordDict):
    wordSet = set(wordDict)  # Convert wordDict to a set for O(1) lookup
    n = len(s)
    queue = deque([0])  # Start BFS from index 0
    visited = set()  # Keep track of visited indices to avoid redundant work

    while queue:
        start = queue.popleft()
        if start in visited:
            continue
        visited.add(start)

        for end in range(start + 1, n + 1):
            if s[start:end] in wordSet:
                if end == n:  # If we reach the end of the string
                    return True
                queue.append(end)

    return False
