'''
Created on Jan 28, 2013

@author: kan
'''
import math
a = int(1000/math.sqrt(2))
while True:
    b = int(math.sqrt(2) * a)
    if 2 * a * (a-1) == b * (b-1):
        print(a)
        #break
    a += 1
