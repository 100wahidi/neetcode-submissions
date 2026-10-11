class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map={}
        freq=[[] for i in range(len(nums)+1)]
        ctr=0
        s=[]
        for n in nums:
            h_map[n]=h_map.get(n,0)+1
        for v,w in h_map.items():
            freq[w].append(v)

        for i in range(len(freq)):
            s+=freq[i]

        return s[-k:]

        
        