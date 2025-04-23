# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    # Base case: if root is None, or root is one of the nodes (p or q), return root
    if not root or root == p or root == q:
        return root
    
    # Search for LCA in the left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    # If both left and right are non-null, the current root is the LCA
    if left and right:
        return root
    
    # Otherwise, return the non-null child (either left or right)
    return left if left else right

# Example Usage
# Construct binary tree: [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

p = root.left         # Node 5
q = root.left.right.right  # Node 4

print(lowestCommonAncestor(root, p, q).val)  # Output: 5
