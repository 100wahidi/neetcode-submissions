class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # representation for anagrams
        def WrodHashing(s:str)->str:
            code=[0]*26
            for l in s:
                code[abs(ord(l)-ord("a"))]+=1
            return str(code)
        Hash_table={}
        for word in strs:
            reps=WrodHashing(word)
            Hash_table[reps]=Hash_table.get(reps, [])+[word]

        return list(Hash_table.values())



        
        