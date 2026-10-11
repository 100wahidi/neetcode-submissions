class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes=0
        prod=1
        if nums[0]==0:
            zeroes+=1
            prod =1
        else:
            prod=nums[0]

        for i in range(1,len(nums)):
            if nums[i]!=0:
                prod*=nums[i]
            else:
                zeroes+=1
            if zeroes>1:
                return [0]*len(nums)
        for j in range(len(nums)):
            if nums[j]==0:
                nums[j]=prod
            else:
                if zeroes:
                    nums[j]=0
                else:
                    nums[j]=prod//nums[j]
        return nums

     
        