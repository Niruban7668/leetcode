class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=0
        m=0
        j=0
        k=0
        for i in reversed(range(0,len(a))):
            if int(a[i])==1:
                n=n+2**j
            j=j+1
        for i in reversed(range(0,len(b))):
            if int(b[i])==1:
                m=m+2**k
            k=k+1
        e=n+m
        f=[]
        q=-1
        while(e>1):
            f.insert(q,e%2)
            e=e//2
            q=q-1
        f.insert(q,e)
        o=0
        for i in range(len(f)):
            o=f[i]+(o*10)
        return str(o)

# https://leetcode.com/problems/add-binary
# easy