'''
Created on Dec 28, 2012

@author: kan
'''
for i in range(20000, 1000000):
    ans = 0
    for j in range(i + 1, i * 2 + 1):
        if i * j % (j - i) == 0 :
            ans += 1
    if ans > 1000: break
print(i)
