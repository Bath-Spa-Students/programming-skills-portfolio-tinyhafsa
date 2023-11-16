''' Practice 3 - 
Write a Python program that uses a function to check if a given number is prime or not.'''

#defining a function with one parameter
def prime(number):
    #check for factors of the number from 2 to square root
    for i in range(2, int(number**0.5) + 1):
        #checking if the number is prime or not
        if number % i == 0:
            #is number is divisible, it is not prime
            return False 
    #if number is not visible, it is prime
    return True 

#taking input from user
num = int(input("Enter a number: "))

#printing the result
if prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
