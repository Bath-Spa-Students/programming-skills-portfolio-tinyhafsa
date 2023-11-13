'''# Exercise 3: T-Shirt  :ballot_box_with_check:
Write a function called make_shirt() that accepts a size and the text of a message that should be printed 
on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.'''

#defining a function with two parameters
def make_shirt(size, message):
    #printing statement when function is called
    print(f"The shirt will be a {size} size and it will read the message: {message}")
#function called with positional arguments
make_shirt ("small", "Hitchhiker's Guide")
#function called with keyword arguments
make_shirt (size="large", message= "Good Omens")