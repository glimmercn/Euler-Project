'''
Created on 2011-7-30

@author: huangkan
'''
l=[1]*101
for i in range(2,100):
    tl=l[:]
    for j in range(1,int(100/i)+1):
        for k in range(101):
            if k+i*j<101:
                l[k+i*j]+=tl[k]
            else:
                break
print(l[100])           