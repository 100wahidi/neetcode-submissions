class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map={}
        Length=0
        ct=0
        start=0
        if len(s)==1:
            return 1
        for i, e in enumerate(s):
            if e not in hash_map:
                ct+=1
            else:
                start=max(start, hash_map[e])
                ct=i-start
            Length=max(Length, ct)
            hash_map[e]=i
        
        return Length
        