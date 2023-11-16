#Exercise 3: T-Shirt

#defining a function with two parameters
def make_shirt(size, message):
    #printing statement when function is called
    print(f"The shirt will be a {size} size and it will read the message: {message}")
#function called with positional arguments
make_shirt ("small", "Hitchhiker's Guide")
#function called with keyword arguments
make_shirt (size="large", message= "Good Omens")