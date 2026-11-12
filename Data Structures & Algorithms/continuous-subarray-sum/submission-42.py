class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modulo=0
        CumSum=0
        Hash_Map={0:-1}
        for i in range(len(nums)):
            CumSum+=nums[i]
            modulo=CumSum%k
            if modulo in Hash_Map:
                if i-Hash_Map[modulo]>1:
                    return True
            Hash_Map[modulo]=min(Hash_Map.get(modulo, i), i)

        return False
            
            

        