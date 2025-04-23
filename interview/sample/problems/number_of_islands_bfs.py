from collections import deque

def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        while queue:
            row, col = queue.popleft()
            # Explore all 4 directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'  # Mark as visited
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # Found an unvisited land
                island_count += 1
                bfs(r, c)

    return island_count

# Example Usage
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(numIslands(grid))  # Output: 3
