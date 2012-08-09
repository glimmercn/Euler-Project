'''
Created on May 25, 2012

@author: kan
'''
import math
max = 0
line = 0
i = 0
for l in open("99base_exp.txt"):
    i = i + 1
    a,b = l.rstrip().split(',')
    if int(b) * math.log(int(a)) > max :
        max = int(b) * math.log(int(a))
        line = i 
        
print(line) 
                               
    