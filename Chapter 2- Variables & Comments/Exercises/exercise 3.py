#Exercise 3: Stripping Names 

#name variable with whitespace characters
name = ("    \n\tSyeda Hafsa  \t ")

#variable printed without stripping
print (f"My name is {name}." )
#variable printed with left stripping
print (f"My name is {name.lstrip()}.")
#variable printed with right stripping
print (f"My name is {name.rstrip()}.")
#variable printed with all stripping
print (f"My name is {name.strip()}.")