#1
import math
degree = float(input("Input degrees: "))
radian = degree*(math.pi/180)
print("Radian: ",radian)

#2
import math
h= int(input("Height: "))
b_1=int(input("b1: "))
b_2=float(input("b2: "))
area = ((b_1 + b_2) / 2) * h
print("The area of a trapezoid: ",area)

#3
from math import tan, pi
n_side=int(input("Number of sides: "))
l_length=float(input("The length of a side: "))
area=n_side*(l_length**2)/(4*tan(pi/n_side))
print("The area of the polygon is: ",area)

#4
import math
l_length=float(input("Length of base: "))
h_height=float(input("Height of parallelogram: "))
area=l_length*h_height
print("The area of a parallelogram: ",area)

