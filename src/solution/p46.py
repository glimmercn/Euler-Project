'''
Created on 2011-7-3

@author: huangkan
'''


p=[int(i.rstrip())for i in open('primes.txt')]
a=55
while True:
    a+=2
    while a in p:
        a+=2
    for i in range(1,int((a//2)**.5)+1):
        res=a-2*i**2
        if res in p:
            break
    else:break
    
print(a)
