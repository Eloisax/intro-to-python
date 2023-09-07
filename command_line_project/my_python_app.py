print(
  "Hello, welcome to your wellbeing diary. Write how you are feeling, and look back at howyou have felt throughout the past week. You may be able to identify whta makes you feel good and what makes you feel bad. If you want to stop adding entries into your diary please type 'Exit' when asked to enter a date\n"
)

feelings = [{
  "Mood": "Sad",
  "Action": "Do something that makes you happy"
}, {
  "Mood": "Happy",
  "Action": "Write down what makes you happy"
}, {
  "Mood": "Tired",
  "Action": "Rest"
}, {
  "Mood": "Overwhelmed",
  "Action": "Try to focus on one sense at a time"
}, {
  "Mood": "Excited",
  "Action": "Do more things that make you feel this way"
}, {
  "Mood": "Unproductive",
  "Action": "Give 5 minutes to a task you are putting off"
}]


def diary_add():
  info_to_add = input("Would you like to read or add to your diary?\n")
  if info_to_add.lower() == "read":
    read_diary()
  elif info_to_add.lower() == "add":
    diary_date()
  else:
    print("Invalid option")
    open_diary()


# Here the user fills in information to be written to their diary, they can choose to not add to sections.
# Note- I was having issues with getting mood to write to the diary below the date (was adding above date in the text file) due to the for loop in the below function so had to repeat asking the user 2 for their mood


def diary_date():
  f = open("diary.txt", "a")

  add_date = True
  add_your_mood = True
  while add_date != "":
    add_date = str(input("\nWhat is the date?\n"))
    if add_date:
      f.write("Date: " + add_date + "\n")
    if add_date.lower() == "exit":
      break
    elif add_date.lower() == "":
      break

    inc_mood = str(input("Do you want to add your mood\n"))
    if inc_mood.lower() == "yes":
      add_mood()
      add_your_mood = str(input("Please enter your mood again\n"))
      f = open("diary.txt", "a")
      f.write("Mood: " + add_your_mood + "\n")

    inc_hobby = str(input("Do you want to add a hobby\n"))
    if inc_hobby.lower() == "yes":
      add_hobby = str(input("What is your hobby?\n"))
      f.write("Hobby: " + add_hobby + "\n")

    inc_habit = str(input("Do you want to add habits\n"))
    if inc_habit.lower() == "yes":
      add_habits()
    f.write("\n")
  f.close()
  close_diary()


# user inputs their mood, if this mood is the same as a mood stored in the above dictionary then a suggestion is provided to the user to improve/maintain their mood


def add_mood():
  your_mood = input("What is your mood\n")
  for dictionary in feelings:
    if dictionary.get('Mood') == your_mood:
      print(dictionary["Action"])


# Asks the user to enter if they have done a series of habits, this then gets written to the file


def add_habits():
  h = open("diary.txt", "a")
  habit_bed = input("Did you make your bed today? (Please enter Yes or No)\n")
  habit_bed = habit_bed.capitalize()
  if habit_bed:
    h.write("Bed Made: " + habit_bed + "\n")
  habit_gym = input("Did you go to exercise today? (Please enter Yes or No)\n")
  habit_gym = habit_gym.capitalize()
  if habit_gym:
    h.write("Exercised: " + habit_gym + "\n")
  habit_water = input(
    "Did you drink enough water today? (Please enter Yes or No)\n")
  habit_water = habit_water.capitalize()
  if habit_water:
    h.write("Drank Water: " + habit_water + "\n")
  habit_medidate = input("Did you medidate today? (Please enter Yes or No)\n")
  habit_medidate = habit_medidate.capitalize()
  if habit_medidate:
    h.write("Medidated: " + habit_medidate + "\n")
  habit_sleep = input("Did you get enough sleep? (Please enter Yes or No)\n")
  habit_sleep = habit_sleep.capitalize()
  if habit_sleep:
    h.write("Enough Sleep: " + habit_sleep + "\n")


# Lets the user continue to add to their diary, or if they want to close the diary they can either close or read through it


def close_diary():
  close_diary_now = input("\nDo you want to close the diary\n")
  if close_diary_now == "no":
    diary_add()
  else:
    print("\nHave a nice day\n")
    diary_results = input("Do you want to read your diary\n")
    if diary_results == "yes":
      print("\n")
      read_diary()


# This allows the user to read what they have entered into the diary


def read_diary():
  print("\n")
  f2 = open("diary.txt", "r")
  for date_add in f2:
    print(date_add)


# This is a form of validation, if the user enters a wrong value in the first question (read or add to the diary e.g. the user enters "close" or other invalid option, this gives them a chance to edit their diary or they can continue with not opening, editing or reading the diary. Putting a stop to the code).


def open_diary():
  open_the_diary = input("\nDo you want to open the diary")
  if open_the_diary == "yes":
    diary_date()
  else:
    print("Thanks")


diary_add()
