class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return '*****'
        ans = '-'.join(strs)
        return ans

    def decode(self, s: str) -> List[str]:
        if s == '*****':
            return []
        ans = s.split('-')
        return ans
        
