# Exercise 4: Deli

# Storing sandwich orders in a list
sandwich_orders = ["chicken", "cheese", "egg", "nutella", "ham", "turkey"]
# Making an empty list
finished_sandwiches = []

# Starting a loop to process sandwich orders
while sandwich_orders:
    # Pop a sandwich from the list
    sandwich = sandwich_orders.pop()
    # Print a statement for each finished sandwich
    print("Your", sandwich, "sandwich is ready.")
    # Append the finished sandwich to the list
    finished_sandwiches.append(sandwich)

# Print statements for each finished sandwich
for order in finished_sandwiches:
    print("I made a " + order + " sandwich.")
