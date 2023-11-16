''' Practice 3 - 
Write a Python program that uses a loop to find the sum of all the numbers from 1 to 100.'''

#variable to store sume of numbers
sum = 0
#using for loop to call numbers in the range
for number in range(1, 101):
    #adding the numbers as they are called
    sum += number
#printing the sum of numbers when the loop is over
print("Sum of numbers from 1 to 100:", sum)
