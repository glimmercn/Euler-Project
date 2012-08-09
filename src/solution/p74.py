'''
Created on 2011-7-29

@author: huangkan
'''
import math
circle=[0]*1000000
f=[math.factorial(i) for i in range(10)]
def fac(n):
    sum=0
    for i in list(str(n)):
        sum+=f[int(i)]
    return sum

ans=0
for i in range(1,1000000):
    l=[i]
    j=i
    while fac(j) not in l:
        j=fac(j)
        if j<1000000 and circle[j]!=0:
            circle[i]=len(l)+circle[j]
            break
        else:        
            l.append(j)
    else:
        circle[i]=len(l)
for i in range(1,1000000):
    if circle[i]==60:ans+=1
print(ans)