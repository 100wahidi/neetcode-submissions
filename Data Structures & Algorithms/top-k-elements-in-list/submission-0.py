class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        H_map={}
        S=[]
        for num in nums:
            H_map[num]=H_map.get(num, [0, num])
            H_map[num][0]+=1
        S=[e[1] for e in sorted(H_map.values())]

        return S[-k:]

            
        

        