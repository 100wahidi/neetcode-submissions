class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # 
        if len(s)<10:
            return []
        
        start=s[:10]
        Hash_table={start:1}
        for i in range(1,len(s)-10+1):
            start=s[i:i+10]
            Hash_table[start]=1+Hash_table.get(start, 0)
        for h, k in Hash_table.copy().items():
            if k<2:
                Hash_table.pop(h)


        return list(Hash_table.keys())


        
