class Solution
    def plusOne(self, digits List[int]) - List[int]
        e=len(digits)-1
        a=digits[0]
        for i in range(e)
            a=a*10+digits[i+1]
        a=a+1
        b=str(a)
        c=[]
        for i in range(len(b))
            c.append(int(b[i]))
        return c

# https://leetcode.com/problems/plus-one/
# easy