# Exercise 1: Pizza Toppings

#starting an infinite loop 
while True: 
    #asking user for input and storing it in toppings value
    toppings = input("Enter your pizza toppings. Enter 'quit' when you are done: ") 
    #break statement to terminate the loop when 'quit' value is entered
    if toppings.lower() == "quit": #quit is converted to lowercase
        break 
    #message confirming topping added to pizza when a value other than quit is entered
    #topping is capitalized
    print(toppings.title() + " will be added to your pizza.") 