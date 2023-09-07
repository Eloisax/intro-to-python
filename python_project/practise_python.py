Green = '\033[92m'

print(Green)



# print("Hello, welcome to your wellbeing diary. Write how you are feeling, and look back at howyou have felt throughout the past week. You may be able to identify whta makes you feel good and what makes you feel bad. If you want to stop adding entries into your diary please type 'Exit'")




# def diary_add():
#   info_to_add = input("Would you like to read or add to your diary?\n")
#   if info_to_add.lower() == "read":
#     read_diary()
#   elif info_to_add.lower() == "add":
#     diary_date()
#   else:
#     print("Invalid option")
#     open_diary()
  

# def diary_date():
#   f = open("diary.txt", "a")
  
#   add_date = True
#   add_mood = True
#   add_hobby = True
#   while add_date != "":
#     add_date = str(input("What is the date?\n"))
#     if add_date.lower() == "exit":
#       break
#     elif add_date:
#       f.write("Date: " + add_date + "\n")
#     add_mood = input("What is your mood?\n")
#     inc_hobby = str(input("Do you want to add a hobby\n"))
#     if inc_hobby.lower() == "yes":
#       f.write("Mood: " + add_mood + "\n")
#     elif inc_hobby == "no":
#       inc_hobby = False
#     else:
#       f.write("Mood: " + add_mood + "\n\n")
#     if inc_hobby.lower() == "yes":
#       add_hobby = input("What is your hobby?\n")
#     inc_habit = str(input("Do you want to add habits\n"))
#     if inc_habit.lower() == "yes":
#       add_habits()
#     else:
#       f.write("Hobby: " + add_hobby + "\n")
#   f.close()
#   close_diary()

# def add_habits():
#   h = open("diary.txt", "a")
#   habit_bed = input("Did you make your bed today? (Please enter Yes or No)\n")
#   habit_bed = habit_bed.capitalize()
#   if habit_bed:
#     h.write("Bed Made: " + habit_bed + "\n")
#   habit_gym = input("Did you go to exercise today? (Please enter Yes or No)\n")
#   habit_gym = habit_gym.capitalize()
#   if habit_gym:
#     h.write("Exercised: " + habit_gym + "\n")
#   habit_water = input("Did you drink enough water today? (Please enter Yes or No)\n")
#   habit_water = habit_water.capitalize()
#   if habit_water:
#     h.write("Drank Water: " + habit_water + "\n")
#   habit_medidate = input("Did you medidate today? (Please enter Yes or No)\n")
#   habit_medidate = habit_medidate.capitalize()
#   if habit_medidate:
#     h.write("Medidated: " + habit_medidate + "\n")
#   habit_sleep = input("Did you get enough sleep? (Please enter Yes or No)\n")
#   habit_sleep = habit_sleep.capitalize()
#   if habit_sleep:
#     h.write("Enough Sleep: " + habit_sleep + "\n\n")

# # add_habits()
  

# def close_diary():
#   close_diary_now = input("Do you want to close the diary\n")
#   if close_diary_now == "yes":
#     f2 = open("diary.txt", "r")
#     for date_add in f2:
#       print(date_add)
#   else:
#     print("Have a nice day")
#     diary_results = input("Do you want to read your  diary\n")
#     if diary_results == "yes":
#       read_diary()
      

# def read_diary():
#     f2 = open("diary.txt", "r")
#     for date_add in f2:
#       print(date_add)
    

# def open_diary():
#   open_the_diary = input("Do you want to open the diary")
#   if open_the_diary == "yes":
#     diary_date()
#   else:
#     print("Thanks")

# diary_add()

# # def diary_hobby():
# #   f = open("diary.txt", "a")
  
# #   add_date = True
# #   add_hobby = True
# #   while add_date != "" and add_hobby != "":
# #     add_date = input("What is the date?\n")
# #     if add_date:
# #       f.write("Date: " + add_date + "\n")
# #     add_hobby = input("What is your hobby?\n")
# #     if add_hobby:
# #       f.write("Hobby: " + add_hobby + "\n\n")
# #   read_diary = input("Do you want to close the diary\n")
# #   if read_diary == "yes":
# #     f2 = open("diary.txt", "r")
# #     for hobby_add in f2:
# #       print(hobby_add)
# #   else:
# #     print("end")
# #   f.close()







