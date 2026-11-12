class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map={}
        Length=0
        start=-1
        for i, e in enumerate(s):
            if e in hash_map:
                start=max(start, hash_map[e])
            Length=max(Length, i-start)
            hash_map[e]=i
        
        return Length
        