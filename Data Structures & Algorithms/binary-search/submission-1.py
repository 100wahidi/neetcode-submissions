class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # transfer it to an abstraction
        # half Hot Dog >=target include 4 returns first 4 

        low, high=0, len(nums)-1
        while(low<=high):
            middle=(low+high)//2
            if nums[middle]>=target:
               high=middle-1
            else:
                low=middle+1

        if low>len(nums)-1 or nums[low]!=target:
            return -1
        return low
            
        