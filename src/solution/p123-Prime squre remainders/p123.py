'''
Created on Mar 28, 2013

@author: kan
'''
primes = [2, 3]
number = 3
exceed = False
while not exceed:
    number += 2
    isprime = True
    for p in primes:
        if number % p == 0:
            isprime = False
            break
        if p > number ** .5:
            break
    if isprime:
        primes.append(number)
        if len(primes) % 2 == 1 and 2 * len(primes) * number > 10 ** 10:
            exceed = True
            print(len(primes)) 
            