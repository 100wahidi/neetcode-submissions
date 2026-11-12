class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # optimal
        items=sorted(items)
        for i in range(len(queries)):
            h=0
            # find last occurence of 4 and get the max of all
            l, r=0, len(items)-1
            while(l<=r):
                mid=(l+r)//2
                if items[mid][0]>queries[i]:
                    r=mid-1
                elif items[mid][0]<queries[i]:
                    l=mid+1
                else:
                    l=mid+1
            print(queries[i], r, l)

            if r>=0 and items[r][0]<=queries[i]:
                for j in range(r+1):
                    h=max(h, items[j][1])
            queries[i]=h
        return queries


        
