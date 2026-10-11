class Solution:
    def isValid(self, s: str) -> bool:
        h_map={"[":"]","{":"}","(":")"}
        stack =[]
        for c in s:
            print(stack)
            
            if c in h_map.keys():
                stack.append(c)
            else:
                
                if stack and h_map[stack[-1]]==c:
                    stack.pop()
                else:
                    return False
        
        return len(stack)==0

        