class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        seen0 = set()
        sol = []

        for i in range(len(nums)):
            target = -nums[i]
            hash = set()
            if nums[i] not in seen0:
                seen1 = set()

                for j in range(i+1,len(nums)):
                    if nums[j] not in seen0 and nums[j] not in seen1:
                        if target-nums[j] in hash :
                            sol.append([nums[i],nums[j],target-nums[j]])
                            seen1.add(nums[j])
                        else:
                            hash.add(nums[j])
            seen0.add(nums[i])           

        return sol




        



        