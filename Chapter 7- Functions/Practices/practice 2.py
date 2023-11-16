''' Practice 2 - 
Write a Python function that calculates the factorial of a given positive integer using recursion.'''

#defining a function 'factorial' with one parameter
def factorial(number):
    #defining badse case using 0
    if number == 0:
        return 1
    #defining recursive case using n! = n * (n-1)!
    else:
        return number * factorial(number - 1)

#ask user for input of positive integar
integar = int(input("Enter a positive integer: "))
#calculate result
result = factorial(integar)
#print result 
print(f"The factorial of {integar} is: {result}")

    
