'''
Created on 2011-7-5

@author: huangkan
'''
'''
Created on May 2, 2011

@author: kan
'''
from itertools import combinations
from Mytools import primes_shelter
def result(li):
    s=''
    for i in li:
        s+=str(i)
    return int(s)
p=primes_shelter(1000000)
num=['0']*6
for i in combinations([0,1,2,3,4,5],3):
    [x,y,z]=[j for j in range(6) if j not in i]
    for a in range(10):
        for b in range(10):
            for c in range(10):
                count=0
                if 0 in i:
                    ran=range(1,10)
                else:ran=range(10)
                for k in ran:
                    for l in i:
                        num[l]=k
                    num[x]=a
                    num[y]=b
                    num[z]=c
                    if p[result(num)]:
                        count+=1
                if count>7:
                    print(num,x,y,z) 
