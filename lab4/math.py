#1
import math
def degree_to_radian(d):
    return d * (math.pi/180)
d=int(input("Degree: "))
print(degree_to_radian(d))

#2
import math
def area(a,b,h):
    return (a+b)/2 * h
h=int(input("Height: "))
a=int(input("Base, first value: "))
b=int(input("Base, second value: "))
print(area(a,b,h))

#3
from math import tan,pi
def area(s,l):
    return s * (l**2) / (4*tan(pi/s))
s=int(input("Input number of sides: "))
l=int(input("Input the length of a side: "))
print(area(s,l))

#4
import math
def area(a,h):
    return a * h
a=int(input("Length of base: "))
h=int(input("Height of parallelogram: "))
print(area(a,h))