'''
Created on 2013-3-27

@author: kan
'''
import numpy as np

import numpy as np
l = [1]
s = [l]
idx = 0
reach200 = False
expons = np.zeros(201)
expons[0:2] = 1
dic = set()
while not np.all(expons):
    for i in range(len(s[idx])):
        for j in range(i, len(s[idx])):
            if 201 > s[idx][i] + s[idx][j] > s[idx][-1] :
                new = s[idx][i] + s[idx][j]
                p1 = s[idx] + [new]
                if str(p1) not in dic:
                    s.append(p1)
                    dic.add(str(p1))
                    if expons[new] == 0:
                        expons[new] = len(p1) - 1
    idx += 1
print(np.sum(expons))