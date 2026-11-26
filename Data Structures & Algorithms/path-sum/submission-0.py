# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,t):
            if not root:
                return False
            if not root.left and not root.right:
                return True if t - root.val == 0 else False
            return dfs(root.left, t - root.val) or dfs(root.right, t - root.val)
        
        return dfs(root,targetSum)