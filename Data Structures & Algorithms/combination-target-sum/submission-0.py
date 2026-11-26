class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr = []

        def comb(nums,i,cur = [], sum = 0):
            if i >= len(nums):
                if sum == target:
                    arr.append(cur[:])
                    return
                return
            if sum == target:
                    arr.append(cur[:])
                    return
            elif sum > target:
                return                
            cur.append(nums[i])
            comb(nums,i, cur, sum + nums[i])
            cur.pop()
            comb(nums,i + 1, cur, sum)
        comb(nums,0)
        return arr


        