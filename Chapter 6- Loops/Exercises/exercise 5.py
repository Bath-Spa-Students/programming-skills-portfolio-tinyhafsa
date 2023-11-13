# Exercise 5: No Pastrami

# Storing sandwich orders in a list
sandwich_orders = ["chicken", "pastrami", "cheese", "pastrami", "egg", "nutella", "pastrami", "ham", "turkey"]
# Making an empty list
finished_sandwiches = []

# printing message telling the user of pastrami situation
print("The deli has run out of pastrami.")

# removing pastrami from list
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# starting a loop to print sandwich orders
while sandwich_orders:
    # popping sandwiches from the list
    sandwich = sandwich_orders.pop()
    # Print a statement for each finished sandwich
    print("Your", sandwich, "sandwich is ready.")
    # Append the finished sandwich to the list
    finished_sandwiches.append(sandwich)
print("\n ")
# Print statements for each finished sandwich
for order in finished_sandwiches:
    print("I made a " + order + " sandwich.")
