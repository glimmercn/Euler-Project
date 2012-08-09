'''
Created on 2011-7-28

@author: huangkan
'''
ans=1
temp=0
for i in range(4,1000000):
    k=int(3*i/7)-1
    while (k+1)/i<3/7:
        k=k+1
    if k/i>temp:
        temp=k/i
        ans=k
print(ans)
        