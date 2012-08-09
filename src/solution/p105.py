'''
Created on Jun 27, 2012

@author: kan
'''
import itertools

def IsSpecialSum(l):
    for nb in range(1, len(l)):
        for B in itertools.combinations(l, nb):
            A = l.difference(B)
            for nc in range(1,len(A)+1):
                for C in itertools.combinations(A, nc):
#                    print(B)
#                    print(C)
#                    print(str(sum(B))+ ' ' + str(sum(C)))
                    if sum(B) == sum(C) or (nb - nc) * (sum(B) - sum(C)) < 0:
                        return False
    return True
f = open('105sets.txt')
specialsum = 0
#s = set([13, 17, 20, 22, 23, 24])
#print(IsSpecialSum(s))
#print(sum(s))
for l in f:
    s = set([int(i) for i in l.rstrip().split(',')])
    if IsSpecialSum(s): specialsum = specialsum + sum(s)

print(specialsum)