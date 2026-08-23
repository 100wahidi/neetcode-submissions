class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str 
        :rtype: int
        """
        length = 0
        new_length = 0
        max_length = 0
        D={}
        for i in range(len(s)):
            if s[i] not in s[:i]:
               D[s[i]]=i
               length+=1
            else:
                if i-length<=D[s[i]]:
                    new_length = i-D[s[i]]
                    length = new_length  
                else:
                    length+=1
                D[s[i]]=i
            if length>max_length:
                max_length=length
        return max_length
            
           
 
