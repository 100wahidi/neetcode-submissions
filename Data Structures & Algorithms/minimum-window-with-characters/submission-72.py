class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ''
        h_window={}
        h_map={}
        for c in t:
            h_map[c]=h_map.get(c, 0)+1

        r, l=0, 0
        lenght=len(h_map)
        ctr=0
        maxiso=""
        while(r<len(s)):
            if s[r] in h_map:
                h_window[s[r]]=h_window.get(s[r],0)+1
                if h_map[s[r]]==h_window[s[r]]:
                    ctr+=1

            while(l<=r and ctr==lenght):
                if s[l] in h_map:
                    h_window[s[l]]-=1
                    if h_window[s[l]]<h_map[s[l]]:
                        ctr-=1
                if maxiso=="":  
                    maxiso=s[l:r+1]
                if len(maxiso)>len(s[l:r+1]):
                    maxiso=s[l:r+1]
                l+=1
            r+=1

        return maxiso

            
            




        