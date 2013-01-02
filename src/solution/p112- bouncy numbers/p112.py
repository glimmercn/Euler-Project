'''
Created on Jan 2, 2013

@author: kan
'''
import copy
percentage = 0
number = 0
bouncy = 0

while percentage < 0.99:
    number += 1
    a = list(str(number))
    b = sorted(a)
    b.reverse()
    if sorted(a) != a and b != a:
        bouncy += 1
    percentage = bouncy/number

print(number)