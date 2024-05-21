class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0
    else:
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        return 1 + max(left_depth,right_depth)


# Example usage
# Creating a binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(None)
root.left.right = TreeNode(None)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxDepth(root))  # Output: 3

root = TreeNode(1)
root.left = TreeNode(None)
root.right = TreeNode(2)

print(maxDepth(root))