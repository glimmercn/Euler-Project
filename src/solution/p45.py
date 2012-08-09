'''
Created on 2011-4-30

@author: huangkan
'''
import Mytools

i=144
while 1:
    o=Mytools.hexagonal(i)
    if Mytools.Ispentagon(o) and Mytools.Istriangle(o): 
        print(o)
        break
    i+=1
   