from collections import deque

def cloneGraph(node):
    if not node:
        return None

    # A hashmap to store the mapping of original node to its clone
    cloned = {}
    
    # Clone the root node
    cloned[node] = Node(node.val)
    queue = deque([node])

    while queue:
        current = queue.popleft()
        
        # Iterate through the neighbors
        for neighbor in current.neighbors:
            if neighbor not in cloned:
                # Clone and store the neighbor
                cloned[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            
            # Add the cloned neighbor to the current node's clone
            cloned[current].neighbors.append(cloned[neighbor])
    
    return cloned[node]
