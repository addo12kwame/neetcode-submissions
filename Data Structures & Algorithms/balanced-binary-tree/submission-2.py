# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(r):
            
            if not r:
                return (True, 0)
            left_more = helper(r.left)
            right_more = helper(r.right)
            is_balanced = (left_more[0] and right_more[0]) and abs( left_more[1]-  right_more[1]) <= 1
            
            return (is_balanced,1 + max(left_more[1],right_more[1]) )
            
        # print(helper(root))
        return helper(root)[0]
         