class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # O(n) hash map 
        H_mp={}
        S=[]
        for n in nums:
            H_mp[n]=1+ H_mp.get(n, 0)
        
        for x, y in H_mp.items():
            if y>=len(nums)//3+1:
                S.append(x)

        return S

        