'''
Created on 2013-3-27

@author: kan
'''
l = [1]
s = [l]
idx = 0
reach200 = False
while not reach200:
    for i in range(len(s[idx])):
        for j in range(i, len(s[idx])):
            if s[idx][i] + s[idx][j] > s[idx][-1]:
                new = s[idx][i] + s[idx][j]
                s.append(s[idx] + [new])
                if new == 200:
                    reach200 = True
    idx += 1