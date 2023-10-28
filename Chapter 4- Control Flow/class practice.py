#if statement practice

income = float(input("Total income of household:"))
scholarship = 0

if income < 30000 :
    scholarship = 2500
else: 
    scholarship = 200
print (f"You are eligible for {str(scholarship)} pound discount in your fees.")

#nested statement practice
household_income = int(input("\nWhat is the total income earned?"))
previous_grades = int(input("What was your most recent result in %?"))
scholarship = 0

if household_income <= 25000 :
    if previous_grades >=90 :
       print ("You are elegible for 5000 pund discount in your fees.")
    else :
        print ("You are not elegible for discount in your fees.")
else :
    print ("\nYou are not eligible for discount in your fees.")