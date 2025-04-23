class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return None

    # A hashmap to store the mapping of original node to its clone
    cloned = {}

    def dfs(node):
        if node in cloned:
            return cloned[node]
        
        # Clone the current node
        copy = Node(node.val)
        cloned[node] = copy
        
        # Recursively clone all the neighbors
        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))
        
        return copy

    return dfs(node)

# Example Usage
# Input graph:
# 1 -- 2
# |    |
# 4 -- 3

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

cloned_graph = cloneGraph(n1)
print(cloned_graph.val)  # Output: 1
