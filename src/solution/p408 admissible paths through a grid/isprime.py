'''
Created on Jan 3, 2013

@author: kan
'''
Isprime = True
n = 1000000007
for i in range(2, int(n**.5)):
    if n % i == 0 :
        Isprime = False
        break
print(Isprime)