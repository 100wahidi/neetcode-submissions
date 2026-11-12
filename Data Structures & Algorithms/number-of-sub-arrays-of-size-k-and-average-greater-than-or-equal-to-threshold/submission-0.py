class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        CumSum=sum(arr[:k])/k
        Ct=0
        if CumSum>=threshold:
            Ct+=1
        for i in range(k, len(arr)):
            CumSum+=(-arr[i-k]+arr[i])/k
            if CumSum>=threshold:
                Ct+=1
        return Ct
        