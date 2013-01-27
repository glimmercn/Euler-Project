'''
Created on Jan 27, 2013

@author: kan

This method is too slow.
'''
import src.solution.Mytools as Mt
import math
i = 10
number = 614656
while i < 30 :
    number += 1
    l = Mt.num2list(number)
    x = 0
    for j in l:
        x += int(j)
    if x != 1:
        power = int(math.log(number) /math.log(x))
        if x**power == number or x**(power + 1) == number:
            i += 1
            print(number)