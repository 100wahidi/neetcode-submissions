class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        H_map={}
        count=0
        Max=0
        L=0
        for i in range(len(fruits)):
            H_map[fruits[i]]=H_map.get(fruits[i], 0)+1
            while(L<=i and len(H_map)>2):
                H_map[fruits[L]]-=1
                if H_map[fruits[L]]==0:
                    H_map.pop(fruits[L])
                L+=1
            Max=max(Max, i-L+1)
        return Max

                


        