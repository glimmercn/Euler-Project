"""Compute solutions to the diophantine Pell equation x^2-D*y^2=1."""

import itertools

def pell (D):
    """Return the smallest integer set solving Pell equation
    x^2-D*y^2=1 where x, D and y are positive integers. If there are no
    solution (D is a square), return None.

    >>> pell(3)
    (2, 1)"""
    a0 = int (D**0.5)
    if a0*a0 == D: return None
    gp = [0, a0]
    gq = [1, D-a0**2]
    a = [a0, int((a0+gp[1])/gq[1])]
    p = [a[0], a[0]*a[1]+1]
    q = [1, a[1]]
    maxdepth = None
    n = 1
    while maxdepth is None or n < maxdepth:
        if maxdepth is None and a[-1] == 2*a[0]:
            r = n-1
            if r % 2 == 1: return p[r], q[r]
            maxdepth = 2*r+1
        n += 1
        gp.append (a[n-1]*gq[n-1]-gp[n-1])
        gq.append ((D-gp[n]**2)//gq[n-1])
        a.append (int ((a[0]+gp[n])//gq[n]))
        p.append (a[n]*p[n-1]+p[n-2])
        q.append (a[n]*q[n-1]+q[n-2])
    return p[2*r+1], q[2*r+1]

def gen_pell (D):
    """Return the first solutions to Pell equation x^2-D*y^2=1 where x,
    D and y are positive integers. Computation of solution couples is
    done in floating point. As soon as the precision is not high enough,
    the generator stops. All the solutions the caller receives are correct.

    >>> for (x, y) in gen_pell(1053): print (x, y)
    ...
    (649, 20)
    (842401, 25960)
    (1093435849, 33696060)
    (1419278889601L, 43737459920L)"""
    r = pell (D)
    if not r: return
    p, q = r
    sd = D**0.5
    qd = q * sd
    sd2 = 2*sd
    lm = p + qd
    rm = p - qd
    for n in itertools.count (1):
        lmn = lm**n
        rmn = rm**n
        x, y = int ((lmn+rmn)/2+0.5), int ((lmn-rmn)/sd2+0.5)
        if x**2-D*y**2 != 1: return
        yield x, y
print(pell(14))