class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # brUthe force 
        # l should be the biggest min of x
        # r should be the smallest max if
        if x<=arr[0]:
            return list(arr[:k])
        if x>=arr[-1]:
            return list(arr[-k:])
        min_heap=[]
        r, l=0, len(arr)-1
        for i in range(len(arr)):
            if arr[i]>=x:
                r, l= i, i-1
                break
        
        while(r-l<k+1):
                if abs(arr[l]-x)<abs(arr[r]-x):
                    min_heap.append(arr[l])
                    l-=1
                elif abs(arr[l]-x)>abs(arr[r]-x):
                    min_heap.append(arr[r])
                    r+=1
                else:
                    min_heap.append(arr[l])
                    l-=1
     
        return sorted(min_heap[:k])


        