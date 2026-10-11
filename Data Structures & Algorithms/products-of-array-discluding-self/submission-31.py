class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        n=len(nums)
        res = [0]*n
        s = [0]*n
        for i in range(n):
            left*= nums[i]
            res[i]=left
        
        for j in range(n-1, 0, -1):
            s[j]= right*res[j-1]
            right = right*nums[j]
        s[0]=right

        return s

    
