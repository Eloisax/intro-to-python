# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.

## width = 5
## height = 7
## area = width * height
## print("Rectangle of width " + str(width) + " and height " + str(height) + " has an area of " + str(area))

# 2. Write code that prints the length of the string, 'python'.

## name = "Python"
## name_length = len(name)
## print(name_length)

## print(len("Python"))

# 3. Print out the first and third letter of the word 'python'.

## word = "Python"
## print(word[0])

## print("Python"[2])

# 4. Ask the user to enter their name, and print out `Hello, <name>`.

## name = input("What is your name")
## print("Hello " + name)

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.

## age = int(input("What is your age "))
## future_age = age + 15
## print("Age in 15 years is " + str(future_age))

# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.

## age = int(input("What is your age "))
## name = input("What is your name ")
## future_age = age + 15
## print("Hello " + name + " Your age is " + str(age) + " Age in 15 years is " + str(future_age))

# 7. Ask the user to enter their hometown, print it out in uppercase letters.

## hometown = input("Please enter your hometown ")
## print(hometown.upper())

# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.

## colour = input("Enter your favourite colour ")
## print(len(colour))

# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.

## weather = input("Enter the weather ")
## month = input("Enter the month ")
## print("It is " + month + " and it is " + weather + " today")

# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.

## month = input("Enter the month ")
## temperature = int(input("Enter the temperature "))
## temperature2 = int(input("Enter the temperature "))
## temperature3 = int(input("Enter the temperature "))
## temperature4 = int(input("Enter the temperature "))
## temperature5 = int(input("Enter the temperature "))
## avg_temperature = (temperature+temperature2+temperature3+temperature4+temperature5)/5
## print("It is " + month + " and it is " + str(avg_temperature) + " degrees celsius")

# 11. Print out the above sentence but make the month upper case.

## print("It is " + month.upper() + " and it is " + str(avg_temperature) + " degrees celsius")

# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.

## animal = ("My favourite animal is:\n\tDog,\n\tCat")
## print(animal)

# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.

## name = input("What is your name ")
## number = int(input("Enter a number "))
## print(name[number].upper())

# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".

## welcome = "WelcometoPython"
## print(len(welcome))
## print(welcome[0:14:2])

fullname = "Alan" + "Turing"
length = len(fullname)
print(length)
middle_letter = fullname[int(length / 2)].lower()
print(int(length)/2)
print(middle_letter)