class Solution:
    def isPalindrome(self, s: str) -> bool:
        case = ""
        case0 =""
        sens = {'?',' ',',',"'",'/','.',':',';','!'}
        low = s.lower()
        for i in range(len(low)):
            if low[i] not in sens:
                case0+=low[i]
            if low[len(s)-1-i] not in sens:
                case+=low[len(s)-1-i]
        print(case0," ",case)
        return case0==case

        