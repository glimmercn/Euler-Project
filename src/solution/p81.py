'''
Created on 2011-8-2

@author: huangkan
'''
f=open('matrix.txt')

l=f.readline()
ans=[int(j) for j in list(l.rstrip().split(','))]
for i in range(1,80):
    ans[i]=ans[i]+ans[i-1]
for l in f:
    n=[int(j) for j in list(l.rstrip().split(','))]
    ans[0]+=n[0]
    for i in range(1,80):
        ans[i]=n[i]+min([ans[i-1],ans[i]])
print(ans[-1])