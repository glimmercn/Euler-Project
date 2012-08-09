'''
Created on Jun 1, 2012

@author: kan
'''

def ad(a):
    a[1] = 5
a = [1, 1]
ad(a)
print(a)

def de(a):
    a = a - 1
    return a
a = 4
a = de(a)
print(a)
def swap(a,b):
    return b,a
a = [1,2]
x = 5
a,x = swap(a,x)
print(x)