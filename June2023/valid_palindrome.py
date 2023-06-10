class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower1=s.lower()
        lower_list=list(lower1)
        string1=[]
        string2=[]
        for i in lower_list:
            if i.isalnum()==True:
               string1.append(i)
        for i in reversed(string1):
            string2.append(i)
        if string1==string2:
           return True
        return False

#https://leetcode.com/problems/valid-palindrome/description/
#easy