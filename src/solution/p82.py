'''
Created on 2011-8-3

@author: huangkan
'''
mtx=[]
for i in open('matrix82.txt'):
    n=[int(j) for j in list(i.rstrip().split(','))]
    mtx.append(n)
ans=[l[0] for l in mtx]
for i in range(79):
    n=[l[i+1] for l in mtx]
    temp=ans[:]
    for j in range(80):
        m=[]
        for j1 in range(0,j):
            a=temp[j1]
            for k in range(j1,j):
                a+=n[k]
            m.append(a)
        m.append(temp[j])
        for j2 in range(j+1,80):
            a=temp[j2]
            for k in range(j+1,j2+1):
                a+=n[k]
            m.append(a)
        ans[j]=n[j]+min(m)
print(min(ans))