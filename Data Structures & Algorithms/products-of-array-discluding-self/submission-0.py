class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix=prefix=1
        L=[]
        for i in range(len(nums)):
            suffix*=nums[len(nums)-i-1]
            L.append(suffix)
            
        k=[]
        for j in range(len(nums)-1):
            k.append(L[len(nums)-j-2]*prefix)
            prefix*=nums[j]
        k.append(prefix)
            
            
        return k
        
            

        