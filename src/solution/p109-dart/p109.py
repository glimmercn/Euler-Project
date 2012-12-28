'''
Created on Dec 28, 2012

@author: kan
'''

def v(dart):
    a, b = dart
    return a * b
darts = []
dds = []
for i in range(1, 21):
    darts.append([1, i])
    darts.append([2, i])
    darts.append([3, i])
    dds.append([2, i])
darts.append([0, 0])
darts.append([1, 25])
darts.append([2, 25])
dds.append([2,25])

ans = 0
for i3 in range(len(dds)):
    for i1 in range(len(darts)):
        for i2 in range(i1, len(darts)): 
            if (v(darts[i1]) + v(darts[i2]) + v(dds[i3]) < 100):
                ans += 1
print(ans)                