class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        def sub(nums,i, cur = []):
            if i >= len(nums):
                arr.append(cur[:])
                return 
            cur.append(nums[i])
            sub(nums,i+1, cur)
            cur.pop()
            sub(nums,i+1, cur)
        sub(nums,0)
        return arr
            

        