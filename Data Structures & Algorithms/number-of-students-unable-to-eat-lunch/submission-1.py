
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cmap = Counter(students)
        for i in sandwiches:
            if cmap[i] > 0:
                cmap[i] -= 1
            else:
                break
        return cmap[0] + cmap[1]
        