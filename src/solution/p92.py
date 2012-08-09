'''
Created on 2011-9-30

@author: huangkan
'''
f=[0]*568
f[1]=1
f[89]=89
def next(i):
    sum=0
    for j in str(i):
        sum+=int(j)*int(j)
    return sum
def getfinal(i):
    if f[i]: return f[i]
    else:
        f[i]=getfinal(next(i))
        return f[i]
for i in range(1,568):
    if not f[i]: getfinal(i)
ans=f.count(89)
for i in range(569,10000001):
    if f[next(i)]==89:ans+=1
print(ans)