class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix=prefix=1
        L=[0]*len(nums)
        for i in range(len(nums)):
            suffix*=nums[len(nums)-i-1]
            L[len(nums)-1-i]=suffix

        for j in range(len(nums)-1):
            L[j]=L[j+1]*prefix
            prefix*=nums[j]
        L[len(nums)-1]=prefix
        
        return L
        
            

        