class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modulo=0
        CumSum=0
        Hash_Map={}
        for i in range(len(nums)):
            
            CumSum+=nums[i]
            modulo=CumSum%k
            print(i, modulo)
            if i>=1 and modulo==0:
                return True
            if modulo in Hash_Map:
                if CumSum>=k and i-Hash_Map[modulo]>1:
                    return True
            Hash_Map[modulo]=min(Hash_Map.get(modulo, i), i)

        return False
            
            

        