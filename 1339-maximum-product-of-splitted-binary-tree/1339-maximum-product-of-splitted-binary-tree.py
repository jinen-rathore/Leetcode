# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # creating a sum sub tree where every node contains sum 
        def sumTree(root):
            if not root:
                return 0
            # taking current sum at every node
            currSum = sumTree(root.left) + sumTree(root.right) + root.val
            # this is the logic for creating a max sum sub tree 
            self.maximum = max(self.maximum, (self.totalSum-currSum)*currSum)
            
            return currSum
        
        self.maximum = 0
        self.totalSum = 0
        # first calling the sumTree function to get the sum sub tree
        self.totalSum = sumTree(root)
        # then calling the function for the product
        sumTree(root)
        
        return self.maximum %(10 ** 9+7)