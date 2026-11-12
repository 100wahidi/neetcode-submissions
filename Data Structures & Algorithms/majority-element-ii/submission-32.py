class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # O(1)
        # can you do better:
        nums1, nums2=-1, -1
        ct1, ct2=0, 0
        S=[]
        for n in nums:
            if n==nums1:
                ct1+=1
            elif n==nums2:
                ct2+=1
            elif ct1==0:
                ct1=1
                nums1=n
            elif ct2==0:
                ct2=1
                nums2=n
            else:
                ct1-=1
                ct2-=1
        ct1=nums.count(nums1)
        ct2=nums.count(nums2)
        if ct1>=(len(nums)//3)+1:
            S.append(nums1)
        if ct2>=(len(nums)//3)+1:
            S.append(nums2)

        print(nums1, nums2)
        
        return S

        
        
        