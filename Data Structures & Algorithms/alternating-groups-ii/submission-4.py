class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        count=0
        M=0
        for i in range(1,len(colors)+k-1):
            if i>=k:
                if colors[i-k+1]!=colors[i-k]:
                    count-=1
            if colors[i%len(colors)]!=colors[(i-1)%len(colors)]:
                count+=1
            if count==k-1:
                M+=1
        return M

            
            

