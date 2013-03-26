'''
Created on Jan 28, 2013

@author: kan
'''
import itertools
import src.solution.Mytools as Mt

def pr(n):
    
    sum = 0
    s = set(range(1, n+1))
    for i in range(1, ((n-1)>>1)+1):
        ''' the case that no red disc is picked will be added at last'''
        blue = itertools.combinations(s, i)
        for j in blue:
            p = 1
            for k in j:
                p *= k
            sum += p
    return sum + 1

print(Mt.factorial(16)/pr(15))
            