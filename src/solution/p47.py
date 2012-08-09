'''
Created on 2011-7-3

@author: huangkan
'''
#from Mytools import factors
def factors(i):
    if i<=0: return 'give a positive number'
    if i in p: return []
    r=[]
    l=0
    while i>1:
        
        if i%p[l]==0:
            r.append(p[l])
            while i%p[l]==0:
                i//=p[l]
        l+=1
    return r
p=[int(i.rstrip())for i in open('primes.txt')]
counter=0
n=647
while True:

    if len(factors(n))>3: 
        counter+=1
    else:
        counter=0
    if counter==4: break
    n+=1
print(n-3)