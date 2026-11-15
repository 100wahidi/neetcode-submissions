class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        H_mp={0:0}
        for i in range(1, len(colors)):
            if colors[i-1]!=colors[i]:
                H_mp[i]=H_mp.get(i-1, 0)+1
            else:
                H_mp[i]=H_mp.get(i-1, 0)
        
        count=0
        Sec=0
        for i in range(len(colors)):
            if i<=len(colors)-k:
                if H_mp[i+k-1]-H_mp[i]==k-1:
                    Sec+=1
            else:
                count=0
                if colors[-1]!=colors[0]:
                    count=1
                pairs=H_mp[len(colors)-1]-H_mp[i]+count+H_mp[k-(len(colors)-i)-1]
                if pairs==k-1:
                    Sec+=1
        return Sec

            
        
