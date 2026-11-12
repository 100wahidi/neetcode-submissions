class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x=sorted(nums1+nums2)
        if len(x)%2==0:
            return (x[(len(x)-1)//2]+x[(len(x)-1)//2+1])/2
        return x[(len(x)-1)//2]


        