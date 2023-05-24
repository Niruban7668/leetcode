class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip() 
        if not s:
            return 0
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1    
        result *= sign
        result = max(-2**31, min(result, 2**31 - 1))
        
        return result
    
#https://leetcode.com/problems/string-to-integer-atoi/
#medium
