import numpy as np
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        S=[]
        for i in range(len(points)):
            distance=np.sqrt(points[i][0]**2+points[i][1]**2)
            heapq.heappush(heap, (-distance, i))
            if i>=k:
                heapq.heappop(heap)
        for i in range(k):
            S.append(points[heapq.heappop(heap)[1]])
        return S

        