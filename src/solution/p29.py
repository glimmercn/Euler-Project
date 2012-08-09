'''
Created on 2011-4-28

@author: huangkan
'''
import Mytools
a=list(range(2,101))
sum=0
while a!=[]:
    i=a[0]
    b=i
    tset=set()
    p=1
    while i<=100:
        a.remove(i)
        for k in range(2,101):
            tset.add(k*p)
        i*=b
        p+=1
    sum+=len(tset)
print(sum)
    
            

