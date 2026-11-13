class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # bruthe force 
        heap=[]
        reserve=k
        count=0
        Length=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                if reserve>0:
                    heapq.heappush(heap,i)
                    count+=1
                    reserve-=1
                else:
                    heapq.heappush(heap,i)
                    count=i-heapq.heappop(heap)
            Length=max(Length, count)
        return Length

        