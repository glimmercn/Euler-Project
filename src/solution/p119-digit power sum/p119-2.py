'''
Created on Jan 27, 2013

@author: kan
'''
import src.solution.Mytools as Mt
import math

logs = [20000] * 500
for i in range(3, len(logs)):
    logs[i] = math.log(i)
    
clogs = list(logs)

power = [1] * 500
'''clogs is the list of log of power numbers'''

i = 0
while i < 37 :
    min_index = clogs.index(min(clogs))
    number = min_index**power[min_index]
    l = Mt.num2list(number)
    x = 0
    for j in l:
        x += int(j)
    if x == min_index:
        print(number)
        i += 1
    clogs[min_index] += logs[min_index]
    power[min_index] += 1
        