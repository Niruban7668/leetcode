class Solution:
    def isValid(self, s: str) -> bool:
        bool1=False
        list1=list(s)
        a=[]
        b=[]
        c=[]
        d=[] 
        e=[]
        f=[]
        maximum=[]
        minimum=[]
        for i in range(len(list1)):
            if list1[i]=='(':
               a.append(i)
            elif list1[i]=='{':
               b.append(i)
            elif list1[i]=='[':
               c.append(i)
            elif list1[i]==')':
               d.append(i)
            elif list1[i]=='}':
               e.append(i)
            else:
               f.append(i) 
        if len(a)==len(d) and len(b)==len(e) and len(c)==len(f):
            if len(a)!=0: 
                if min(d)<min(a):
                   return False
                else:
                    for i,j in zip(reversed(a), d):
                        if i>j:
                           return False
                        else:
                            if max(a)+1!=min(d): 
                                if max(a)>min(d):
                                    return False
                                else:
                                    maximum.append(max(a))
                                    minimum.append(min(d))
            if len(a)==0 or (all(element % 2 == 0 for element in a)!=all(element % 2 == 0 for element in d)):
                bool1=True
            else:
                return False        
            if len(b)!=0: 
                if min(e)<min(b):
                   return False
                else:
                    for i,j in zip(reversed(b), e):
                        if i>j:
                           return False
                        else:
                            if max(b)+1!=min(e): 
                                if max(b)>min(e):
                                    return False
                                else:
                                    maximum.append(max(b))
                                    minimum.append(min(e))
            if len(b)==0 or (all(element % 2 == 0 for element in b)!=all(element % 2 == 0 for element in e)):  
                bool1=True
            else:
                return False
            if len(c)!=0: 
                if min(f)<min(c):
                   return False
                else:
                    for i,j in zip(reversed(c), f):
                        if i>j:
                           return False
                        else:
                            if max(c)+1!=min(f):
                                if max(c)>min(f):
                                    return False
                                else:
                                    maximum.append(max(c))
                                    minimum.append(min(f))
            if len(c)==0 or (all(element % 2 == 0 for element in c)!=all(element % 2 == 0 for element in f)):
                bool1=True
            else:
                return False
        else:
            return False
        if len(maximum)!=0 and len(minimum)!=0:
            if ((maximum.index(max(maximum))))!=(minimum.index(min(minimum))):
                return False
        return bool1

#lesson learned