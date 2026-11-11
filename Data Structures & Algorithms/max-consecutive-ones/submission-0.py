class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxy = 0
        
        count = 0
        for i in nums:
            
            if i == 1:
                count +=1
                print(count)
            else:
                count = 0
            maxy = max(count, maxy)
        
        return maxy
                
        