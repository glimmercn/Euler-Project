'''
Created on Jan 3, 2013

@author: kan
'''
def perfect(i):
    if int(i**.5)**2 == i:
        return True
    else:
        return False
n = 1000
path = [1 for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if perfect(i) and perfect(j) and perfect(i+j):
            path[j] = 0
        else:
            path[j] += path[j-1]
    path[j] %= 1000000007
print(path[n])