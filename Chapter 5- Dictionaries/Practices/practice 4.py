''' Practice 4 - 
Write a Python program to iterate through both the keys and values of a dictionary and print them.'''

#creating a dictionary, storing book titles and authors
books = {"The Book Thief": "Markus Zusak",
         "Good Omens": "Neil Gaiman, Terry Prachet",
         "Hitchhiker's Guide to the Galaxy": "Douglas Adams",
         "The Dream Thieves": "Maggie Stiefvater"}
#iterating the keys and values in the dictionary
for title, author in books.items():
    #printing the items in the dictionary
    print(f"Book: {title} - Author: {author}.")
