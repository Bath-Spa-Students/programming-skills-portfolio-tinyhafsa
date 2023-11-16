''' Practice 4 - 
Write a Python program that uses the break statement to exit a for loop when a specific condition is met.'''

# Specify the condition to exit the loop
exit_number = 7
#using for loop to call numbers in a range
for number in range(1, 20):
    #print the numbers in the range
    print(number)
    #if the number matches the exit condition
    if number == exit_number:
        print("Loop terminated.")
        #loop is terminated
        break
