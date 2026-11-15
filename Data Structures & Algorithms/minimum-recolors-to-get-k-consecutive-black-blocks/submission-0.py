class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        Ws=0
        Bs=0
        Min=100
        Left=0
        for i in range(len(blocks)):
            if i<=k-1:
                if blocks[i]=="W":
                    Ws+=1  
            else:
                if blocks[Left]=="W":
                    Ws-=1
                Left+=1
                if blocks[i]=="W":
                    Ws+=1
            if i>=k-1:
                Min=min(Min, Ws)

        return Min        
        