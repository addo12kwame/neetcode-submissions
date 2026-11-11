class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        strs1 = strs
        dic = []

        for i in range(len(strs)):
            bucket = []
            if strs[i] in dic:
                continue
            first = sorted(strs[i])
            bucket.append(strs[i])
            for j in range(i+1,len(strs)):
                second = sorted(strs[j])
                if first == second:
                    bucket.append(strs[j])
                    dic.append(strs[j])
            final.append(bucket)
            

        return final


        