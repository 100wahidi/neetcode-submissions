class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str 
        :rtype: int
        """
        length = 0
        max_length = 0
        D={}
        for i in range(len(s)):
            if s[i] not in D.keys():
               D[s[i]]=i
               length+=1
            else:
                if i-length<=D[s[i]]:
                    length = i-D[s[i]]  
                else:
                    length+=1
                D[s[i]]=i
            if length>max_length:
                max_length=length
        return max_length
            
           
 
