'''
Created on Jan 25, 2013

@author: kan
'''
def countstation(n):
    a = 2 % n
    print(a)
    b = a * 2 % n
    while a != b :
        print(b)
        b = b * 2 % n
        
def countstation2(factor, n):
    a = factor
    b = a * factor % n
    set = {a}
    while b not in set:
        set.add(b)
        b = b * factor % n
    return set

print(len(countstation2(3, 7**5)))