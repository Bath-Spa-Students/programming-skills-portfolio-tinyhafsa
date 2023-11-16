''' Practice 5 - 
Write a Python program that uses a while loop to find the largest number among a series of
user-input values until they enter '0' to exit the loop.'''

#creat the variable that will store the largest value
largest_number = None
#creating while loop that will continue until terminated
while True:
    #taking user input 
    user_input = input("Enter a number (enter '0' to exit): ")
    #if the number ended is 0
    if user_input == '0':
        #loop is terminated
        break

    #input is string - convert to number type
    number = float(user_input)

    #largest number variable is updated
    if largest_number is None or number > largest_number:
        largest_number = number

#result is printed when loop is terminated
if largest_number is not None:
    print("The largest number entered is:", largest_number)
else:
    print("No valid numbers entered.")

