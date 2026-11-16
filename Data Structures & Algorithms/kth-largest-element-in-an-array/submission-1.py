class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
   
        for i in nums:
            heapq.heappush(heap, i)
        for i in range(len(nums)-k+1):
            Kesit=heapq.heappop(heap)

        return Kesit if len(nums)>0 else nums[0]
            
        