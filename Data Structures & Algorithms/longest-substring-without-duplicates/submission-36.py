class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # to count refere to every leter by position
        # if a letter is seen the next counting start from the last seen position+1 
        h_map={}
        # to count distinct letters with max function
        max_sbs=0
        l=0
        for i in range(len(s)):
            if s[i] in h_map:
                l=max(h_map[s[i]]+1, l)
            h_map[s[i]]=i
            max_sbs=max(max_sbs,i-l+1)

        return max_sbs



        