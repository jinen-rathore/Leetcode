# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        #ancestor holds the values of max,min
        def helper(root, ancestor):
            if not root.left and not root.right:
                # a leaf
                max_ = max(ancestor[0], root.val)
                min_ = min(ancestor[1], root.val)
                return abs(max_ - min_)
            
            left_val, right_val = 0, 0
            prev_max, prev_min = ancestor 
            if root.left:
                ancestor[0] = max(ancestor[0], root.val)
                ancestor[1] = min(ancestor[1], root.val)
                left_val = helper(root.left, ancestor)
                ancestor[0], ancestor[1] = prev_max, prev_min
            
            if root.right:
                ancestor[0] = max(ancestor[0], root.val)
                ancestor[1] = min(ancestor[1], root.val)
                right_val = helper(root.right, ancestor)
                ancestor[0], ancestor[1] = prev_max, prev_min
           
            return max(left_val, right_val)
        
        return helper(root, [float("-inf"), float("inf")])
            