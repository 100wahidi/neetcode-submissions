class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # best ime to apply the minutes
        maxisio=0
        best=-1
        H={-1:0}
        index=-1
        for i in range(len(grumpy)):
            if grumpy[i]==1:
                maxisio=sum(customers[i:i+minutes])
                if maxisio>=best:
                    index=i
                    best=maxisio
            if grumpy[i]==0:
                H[i]=H.get(i-1, 0)+customers[i]
            else:
                H[i]=H.get(i-1, 0)
        
        Cum=0
        r=0
        while(r<len(grumpy)):
            if grumpy[r]==1:
                if r<=len(grumpy)-minutes:
                    Cum=max(Cum,H[r-1]+sum(customers[r:r+minutes])+H[len(grumpy)-1]-H[r+minutes-1])
                else:
                    print(r)
                    Cum=max(Cum, H[r-1]+sum(customers[r:]))
            r+=1

        return Cum if Cum!=0 else H[len(grumpy)-1]

        