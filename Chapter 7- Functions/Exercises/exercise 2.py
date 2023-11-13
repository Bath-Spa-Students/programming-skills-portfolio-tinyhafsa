'''## Exercise 2: Favorite Book :ballot_box_with_check:
Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as One of my favorite books is Alice in Wonderland. 
Call the function, making sure to include a book title as an argument in the function call.'''

#defining function that takes one parameter
def favorite_book(title):
    #printing message when the function is called
    print(f"My favorite book is {title}.")

#calling the function to print the message with a book title
favorite_book("The Book Thief")
