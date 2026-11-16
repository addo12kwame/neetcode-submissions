class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        l , r = 0, len(matrix) - 1 


        while l <= r:
            mid = (l + r) // 2
            if target ==  matrix[mid][0]:
                return True
            elif target < matrix[mid][0]:
                l2, r2 = 0, len(matrix[mid]) - 1
                while l2 <= r2:
                    mid2 = (l2 + r2) // 2
                    if target ==  matrix[mid][mid2]:
                        return True
                    elif target < matrix[mid][mid2]:
                        r2 = mid2 - 1
                    else:
                        l2 = mid2 + 1
                r = mid - 1
            else:
                l2, r2 = 0, len(matrix[mid]) - 1
                while l2 <= r2:
                    mid2 = (l2 + r2) // 2
                    if target ==  matrix[mid][mid2]:
                        return True
                    elif target < matrix[mid][mid2]:
                        r2 = mid2 - 1
                    else:
                        l2 = mid2 + 1
                l = mid + 1 


        return False 
