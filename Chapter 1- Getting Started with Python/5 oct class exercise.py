#take profile input from user

name= input ("What is your name?")
age = int (input ("How old are you?"))
date_of_birth = int (input("What year were you born in?"))
city_of_residence = input ("What city do you live in?")

family_members = int (input ("How many people are there in your family?"))
name_of_father = input ("What is your father's name?")
pets = input ("Do you have any pets?")

hobbies = input ("What do you do for fun?")
university = input ("Where do you study?")
subject = input ("What do you study?")

print ("PERSONAL" , "\nName:" , name , "\nAge:" , age , "\nYear of birth:" , date_of_birth) 
print ("ADDRESS" , "\nCity: " , city_of_residence)
print ("FAMILY" , "\nMembers:" , family_members , "\nFather's name:" , name_of_father , "\nPets:" , pets)
print ("EDUCATION" , "\nHobbies:" , hobbies , "\nUniversity:" , university , "\nSubject:" , subject)