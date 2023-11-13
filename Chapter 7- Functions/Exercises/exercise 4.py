# Exercise 4:  Large Shirts

#defining a function with two parameters and default values
def make_shirt(size="large", message="I love Python"):
    #printing statement when function is called
    print(f"The shirt will be a {size} size and it will read the message: {message}")
#calling function to print default message and size
make_shirt()
#calling function to print default message and medium size
make_shirt(size="medium")
#calling function to print any message and any size
make_shirt(size="small", message="Hello, World!")