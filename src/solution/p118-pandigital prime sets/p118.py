'''
Created on Jan 26, 2013

@author: kan
'''
import src.solution.Mytools

def primelist(n):
    pl = [2]
    for i in range(3, n+1, 2):
        for p in pl:
            if i % p == 0:
                break
            else:
                if p > i**.5:
                    pl.append(i)
                    break
    return pl


plist = primelist(100000)
              