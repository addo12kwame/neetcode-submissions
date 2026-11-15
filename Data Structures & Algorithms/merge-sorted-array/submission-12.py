class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m+n -1
        l = m-1
        r = n-1
        if n ==0:
            return nums1
        while l >= 0 and r >= 0:
            if nums1[l] >= nums2[r]:
                nums1[k] = nums1[l]
                l -= 1
            else:
                nums1[k] = nums2[r]
                r -= 1
            k -= 1

        print(f"k {k}")
        print(f"l {l}")
        print(f"r {r}")
        while l >= 0:
            nums1[k] = nums1[l]
            l -=1
            k-= 1
        while r >= 0:
            nums1[k] = nums2[r]
            r -=1   
            k -=1 
        

    def swap(self,x,y,arr1,arr2):
        temp = arr1[x]
        arr1[x] = arr2[y]
        arr2[y] = temp