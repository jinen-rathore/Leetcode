# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = [0]
        self.bstToGstHelper(root, total)
        return root
        
    def bstToGstHelper(self, root, total):
        if root is None:
            return
        
        self.bstToGstHelper(root.right, total)

        total[0] += root.val
        root.val = total[0]

        self.bstToGstHelper(root.left, total)


        