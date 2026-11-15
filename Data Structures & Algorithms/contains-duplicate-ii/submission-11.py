class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()
        Left=0
        for i in range(len(nums)):
            if i>k:
                window.remove(nums[Left])
                Left+=1
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False


