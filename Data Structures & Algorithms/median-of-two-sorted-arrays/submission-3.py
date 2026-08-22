class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        bF = nums1+nums2
        for i in range(len(bF)):
            for j in range(i+1,len(bF)):
                if bF[j]<=bF[i]:
                   bF[i],bF[j]=bF[j],bF[i]
        if (len(bF))%2==0:
            return (bF[(len(bF)//2)-1]+bF[len(bF)//2])/2
        else:
            return bF[len(bF)//2]

        