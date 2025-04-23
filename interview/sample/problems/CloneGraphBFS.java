import java.util.*;

// Definition for a Node
class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new ArrayList<>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<>();
    }

    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}

public class CloneGraphBFS {
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }

        // A hashmap to store the mapping of original node to its clone
        Map<Node, Node> cloned = new HashMap<>();

        // Clone the root node
        cloned.put(node, new Node(node.val));
        Queue<Node> queue = new LinkedList<>();
        queue.add(node);

        while (!queue.isEmpty()) {
            Node current = queue.poll();

            // Iterate through the neighbors
            for (Node neighbor : current.neighbors) {
                if (!cloned.containsKey(neighbor)) {
                    // Clone and store the neighbor
                    cloned.put(neighbor, new Node(neighbor.val));
                    queue.add(neighbor);
                }

                // Add the cloned neighbor to the current node's clone
                cloned.get(current).neighbors.add(cloned.get(neighbor));
            }
        }

        return cloned.get(node);
    }
}
