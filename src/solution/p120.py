'''
Created on Dec 27, 2012

@author: kan
'''
def rmax(i):
    return (i-1)//2
s = 0
for i in range(3,1001):
    s = s + i * 2 * rmax(i)
print(s)

