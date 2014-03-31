'''
Created on Mar 31, 2014

@author: kan
'''

import src.solution.Mytools as Mt
N = 100000
primes = Mt.primes2(N)

def compute_r(n):
    if n==0 or n==1:
        return n    
    rad = 1
    for p in primes:
        if n%p == 0:
            rad *= p
            n//=p
            while n % p == 0:
                n //= p
        if n==1:
            return rad
        
class radical:
    def __init__(self, n):
        self.n = n
        self.r = compute_r(n)
    def __lt__(self, rad2):
        return self.r < rad2.r or self.r==rad2.r and self.n < rad2.n
        
class ordered_radicals:
    def __init__(self, N):
        self.N = N
        self.rs = [None for i in range(self.N+1)]
        return None
    
    def solve(self):
        for i in range(self.N+1):
            self.rs[i] = radical(i)
        #self.rs = sorted(self.rs)
        self.rs.sort()
        
sol = ordered_radicals(N)
sol.solve()
print(sol.rs[10000].n)
    
