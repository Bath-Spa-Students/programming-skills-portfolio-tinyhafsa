# Exercise 2: Glossary

#storing words and meanings as keys and values in a dictionary
glossary = {"print" : "display." , #1
            "variable" : "container for storing data values." , #2
            "string" : "piece of text surrounded by quotations." , #3
            "concatenation" : "using + operator to join strings together." , #4
            "Boolean" : "data type with only two values (True and False)." #5
            } 

word1 = "print" #decalring key as variable and printing word and meaning
print (f"{word1}: {glossary[word1]}")
word2 = "variable" #decalring key as variable and printing word and meaning
print (f"\n{word2}: {glossary[word2]}")
word3 = "string" #decalring key as variable and printing word and meaning
print (f"\n{word3}: {glossary[word3]}")
word4 = "concatenation" #decalring key as variable and printing word and meaning
print (f"\n{word4}: {glossary[word4]}")
word5 = "Boolean" #decalring key as variable and printing word and meaning
print (f"\n{word5}: {glossary[word5]}")