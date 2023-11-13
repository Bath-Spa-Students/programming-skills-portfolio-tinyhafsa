# Exercise 2: Movie Tickets:

#starting a while loop
while True:
    age = input("Enter your age: ") #asking user to enter their age
    #break statement that will terminate the loop if "quit" value is entered
    if age.lower() == "quit": #making quit value case insensitive
        break
    age = int(age)    # Convert the input to an integer
    if age < 3: #if the age is less than three 
        print("The ticket is free.")
    elif 3 <= age <= 12: #if the age is between 3 and 12
        print("The ticket is $10.")
    else: #if the age is more than 12
        print("The ticket is $15.")