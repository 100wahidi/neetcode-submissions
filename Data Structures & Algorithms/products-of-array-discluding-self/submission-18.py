class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sol = [0]*n
        stop = n//2
        count = 0
        if n%2!=0:
            prod = nums[n-1]
        else:
            prod = 1
        for i in range(stop):
            if nums[i]!=0:
               prod*=nums[i]
            else:
                count+=1
            if nums[i+stop]!=0:
               prod*=nums[i+stop]
            else:
               count+=1
        if count>1:
            return sol
        for i in range(n//2):
            if nums[i]==0:
                sol = [0]*n
                sol[i]=prod
                return sol
            elif nums[i+stop]==0:
                sol = [0]*n
                sol[i+stop]=prod
                return sol
            else:
                sol[i]=prod//nums[i]
                sol[i+stop]=prod//nums[i+stop]
        if n%2!=0:
            sol[n-1] = prod//nums[n-1]


        return sol