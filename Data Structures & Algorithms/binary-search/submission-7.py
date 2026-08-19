class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums)-1
        ptr=1
        if nums[max]==target:
            return max
        if nums[min]==target:
            return min
        while min != max and ptr!=0:
            if nums[max] == target:
                return max
            elif nums[min] == target:
                return min
            ptr = int((min+max)/2)
            if nums[ptr]>target:
                max = ptr-1
            elif nums[ptr]<target:
                min = ptr+1
            else:
                return ptr   
         
        return -1
            
             