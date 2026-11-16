from math import sqrt
from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for point in points:
            r = sqrt((point[0]-0)**2 + (point[1]-0)**2)
            print(point[0])
            arr.append((r, point))
        heapify(arr)

        ans = []
        for i in range(k):
            ans.append(heappop(arr)[1])
        return ans