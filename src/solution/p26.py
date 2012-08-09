'''
Created on 2011-4-26

@author: huangkan
'''
def min10(i):
    ##ii=i
    while i%2==0:
        i/=2
    while i%5==0:
        i/=5
    if i==1:return 0
    ##i=ii
    f=False
    a=10
    b=1
    i=int(i)
    while not f:
        if (a-1)%i==0:
            f=True
        a*=10
        b+=1
    return b

max=1
objective=1
for i in range(1,1001):
    if min10(i)>max: 
        max=min10(i)
        objective=i
print(objective)
