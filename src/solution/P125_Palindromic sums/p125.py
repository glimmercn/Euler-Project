'''
Created on Mar 31, 2014

@author: kan

make sure that all numbers added are unique
'''


import src.solution.Mytools as Mt
n = 10001
bound = 10**8
def f(n):
    return n*(n+1)*(2*n+1)//6

squre_sums = [f(i) for i in range(n)]

nset = set()
ans = 0
for i in range(2, n):
    for j in range(i-1):
        s = squre_sums[i] - squre_sums[j]
        if s<bound and Mt.isPalindromic(str(s)):
            nset.add(s)
            
print(sum(nset))