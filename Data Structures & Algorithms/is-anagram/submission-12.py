class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = max(len(s),len(t))
        h_map={}
        for i in range(n):
            if i<len(s):
                h_map[s[i]]=h_map.get(s[i],0)+1
            if i<len(t):
                h_map[t[i]]=h_map.get(t[i],0)-1

        for val in h_map.values():
            if val!=0:
               return False
            
        return True

         


            