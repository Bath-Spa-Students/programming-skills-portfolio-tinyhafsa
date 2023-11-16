''' Practice 4 - 
Write a Python program that defines a function to calculate the area of a circle, and then
calls that function with a given radius'''

def area_of_circle (radius):
    area= 3.14 * radius * radius
    return area

radius = float(input("Enter the radius: "))
area = area_of_circle(radius)

print (f"The area of a circle with radius {radius} is {area}.")
