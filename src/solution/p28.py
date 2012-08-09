'''
Created on 2011-4-27

@author: huangkan
'''
sum=1
j=1
inc=0
for i in range(500):
    inc+=2
    for l in range(4):
        j+=inc
        sum+=j
print(sum)