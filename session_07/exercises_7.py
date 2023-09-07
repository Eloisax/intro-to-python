# Session 7 Exercises

## Section A
# 1. Write a function that prints your name

# def name():
#   ask_name = input("What is your name? ")
#   print(ask_name)

# name()



# 2. Write a function that accepts a name as a parameter and prints "Hello, <name>".

# def name(hello_name):
#   print("Hello, " + hello_name)

# name("Alice")
# name("Bob")
# name("Charlie")


# 3. Loop through the list ["Alice", "Bob", "Charlie"] and call the function you just wrote.

# names_list = ["Alice", "Bob", "Charlie"]
# for hello_name in names_list:
#   name(hello_name)



# 4. Write a function that prints the area of two passed in parameters.

# def area(length,width):
#   print("The area is " + str(length*width))

# area(8, 2)

# 5. Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list.

# def print_list(list_prm):
#   for x in list_prm:
#     print(x)

# print_list(["Test1", "Test2", "Test3"])

# 6. Put the following into a function that accepts age as a parameter:
#     1. If they are younger than 11, print "You're too young to go to this school".
#     2. If they are between 11 and 16, print "You can can come to this school".
#     3. If they are over 16, print 'You're too old for school".
#     4. If they are 0, print "You're not born yet!".

# def school(ages):
#   if ages < 11:
#     print("You're too young to go to this school.")
#   elif ages >= 11 and ages <= 16:
#     print("You can come to this school.")
#   elif ages > 16:
#     print("You're too old for school.")
#   elif ages == 0:
#     print("You're not born yet.")
#   else:
#     print("You didn't pick a number.")

#ages = str(input("What is your age"))
#school(18)



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (hint: x % 2 will return true for all odd numbers).

# def is_odd(number):
#     if number % 2 == 1:
#         return True
#     else:
#         return False

# is_odd(6)
# is_odd(5)

# 2. Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'.

# def reverse_word(word):
#   word_string = ""
#   word_length = len(word)
#   while word_length != 0:
#     word_length -= 1
#     word_string += word[word_length]
#   print(word_string)
#   return word_string

# reverse_word("Hello")

# 3. Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars on each line, E.g:
# ```
# *****
# ****
# ***
# **
# *
# ```

# def reverse_stars(stars):
#   number_of_stars = ""
#   for star_position in range(0, stars):
#     number_of_stars = number_of_stars + "*"
#   print(number_of_stars)
#   if stars > 1:
#     reverse_stars(stars - 1)

# reverse_stars(4)

# 4. Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked".

# def passcode_check(code):
#   pin = 1234
#   if code == pin:
#     print("Correct")
#   else:
#     print("Locked")

# passcode_check(9876)
# passcode_check(1234)

# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
#   For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

# def sum_multiples_3_and_5(limit):
#   sum = 0

#   for i in range(0, limit + 1):
#     if limit < 0:
#       print("The limit must be greater than 0")
#     if i % 3 == 0:
#       sum += i
#     elif i % 5 == 0:
#       sum += i
#   print(sum)

# sum_multiples_3_and_5(20)
    

# 6. Write a function called is_prime() that accepts a number and return True or False if the number of prime or not.

# def is_prime(number):

#   count = 0

#   for i in range(2, number):
#     if number % i == 0:
#       count = count + 1
#       break
  
#   if (count == 0 and number != 1):
#     print(str(number) + " Prime")
#     return True
#   else:
#     print(str(number) + " Not Prime")
#     return False

# is_prime(11)
# is_prime(12)


# 7. Write a function that checks to see if a string is a pallindrome, if it is, it will return True and False if it is not.

# def pallindrome(word):
#   reverse_word = word[::-1]
#   if word == reverse_word:
#     print(True)
#   else:
#     print(False)

# pallindrome("hello")
# pallindrome("racecar")


# 8. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not. 
#   Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.

# def pallindrome_sentence(sentence):
#     formatted_sentence = sentence.lower()
#     new_sentence = formatted_sentence.replace(' ', '')
#     reverse_sentence = new_sentence[::-1]
#     if new_sentence == reverse_sentence:
#         print(True)
#     else:
#         print(False)

# pallindrome_sentence("The cat sat on the mat")
# pallindrome_sentence("A nut for a jar of tuna")