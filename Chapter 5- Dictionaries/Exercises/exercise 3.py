# Exercise 3: Glossary 2

#storing 10 programming words and meanings in a dictionary
glossary = {"print" : "display" , #1
            "variable" : "container for storing data values" , #2
            "string" : "piece of text surrounded by quotations" , #3
            "concatenation" : "using + operator to join strings together" , #4
            "Boolean" : "data type with only two values (True and False)" , #5
            "int" : "data type for number, converts number to integar" , #6
            "float" : "data type for number, converts number to decimal" , #7
            "list" : "store multiple values of different types in one variable" , #8 
            "and" : "logical operation, results in True only if both inputs are true at the same time" , #9 
            "or" : "logical operator, results in True if atleast one of the inputs is true"  #10
            }

#using for loop to display word and their meanings
for word, meaning in glossary.items():
    print(f"{word}: {meaning}.\n")