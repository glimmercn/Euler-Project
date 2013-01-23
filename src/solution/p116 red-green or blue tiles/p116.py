'''
Created on Jan 23, 2013

@author: kan
'''
def tiles(l, d):
    ts = []
    for i in range(l+1):
        if i < d :
            ts.append(0)
        else:
            ts.append(ts[i-1] + ts[i-d] + 1)
#    print(ts)
    return ts[-1]

print(tiles(50, 2) + tiles(50, 3) + tiles(50, 4))

def tiles(l, lens):
    ts = [1, 1]
    for i in range(2, l+1):
        sum = 0
        for d in lens:
            if i-d >= 0:
                sum += ts[i-d]
        ts.append(sum)
    print(ts)
    return ts[-1]

lens = [1, 2, 3, 4]
print(tiles(50, lens))
                