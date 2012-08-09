'''
Created on 2011-4-27

@author: huangkan

'''
import math
import fractions
def Isprime(i):
    if abs(i)<2: return False
    bool=True;
    j=2
    while j<=math.sqrt(abs(i)):
        if i%j==0: return False
        j+=1
    return bool
def primes(t):
    t+=1
    p=list(range(2,t+1))
    i=0
    while i<len(p):
        a=p[i]
        b=2*a
        while b<=t:
            if b in p:p.remove(b)
            b+=a
        i+=1    
    return p
def primes_shelter(t):
    p=[1]*(t+1)
    p[0]=0
    p[1]=0
    for i in range(2,int(t**.5)+1):
        for j in range(i*2,t+1,i):
            p[j]=0
    return p
def primes2(t):
    if t<2: return []
    p=[2]
    for i in range(3,t+1):
        isprime=True
        j=0
        while p[j]<=math.sqrt(i)and j<len(p):
            if i%p[j]==0:isprime=False
            j+=1
        if isprime: p.append(i)
    return p
def penta(i):
    return int((3*i-1)*i/2)
def Ispentagon(x):
    a=int((1+math.sqrt(1+24*x))/6)
    b=a+1
    if penta(a)==x or penta(b)==x: return True
    return False
def tri(i):
    return int(i*(i+1)/2)
def Istriangle(x):
    if tri(int((-1+math.sqrt(1+8*x))/2))==x: return True
    return False        
##print(primes2(100000))
def hexagonal(i):
    return i*(2*i-1)
def Ishex(i):
    if hexagonal(int((1+math.sqrt(1+8*i))/4))==i: return True
    return False
def Is_tri_num(i):
    n=int((i*2)**.5)
    if n*(n+1)//2==i: 
        return True 
    else: return False 
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]
#p=[int(i.rstrip())for i in open('primes.txt')]
def classification(li):
    '''
    Get classification of list li,return a dictionary whose keys are different value of list.
    '''
    d={}
    for i in li:
        if i in d.keys():d[i]+=1
        else:d[i]=1
    return d
    
class PrimeOracle:
        # Takes a starting maximum to sieve to
    def __init__(self, startmax = 2000):
    # self.isprime[n] = True if 2n+1 is prime
        self.isprime = [True]*(startmax//2+1)
        self.isprime[0] = False
    # run the sieve
        for val in range(3, startmax + 1, 2):
            if(self.isprime[val // 2]):
                for mul in range(val*val, startmax + 1, 2*val):
                    self.isprime[mul // 2] = False
     
        # is n prime?
    def __getitem__(self, n):
        if n == 2:
            return True
        if n<2 or n % 2 == 0:
            return False
        nidx = n//2
        while(nidx >= len(self.isprime)):
            # extend the sieve
            # currently, we know the primality of 2*(len-1)+1=2*len-1
            # we can extend that to its square, 4*len^2 - 4len + 1
            # which would be index (4*len^2-4*len+1) // 2 = 4len(len-1)+1 // 2
            # so the new length should be one more than this
            # we already have length len, so we need to add (prev line) - len
            curlen = len(self.isprime)
            newlen = (4*curlen*(curlen-1) + 1) // 2
            self.isprime += [True for n in range(0, newlen+1-curlen)]
            maxknown = 2*curlen - 1
            maxtoknow = 2*newlen - 1
            for idx in range(1, curlen):
                if(self.isprime[idx]):
                    val = 2*idx + 1
                    # start crossing off multiples larger than maxknown
                    sfact = 1 + (maxknown // val)
                    if(sfact % 2 == 0):
                        sfact += 1 # otherwise our indexing is wrong
                    startfact = max(val, sfact)
                    for mul in range(startfact * val, maxtoknow + 1, 2*val):
                        self.isprime[mul // 2] = False
            return self.isprime[nidx]
 
    # the largest index we know about
    def __len__(self):
        return 2*len(self.isprime) - 1
 
    def __str__(self):
        return "\n".join(["%d: %s" % (2*n+1, self.isprime[n])
                        for n in range(0,len(self.isprime))])
def continued_fractions(D):

    a0 = int (D**0.5)
    if a0*a0 == D: return None
    gp = [0, a0]
    gq = [1, D-a0**2]
    a = [a0, int((a0+gp[1])/gq[1])]
    p = [a[0], a[0]*a[1]+1]
    q = [1, a[1]]
    maxdepth = None
    n = 1
    while True:
        if maxdepth is None and a[-1] == 2*a[0]:
            a.pop()
            return a
        n += 1
        gp.append (a[n-1]*gq[n-1]-gp[n-1])
        gq.append ((D-gp[n]**2)//gq[n-1])
        a.append (int ((a[0]+gp[n])//gq[n]))
        p.append (a[n]*p[n-1]+p[n-2])
        q.append (a[n]*q[n-1]+q[n-2])
def contif2frac(li):
    y=fractions.Fraction(li[-1],1)
    for i in range(len(li)-2,-1,-1):
        y=fractions.Fraction(li[i],1)+fractions.Fraction('1')/y
    return y
def mysqrt(n):
    e=n
    ne=(n/e+e)/2
    while abs(ne-e)>0.001:
        e=ne
        ne=(n/e+e)/2
    return ne

def gcd(a,b):
    if b>a: return gcd(b,a)
    if a%b==0: return b
    else: return gcd(b,a%b)
def int2(a,k):
    if a<0 or k>10:
        print('can\'t handle negative number or k>10.' )
        return None
    else:
        if a<k:
            return str(a)
        else:
            return int2(a//k,k)+str(a%k)

def mean(l):
    sum=0.0
    for i in l:
        sum+=i
    return sum/len(l)
def variance(l):
    s=0.0
    m=mean(l)
    for i in l:
        sum+=(i-m)^2
    return sum/len(l)