class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N1=set(nums1)
        N2=set(nums2)
        for e in N1.copy():
            if e not in N2: 
                N1.discard(e)

        return list(N1)