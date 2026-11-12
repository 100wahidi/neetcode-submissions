class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # init a hash map to store cumsums with index 
        H_map={0:-1}
        CumSum=0
        for i, num in enumerate(nums):
            CumSum+=num
            modulo=CumSum%k
            if modulo in H_map and (i-H_map[modulo])>1:
                return True
            H_map[modulo]=min(i, H_map.get(modulo, i)) 

        return False

        