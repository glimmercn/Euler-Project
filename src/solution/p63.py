'''
Created on 2011-7-11

@author: huangkan
'''
import math
count=1
d=1
while True:
    if len(str(9**d))>=d:d+=1
    else:break
print(d)
for i in range(1,23):
    for j in range(1,10):
        if math.ceil(math.log10(j)*i)==i:count+=1

print(count)
        