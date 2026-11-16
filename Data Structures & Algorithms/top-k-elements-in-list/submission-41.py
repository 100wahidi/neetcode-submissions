class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        H_map={}
        heap=[]
        S=[]
        for i in range(len(nums)):
            H_map[nums[i]]=H_map.get(nums[i], 0)+1
        

        for i, K in enumerate(H_map.keys()):
            heapq.heappush(heap, (-H_map[K], K))
            if i>len(H_map)-k-1:
                S.append(heapq.heappop(heap)[1])

        return S

