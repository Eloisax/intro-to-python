# Session 8 Exercises


# All of these questions will use a set of pre-made files with data in. The files are in the text_files directory.
# In order to access the text files from this file, make sure you get into the text_files directory when using read/write.
# Ex: f = open("text_files/austen.txt", "r") OR f = open("text_files/register.txt", "w")


## Section A
# 1. Read the file 'jabberwocky.txt' and print its content to the screen.

# f =open("text_files/jabberwocky.txt", "r")
# print(f.read())

# 2. Read the file 'austen.txt' and print the amount of lines in the file.

# f = open("text_files/austen.txt", "r")
# count = 0
# for line in f:
#   count += 1

# print(count)


# 3. Each line of the file 'numbers.txt' contains a number, write a script to add up all the values in the file.

# f = open("text_files/numbers.txt", "r")
# sum = 0 
# for x in f:
#   x = int(x)
#   sum += x

# print(sum)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask the user to enter their name and append this to a file called 'register.txt'

# f = open("text_files/register.txt", "a")

# name = True
# while name != "":
#   name = input("What is your name?\n")
#   if name:
#     f.write(name + "\n")
# f.close()

# f2 = open("text_files/register.txt", "r")
# for name in f2:
#   print(name)

# 2. Create a new file called 'even.txt' that contains only the even numbers from the file 'numbers.txt'.

# f = open("text_files/even.txt", "w")

# for x in open("text_files/numbers.txt"):
#     x = int(x)
#     if x % 2 == 0:
#         f.write(str(x) + "\n")

# f.close()


# 3. 'secret.txt' contains a secret message. Each number represents the letter of the alphabet where 1 = A, 2 = B ... Z = 26. 
#    Work out what the secret message says.

# alphabet = {
#     0: "!",
#     1: "A",
#     2: "B",
#     3: "C",
#     4: "D",
#     5: "E",
#     6: "F",
#     7: "G",
#     8: "H",
#     9: "I",
#     10: "J",
#     11: "K",
#     12: "L",
#     13: "M",
#     14: "N",
#     15: "O",
#     16: "P",
#     17: "Q",
#     18: "R",
#     19: "S",
#     20: "T",
#     21: "U",
#     22: "V",
#     23: "W",
#     24: "X",
#     25: "Y",
#     26: "Z"
# }

# word = ""
# for x in open("text_files/secret.txt", "r"):
#     x = int(x)
#     word = word + alphabet[x]
# print(word)

# 4. Benford’s law states that the leading digits in a collection of data are probably going to be small. 
#   For example, most numbers in a set (about 30%) will have a leading digit of 1, when the expected probability is 11.1% (i.e. one out of nine digits). 
#   Fake data is usually evenly distributed, where as real data The files 'accounts_1.txt', 'accounts_2.txt' and 'accounts_3.txt' contain financial transaction data. 
#   Work out which of the files contains fake data.

# import random

# def benford_calc_file(file_name):
#   f = open(file_name, "r")
#   return benford_calc(f)

# def benford_calc(data):

#   count = {}
#   for x in range(1,10):
#     count[str(x)] = 0

#   for num in data:
#       if num:
#         count[str(num[0])] += 1
  
#   return count 

# for x in range (1,4):
#   file_name = "text_files/accounts_" + str(x) + ".txt"
#   data = benford_calc_file(file_name)

#   print("Results for:" + file_name)

#   for y in range(1,10):
#       print(str(y) + " = " + str(data[str(y)]/100) + "%")

# random_nums = [str(random.randint(1,100)) for x in range(1,10001)]
# data = benford_calc(random_nums)
# print("Results for Random Nums")

# for y in range(1,10):
#       print(str(y) + " = " + str(data[str(y)]/100) + "%")