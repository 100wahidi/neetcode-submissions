class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # optimal 
        # thelongest matching pattern that cound be used 
        # search it count it and substract it 
        i=0
        for e in s:
            if i<len(t) and e==t[i]:
               i+=1
        return len(t)-i
