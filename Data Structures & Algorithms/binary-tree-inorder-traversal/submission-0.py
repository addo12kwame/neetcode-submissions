# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(roots):
            if not roots:
                return
            if roots.left:
                helper(roots.left)
            ans.append(roots.val)
            if roots.right:
                helper(roots.right)
        helper(root)
        return ans
