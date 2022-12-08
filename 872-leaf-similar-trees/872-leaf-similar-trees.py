# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        #Stack for root1
        s11 = []
        s12 = []
        
        #Stack for root2
        s21 = []
        s22 = []

        s11.append(root1)
        while(len(s11) != 0):
            curr = s11.pop()

            if curr.left:
                s11.append(curr.left)
            if curr.right:
                s11.append(curr.right)

            if not curr.left and not curr.right:
                s12.append(curr.val)
        
        s21.append(root2)

        while(len(s21)!=0):
            curr = s21.pop()

            if curr.left:
                s21.append(curr.left)
            if curr.right:
                s21.append(curr.right)

            if not curr.left and not curr.right:
                s22.append(curr.val)

        return s12 == s22  
