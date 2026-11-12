class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # optimal
        items=sorted(items)
        maximosis=0
        Prices, Beauties= [], []
        for price, best in items:
            # , since it is ascending, every max will be the max 
            # the logic if i can by i+1 i can by i 
            # so the max does't matter affecting max i to max i +1
            # if so the final chose is i 
            maximosis=max(maximosis,best)
            Beauties.append(maximosis)
            Prices.append(price)
        

        
        for i in range(len(queries)):
            h=0
            # find last occurence of 4 and get the max of all
            l, r=0, len(items)-1
            while(l<=r):
                mid=(l+r)//2
                if Prices[mid]>queries[i]:
                    r=mid-1
                else:
                    l=mid+1
            print(l-1, r)
            if r>=0 and Prices[l-1]<=queries[i]:
                for j in range(l):
                    h=max(h, Beauties[j])
            queries[i]=h
        return queries


        
