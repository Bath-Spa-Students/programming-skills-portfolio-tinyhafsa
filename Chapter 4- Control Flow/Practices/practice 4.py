''' Practice 4 - 
Write a python program with an if-else statement that displays Speed is normal if the speed
variable is within the range of 24 to 56. 
If the speed variable's value is outside this range, display 'Speed is abnormal'''

#assigning value to speed
speed = 76
#if speed is within rage to 24 to 56
if speed > 24 and speed < 56:
    #printing statement
    print ("Speed is normal.")
#if speed is out of range
else:
    #printing statement
    print ("Speed is abmnormal.")