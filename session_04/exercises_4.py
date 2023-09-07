# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.

#fruits = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
#print(fruits)

# 2. Add "Grapes" to the list and print the list.

#fruits.append("Grapes")
#print(fruits)

# 3. Change "Pears" to "Strawberries" and print the list.

#fruits[2] = "Strawberry"
#print(fruits)

# 4. Remove "Apples" from the list and print the list.

#del(fruits[0])
#print(fruits)

# 5. Print out the current length of the list.

#print(len(fruits))

# 6. Order the list alphabetically.

#fruits.sort()

# 7. Print out the list again.

#print(fruits)


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.

#fruits = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
#for fruit in fruits:
  #print(fruit)


# 2. Print the numbers 1 to 100 (including the number 100).

#for my_number in range(1, 101):
  #print(my_number)

# 3. Print all odd numbers from 1 to 100.

#for my_number in range(1, 101, 2):
  #print(my_number)

# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).

#for olympics in range (1896, 2022, 4):
  #print(olympics)

#not_held = [1916, 1940, 1944, 2022]
#for olympics in range(1896, 2022, 4):
  #if olympics not in not_held:
    #print(olympics)

# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.

#rand_list = [4, 8, 1, 10, 189, 6, 65, 12, 90, 19]
#even_count = 0
#odd_count = 0
#for i in rand_list:
  #if i % 2 == 0:
    #even_count = even_count + 1
  #else:
    #odd_count = odd_count + 1

#print("This list has " + str(even_count) + " even numbers and " + str(odd_count) + " odd numbers.")


# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.

#names = ["Bob", "Alice", "Charlie", "Evie", "James"]
#for name in names:
  #print("Hello " + name)

# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".

#phrase = "Supercalifragilisticexpialidocious"
#for i in phrase:
  #print(i)

# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.

#numbers = [2, 8, 4, 9,7]
#sqr_numbers = []
#for square in numbers:
  #sqr_numbers.append(square ** 2)
#print(sqr_numbers)

# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.

#names = ["Bob", "Alice", "Charlie", "Evie", "James"]
#doctor_names = []
#for name in names:
  #doctor_names.append("Dr. " + name)
#print(doctor_names)

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```

#for number in range(1, 101):
  #if (number % 3 == 0) and (number % 5 == 0):
    #print("FizzBuzz")
  #elif number % 3 == 0:
    #print("Fizz")
  #elif number % 5 == 0:
    #print("Buzz")
  #else:
    #print(number)

