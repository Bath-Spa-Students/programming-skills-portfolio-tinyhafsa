''' Practice 5 - 
Write a Python program that uses the elif statement to determine the season based on the
month provided as input.'''

#choosing a month
month = "September"
#assigning months to seasonal lists
winter = ["November", "December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]
autumn = ["September", "October"]
#if the month is in the winter list
if month in winter:
    print("It is the winter season.")
#if the month is in the spring list
elif month in spring:
    print("It is the spring season.")
#if the month is in the summer list
elif month in summer:
    print("It is the summer season.")
#if the month is in the autumn list
elif month in autumn:
    print("It is the autumn season.")
#if the month is not in any of the lists
else:
    print("Month not recognized.")
