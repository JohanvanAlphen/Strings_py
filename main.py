# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# PART 1
# Players scored:
first_player_scored = "Ruud Gullit"
second_player_scored = "Marco van Basten"

# Minute scored:
goal_0 = 32
goal_1 = 54

scorers = first_player_scored + " " + str(goal_0) + \
    ", " + second_player_scored + " " + str(goal_1)

report = f'{first_player_scored} scored in the {goal_0}nd minute' '\n' f'{second_player_scored} scored in the {goal_1}th minute'

print("Scorers: ", scorers)
print("Complete sentence: ", report)

#  PART 2

player = second_player_scored

# Using slicing and find-method to isolate and store the player's first name:
first_name_find = player.find('Marco')  # find-method
first_name = player[0:5]  # slicing-method

print("Find 1st position of first name in string: ", first_name_find)
print("First name: ", first_name)


# Use find, slicing and len to isolate and store the length of their last name:
last_name_len_find = player.find("van Basten")  # find-method
last_name_len_slice = player[6:]  # slicing-method
last_name_len = len(last_name_len_slice)


print("Find 1st position of last name in string: ", last_name_len_find)
print("Length last name: ", last_name_len)

# Isolate and store the player's name in format G. von Examplestein:
name_short = first_name[0] + ". " + last_name_len_slice

print("Name short: " + name_short)

''' This is what the crowd chants when it looks like your player is going to score a goal
their first name plus an exclamation mark(!), x-times,
where x is the number of characters in their first name.
Make sure the last character of this string is not a space!'''

# Attempt 1:
# chant = (player[:-1] + "!") * (len(first_name))

# Attempt 2:
# chant = (player[:-1] + "!") * (len(first_name))

# Attempt 3:
# chant = (first_name[:-1] + "!") * (len(first_name[0:4]))

# Attempt 4:
# chant = (f'{first_name}! ') * (len(first_name))

# Attempt 5:
# chant = (len(first_name)) * (player[-1] + first_name + "!")

# Final attempt:
chant = (
    (player[: player.find(" ")] + "! ") * (len(first_name))
)[:-1]

print("Chant: ", chant)

# Make super-sure the last character of chant is not a space by using the inequality operator (!=):
good_chant = chant[-1] != " "

print("Good Chant: ", good_chant)
