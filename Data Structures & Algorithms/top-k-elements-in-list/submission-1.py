import inspect
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        ans = []
        final = []
        
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1

        for key, value in dic.items():
            ans.append({'key': key, 'value': value})
        
        listed = sorted(ans, key=lambda x: x['value'],reverse=True)
        for i in range(k):
            final.append(listed[i]['key'])
        return final