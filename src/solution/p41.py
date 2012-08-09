'''
Created on 2011-6-29

@author: huangkan
'''
import Mytools
max=0
s=set('1234567')

for a1 in set('137'):
    s1=s-{a1}
    for a2 in s1:
        s2=s1-{a2}
        for a3 in s2:
            s3=s2-{a3}
            for a4 in s3:
                s4=s3-{a4}
                for a5 in s4:
                    s5=s4-{a5}
                    for a6 in s5:
                        s6=s5-{a6}
                        for a7 in s6:
                            num=eval(a7+a6+a5+a4+a3+a2+a1)
                            if num>max and Mytools.Isprime(num):
                                max=num
print(max)
                                