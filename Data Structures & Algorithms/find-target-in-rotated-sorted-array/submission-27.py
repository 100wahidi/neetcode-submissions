class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        loop = len(nums)
        min = 0
        max = loop-1
        if loop==1 and nums[loop-1]==target:
            return 0
        while min!=max:
            ptr = (min+max)//2
            print(nums[min],nums[max],nums[ptr])

            if nums[max]==target:
                return max
            elif nums[min]==target:
                return min

            if nums[max]>nums[min]:
                if nums[ptr]>target:
                    max = ptr-1
                elif nums[ptr]<target:
                    min = ptr+1
                else:
                    return ptr
            elif nums[max]<nums[min]:
                if target>nums[ptr]:
                    if nums[ptr]>=nums[min]:
                        min = ptr+1
                    elif nums[ptr]<=nums[min] and target<nums[max]:
                        min = ptr+1
                    elif nums[ptr]<=nums[min] and target>nums[max]:
                        max = ptr-1
                elif target<nums[ptr]:
                    if nums[ptr]>=nums[min]:
                        if nums[min]<target:
                            max = ptr-1     
                        elif nums[min]>=target:
                            min = ptr+1
                    elif nums[ptr]<=nums[min]:
                        max = ptr-1
                else:
                    return ptr
            else:
                if nums[max]==target:
                    return max
                else:
                    return -1

        return -1              
      
                                     
                                   
                    