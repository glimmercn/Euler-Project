'''
Created on 2011-7-4

@author: huangkan
'''
Limit=1000000
def Ispenta(i):
    if i<Limit:
        return f[i]
    else:
        a=int((1+(1+24*i)**.5)/6)
        b=a+1
        if penta(a)==i or penta(b)==i: return 1
        else:
            return 0
def penta(i):
    return (3*i-1)*i//2
f=[0]*Limit
for i in range(1,259):
    f[penta(i)]=1
j=2
found=False

while not found:
    for i in range(1,j):
        a=penta(i)+penta(j)
        b=penta(i)+2*penta(j)
        if Ispenta(a) and Ispenta(b):
            found=True
            print(penta(i))
            break
    j+=1
