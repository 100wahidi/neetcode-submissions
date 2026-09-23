class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = []
        for i in range(len(nums)):

            if nums[i]>0:
                break
            print(i)
            if i>0 and nums[i-1]==nums[i]:
                continue
            r, l = len(nums)-1, i+1
            target = -nums[i]
            while(r>l):
                if  nums[l] + nums[r] == target:
                    s.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
                    l+=1
                elif  nums[l] + nums[r] < target:
                    l+=1
                elif nums[l] + nums[r] > target:
                    r-=1         
        return s