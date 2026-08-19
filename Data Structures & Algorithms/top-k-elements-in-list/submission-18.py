class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n]=1+d.get(n,0)
        l = list(d.keys())
        i=0
        for i in range(k):
            for j in range(i+1,len(l)):
                if d[l[j]]>=d[l[i]]:
                   l[j],l[i]=l[i],l[j] 

        return l[:k]


        
        