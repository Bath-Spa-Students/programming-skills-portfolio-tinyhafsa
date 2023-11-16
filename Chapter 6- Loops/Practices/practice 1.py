''' Practice 1 - 
Write a Python program that uses a while loop to print the even numbers from 2 to 10.'''

#first even number 
num = 2

#using while loop to iterate from 2 to 10
while num <= 10:
    #if number is even
    if num % 2 == 0:
        #number is printed
        print(num)
    #moving to the next iteration
    num += 2
