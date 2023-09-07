# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".

#name= input("What is your name")

#if name == "Bob":
#print("Welcome Bob")

# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".

#name= input("What is your name")

#if name == "Alice":
#print("Welcome Alice")
#else:
#print("You are not Alice")

# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in".
#   If they get it wrong, print "Password failure".

#userinput = input("What is your password\n")
#password = "qwerty123"

#if userinput == password:
#print("You have successfully logged in")
#else:
#print("Password failure")

# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".

#userinput = int(input("Enter a number"))

#if userinput % 2 == 0:
#print("Even")
#else:
#print("Odd")

# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"

#userinput1 = int(input("Enter a number"))
#userinput2 = int(input("Enter a number"))

#if userinput1 + userinput2 > 21:
#print("Bust")
#else:
#print("Safe")

# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.

#length = int(input("Enter a number"))
#width = int(input("Enter a number"))

#if length == width:
#print("Square")
#else:
#print("Not Square")

# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years.
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

#salary = int(input("Enter your salary"))
#serviceyears = int(input("Enter your years of service"))

#if serviceyears > 3:
#bonus = salary * 0.10
#bonussalary = bonus + salary
#print(salary)
#print(bonus)
#print(bonussalary)
#else:
#print("No bonus")
#print(salary)

# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.

#number = int(input("Enter a number"))

#if number >= 0:
#print(number**3)
#else:

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob",
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".

#name = input("Enter your name")

#if name == "Alice":
#print("Hello Alice")
#elif name == "Bob":
#print("you are not Bob, I am Bob")
#else:
#print("You must be Charlie")

# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"

#age = int(input("Enter your age"))
#if age > 0 and age < 11:
#print("You are too young to go to this school")
#elif age >= 11 and age <= 16:
#print("You can come to this school")
#elif age > 16:
#print("You are too old to come to this school")
#elif age <= 0:
#print("You are not born yet")
#else:
#print("Invalid input")

# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".

#month = input("Enter a month")
#if month == "March" or month == "April" or month == "May":
#print("Spring")
#elif month == "June" or month == "July" or month == "August":
#print("Summer")
#elif month == "September" or month == "October" or month == "November":
#print("Autumn")
#elif month == "December" or month == "January" or month == "February":
#print("Winter")
#else:
#print("I don't know")

# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.

#number1 = int(input("Enter a number"))
#number2 = int(input("Enter a number"))
#if number1 % 2 == 0 and number2 % 2 == 0:
#print("Even")
#elif number1 % 2 != 0 and number2 % 2 != 0:
#print("Odd")
#else:
#print(number1+number2)

# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.

#number1 = int(input("Enter a number"))
#number2 = int(input("Enter a number"))
#if number1 > number2:
#print(number1)
#if number1 < number2:
#print(number2)

# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years,
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years.
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

#salary = int(input("Enter your salary"))
#serviceyears = int(input("Enter your years of service"))

#if serviceyears > 7:
#bonus = salary * 0.20
#bonussalary = bonus + salary
#print(salary)
#print(bonus)
#print(bonussalary)
#elif serviceyears > 5:
#bonus = salary * 0.15
#bonussalary = bonus + salary
#print(salary)
#print(bonus)
#print(bonussalary)
#elif serviceyears >= 3 and serviceyears <= 5:
#bonus = salary * 0.10
#bonussalary = bonus + salary
#print(salary)
#print(bonus)
#print(bonussalary)
#else:
#print("No bonus")

# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest.
#   If all three ages are the same, print that.

# name1 = input("What is your name?\n")
# age1 = int(input("How old are you?\n"))
# name2 = input("What is your name?\n")
# age2 = int(input("How old are you?\n"))
# name3 = input("What is your name?\n")
# age3 = int(input("How old are you?\n"))

# #Oldest
# if age1 > age2 and age1 > age3:
#   print(name1 + " is the oldest and is " + str(age1) + " years old.")
# elif age2 > age1 and age2 > age3:
#   print(name2 + " is the oldest and is " + str(age2) + " years old.")
# elif age3 > age1 and age3> age2:
#   print(name3 + " is the oldest and is " + str(age3) + " years old.")
# else:
#   print("You are all the same age")

# #Youngest
# if age1 < age2 and age1 < age3:
#   print(name1 + "is the youngest and is " + str(age1) + "years old.")
# elif age2 < age1 and age2 < age3:
#   print(name2 + "is the youngest and is " + str(age2) + "years old.")
# elif age3 < age1 and age3 < age2:
#   print(name3 + "is the youngest and is " + str(age3) + "years old.")
# else:
#   print("You are all the same age")

# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

# lesson1 = input("Input your lesson:\n")
# mark1 = int(input("Input your mark:\n"))
# lesson2 = input("Input your lesson:\n")
# mark2 = int(input("Input your mark:\n"))
# lesson3 = input("Input your lesson:\n")
# mark3 = int(input("Input your mark:\n"))

# print("REPORT CARD:")

# #Lesson 1
# if mark1 > 80:
#   print(lesson1 + " - A grade")
# elif mark1 <= 80 and mark1 > 60:
#   print(lesson1 + " - B grade")
# elif mark1 <= 60 and mark1 > 50:
#   print(lesson1 + " - C grade")
# elif mark1 <= 50 and mark1 > 45:
#   print(lesson1 + " - D grade")
# elif mark1 <= 45 and mark1 > 25:
#   print(lesson1 + " - E grade")
# elif mark1 < 25:
#   print(lesson1 + " - F grade")
# else:
#   print("Go to see your teacher")

# #Lesson 2
# if mark2 > 80:
#   print(lesson2 + " - A grade")
# elif mark2 <= 80 and mark2 > 60:
#   print(lesson2 + " - B grade")
# elif mark2 <= 60 and mark2 > 50:
#   print(lesson2 + " - C grade")
# elif mark2 <= 50 and mark2 > 45:
#   print(lesson2 + " - D grade")
# elif mark2 <= 45 and mark2 > 25:
#   print(lesson2 + " - E grade")
# elif mark2 < 25:
#   print(lesson2 + " - F grade")
# else:
#   print("Go to see your teacher")

# #Lesson 3
# if mark3 > 80:
#   print(lesson3 + " - A grade")
# elif mark3 <= 80 and mark3 > 60:
#   print(lesson3 + " - B grade")
# elif mark3 <= 60 and mark3 > 50:
#   print(lesson3 + " - C grade")
# elif mark3 <= 50 and mark3 > 45:
#   print(lesson3 + " - D grade")
# elif mark3 <= 45 and mark3 > 25:
#   print(lesson3 + " - E grade")
# elif mark3 < 25:
#   print(lesson3 + " - F grade")
# else:
#   print("Go to see your teacher")
