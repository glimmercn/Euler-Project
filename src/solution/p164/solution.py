'''
Created on Dec 24, 2013

@author: kan
'''

D = {}
for i in range(10):
    for j in range(10):
        if (i+j <= 9):
            D[str(i)+str(j)] = 1
        

for i in range(18):
    TempD = {}
    for k in D.keys():
        TempD[k] = 0
    for j in range(10):
        for k in D.keys():
            if (j+int(k[0])+int(k[1]) <= 9):
                TempD[str(j)+k[0]] += D[k]
    D = TempD

Sum = 0
for k in D.keys():
    if k[0] != '0': Sum += D[k] 

print(Sum)
        