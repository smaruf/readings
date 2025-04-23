# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return None
    # Swap left and right children
    root.left, root.right = root.right, root.left
    # Recursively invert left and right subtrees
    invertTree(root.left)
    invertTree(root.right)
    return root

# Example Usage
# Input: [4, 2, 7, 1, 3, 6, 9]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Invert the tree
inverted_root = invertTree(root)
print(inverted_root.val)  # Output: 4 (root remains the same)
