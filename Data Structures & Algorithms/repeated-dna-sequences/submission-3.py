class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        
        start=s[:10]
        Hash_table={start:1}
        for i in range(1,len(s)-10+1):
            start=s[i:i+10]
            Hash_table[start]=1+Hash_table.get(start, 0)

        return [code for code, k in Hash_table.items() if k>=2]


        
