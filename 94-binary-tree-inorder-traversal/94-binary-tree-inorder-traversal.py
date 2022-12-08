# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        if root:
            l += self.inorderTraversal(root.left)
            l += [root.val]
            l += self.inorderTraversal(root.right)
        return  l
            
            