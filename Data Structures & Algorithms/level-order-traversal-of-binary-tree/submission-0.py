# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []
        if not root:
            return ans
        q = deque([root])
        while len(q) > 0:
            temp_ans = []
            for i in range(len(q)):
                c = q.popleft()
                if c:
                    temp_ans.append(c.val)
                if c and c.left:
                    q.append(c.left)
                if c and c.right:
                    q.append(c.right)
            ans.append(temp_ans)

        return ans
        