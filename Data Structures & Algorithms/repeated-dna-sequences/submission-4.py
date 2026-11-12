class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # optimal 
        repeated=set()
        seen=set()
        for i in range(9,len(s)):
            word=s[i-9:i+1]
            if word in seen:
                repeated.add(word)
            seen.add(word)
        return list(repeated)
