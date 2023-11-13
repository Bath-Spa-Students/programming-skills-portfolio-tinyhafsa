''' Practice 2 - 
Write a python program that takes courses marks as input and then calculates average of all the courses. 
After calculating the average, calculate the percentage of a student using total marks. 
Assume the total of all the courses marks is 500 or take the total marks from the user as input.'''

#taking input of course marks from user
math = int(input("Math marks:"))
english = int(input("English marks:"))
science = int(input("Science marks:"))
language= int(input("Spanish marks:"))
art= int(input("Art marks:"))
#taking input of total course marks from user
total= int(input("Total course marks:"))
#taking sum of marks achieved
marks_achieved = math+english+science+language+art
#calculating average as an integar
average = int(marks_achieved//5)
#calculating percentage as an integar
percentage = int((marks_achieved/total)*100)
#printing average
print (f"\nThe average is {average}.")
#printing percentage
print (f"The total percentage is {percentage}%.")