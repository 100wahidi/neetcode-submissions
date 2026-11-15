class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={"a", "e", "i", "o", "u"}
        Max=0
        L=0
        count=0
        for i in range(len(s)):
            if i<=k-1:
                if s[i] in vowels:
                    count+=1
            else:
                if s[i] in vowels:
                    count+=1
                if s[L] in vowels:
                    count-=1
                L+=1
            Max=max(Max, count)
        return Max



