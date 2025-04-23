# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        def dfs(node):
            if not node:
                result.append("null")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        result = []
        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def dfs():
            val = next(values)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        
        values = iter(data.split(","))
        return dfs()

# Example Usage
# Construct binary tree: [1, 2, 3, null, null, 4, 5]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# Create Codec object
codec = Codec()

# Serialize the tree
serialized = codec.serialize(root)
print(f"Serialized: {serialized}")  # Output: "1,2,null,null,3,4,null,null,5,null,null"

# Deserialize the string back to tree
deserialized_root = codec.deserialize(serialized)
