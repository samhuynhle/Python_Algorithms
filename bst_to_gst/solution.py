# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.prevSum = 0
        self.rightOrder(root)
        return root
        
    def rightOrder(self, node):
        if node:
            self.rightOrder(node.right)
            oldVal = node.val
            node.val += self.prevSum
            self.prevSum += oldVal
            self.rightOrder(node.left)