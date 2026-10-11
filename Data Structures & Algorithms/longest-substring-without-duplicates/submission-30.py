class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str 
        :rtype: int
        """
        # bruthe force 
        h_map={}
        maxisio=0
        left=0
        for i in range(len(s)):
            if s[i] in h_map and h_map[s[i]]>left:
                left = h_map[s[i]]
            h_map[s[i]]=i+1
            maxisio=max(maxisio, i-left+1)
        return maxisio
            



            
           
 
