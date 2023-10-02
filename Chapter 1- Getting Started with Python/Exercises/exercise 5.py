'''Exercise 5: Compute area of Circle
Write a Python program which accepts the radius of a circle from the user and compute the area.'''

import math

radius = int (input ("Enter radius= "))
area = radius * radius * math.pi

print ("Area of circle =", area)