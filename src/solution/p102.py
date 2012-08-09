'''
Created on Jun 1, 2012

@author: kan
'''
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Segment(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
def swap(a,b):
    c = a
    a = b
    b = c
def intersecty(p1,p2):
    return p1.y-p1.x*(p2.y-p1.y)/ float(p2.x-p1.x)
def orgin_if_in(p1,p2,p3):
    if p2.x > p1.x : p1,p2 = p2,p1
    if p3.x > p2.x : p2,p3 = p3,p2
    if p2.x > p1.x : p2,p1 = p1,p2
    if p1.x < 0 or p3.x > 0 : return False
    
    if p2.x > 0:
        if intersecty(p3, p2) * intersecty(p3, p1) > 0 : return False
    else:
        if intersecty(p2, p1) * intersecty(p3, p1) > 0 : return False
    return True
a = Point(-340,495)
b = Point(-153,-910)
c = Point(835, -947)
print(orgin_if_in(a,b,c))
X = Point(-175,41)
Y = Point(-421,-714)
Z = Point(574,-645)
print(orgin_if_in(X,Y,Z))
f = open('102triangles.txt')
count = 0
for l in f:
    n = [float(i) for i in l.rstrip().split(',')]
    p1 = Point(n[0],n[1])
    p2 = Point(n[2],n[3])
    p3 = Point(n[4],n[5])
    if orgin_if_in(p1,p2,p3): count = count + 1
print(count)
          
