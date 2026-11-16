class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2

        while l <= r:
            if nums[mid] == target:
                return mid
            if  target >= nums[mid]:
                l = mid + 1             
            else:
                r = mid - 1
            mid = (l + r) // 2 
            if nums[mid]:
                print(f"mid -> {mid}, l -> {l}, r -> {r}, nums[{mid}] -> {nums[mid]}")
        return -1

        