class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a ={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        r = 0
        for i in range(len(s)-1):
            curr = a[s[i+1]]
            temp = a[s[i]]
            if curr>temp:
                r -= temp
            else:
                r += a[s[i]]
        
        return r+a[s[len(s)-1]]


        