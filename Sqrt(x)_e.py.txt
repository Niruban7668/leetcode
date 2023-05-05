class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        if(x==1):
            return x
        while(i<=(x/2)):
            a=i*i
            if(a==x):
                return i
            elif(a>x):
                return (i-1)
            i=i+1
        return (i-1)




#https://leetcode.com/problems/sqrtx/description/
#easy