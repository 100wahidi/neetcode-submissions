class Solution:
    def firstUniqChar(self, s: str) -> int:
        h_map={}
        for i in range(len(s)):
            if s[i] in h_map:
                h_map[s[i]][0]+=1
            else:
                h_map[s[i]]=[1,i]
        
        for l in h_map:
            if h_map[l][0]==1:
                return h_map[l][1]

        return -1

        