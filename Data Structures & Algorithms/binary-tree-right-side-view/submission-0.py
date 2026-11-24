# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        ans.append(queue[-1].val)
        while len(queue) > 0:
            for i in range(len(queue)):
                c = queue.popleft()
                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)
            if queue:
                ans.append(queue[-1].val)
        return ans
            


            

        