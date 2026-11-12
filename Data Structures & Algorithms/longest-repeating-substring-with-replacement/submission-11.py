class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Hash_map={}
        Left=0
        Length=0
        maxiso=0
        for i in range(len(s)):
            Hash_map[s[i]]=Hash_map.get(s[i], 0)+1
            # max frequency
            Length=max(Length, Hash_map[s[i]])
            # if replacement=length-freq 
            # shrink the substring
            while(Left<=i and (i-Left)+1-Length>k):
                # don't need to update Length
                # because we are loking for max
                #  and shrinking is for forther substrings
                # and Length already maximized before shrinking
                Hash_map[s[Left]]-=1
                Left+=1
            maxiso=max(maxiso, i-Left+1)
        return maxiso
            
            




            
        