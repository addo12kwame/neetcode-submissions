class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(k):
            t = 0
            for i in piles:
                t += math.ceil(float(i)/ k)
            if t <= h:
                print(f"T {t} is <= H {h}")
                return True
            return False
        l = 1
        r = max(piles)
        MINN = r
        while l <= r:
            mid = (l + r) // 2
            if isValid(mid):
                MINN = mid
                r = mid - 1
            else:
                print(f"Something happened at mid {mid}")
                l = mid + 1
                print(f"mid in l {mid}")

            
        return MINN


        