class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dics = {}
        dictt = {}
        s1 = sorted(s)
        t1 = sorted(t)

        if s1 == t1:
            return True
        return False

        
             
