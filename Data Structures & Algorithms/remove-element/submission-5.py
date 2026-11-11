class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        def swap(x,y, num):
            temp = num[x]
            num[x] = num[y]
            num[y] = temp

        x = 0
        y = len(nums) - 1
        while x <= y:
            # if nums[y] == val:
            #     y -= 1
            if nums[x] == val and nums[y] != val:
                swap(x,y,nums)
                x += 1
                y -= 1
            elif  nums[x] != val and nums[y] != val:
                x += 1
            elif nums[x] == val and nums[y] == val:
                y -= 1
            elif nums[x] != val and nums[y] == val:
                x +=1
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                count += 1

        # print(i)
        print(nums)
        return count