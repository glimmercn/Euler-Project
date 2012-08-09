'''
Created on 2011-4-29

@author: huangkan
'''
d=[2,5,10,20,50,100,200]
l=[1]*201
for i in range(7):
    tl=[]
    for j in range(0,201):
        k=j
        sum=0
        
        while k>=0:
            sum+=l[k]
            k-=d[i]
        tl.append(sum)
    l=tl
    print(tl)
        