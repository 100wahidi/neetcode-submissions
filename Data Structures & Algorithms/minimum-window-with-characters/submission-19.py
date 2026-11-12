class Solution:
    def minWindow(self, s: str, t: str) -> str:
        H, G={}, {}
        if len(t)>len(s) or t=="":
            return ""
        for i in range(len(t)):
            H[t[i]]=H.get(t[i], 0)+1
        res=[]
        count=0
        Length=float("infinity")
        Left=0
        solution=""
        low,high=0,0
        for j in range(len(s)):
            if s[j] in H:
                G[s[j]]=G.get(s[j], 0)+1
                if G[s[j]]==H[s[j]]:
                    count+=1
            while(Left<=j and count==len(H)):
                if count==len(H) and j-Left<=Length:
                    Length=j-Left
                    low, high=Left, j+1
                if s[Left] in H:
                    G[s[Left]]=G.get(s[Left], 0)-1
                    if G[s[Left]]<H[s[Left]]:
                        count-=1
                Left+=1

        return s[low :high]

