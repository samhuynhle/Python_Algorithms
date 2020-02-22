# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# stored result in variable to return at the end.
class Solution:
    result = None
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return
        if root.val == val:
            self.result = root
        else:
            if val < root.val:
                self.searchBST(root.left, val)
            else:
                self.searchBST(root.right, val)
        
        return self.result

# updated when/what we are returning (the return of each call); also using Python's ternary syntax
class Solution2:
    def searchBST(self, root, val):
        if root == None or root.val == val:
            return root
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)