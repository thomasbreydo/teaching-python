# Booleans: True/False (yes/no) values

"""
1. Set the "short" variable
    a. Ask for user's height
    b. Set the "short" variable to True if less than 5 ft
    c. Otherwise, set the "short" variable to False

2. Set the "happy" variable
    a. Ask if use is happy
    b. Set the "happy" variable to True if user says yes
    c. Otherwise, set the "happy" variable to False

3. Respond
    a. If the user is happy, say "Glad you're happy!"
    b. If the user isn't happy and the user is short, say "I hope you aren't sad because of your height."
    c. If the user isn't happy and the user is tall say "Feel better."
"""


height = input("How many feet tall are you? ")
if int(height) < 5:
    short = True
else:
    short = False

happy_yes_or_no = input("are you happy? ")
if happy_yes_or_no == "yes":
    happy = True
else:
    happy = False

if happy:
    print("Glad you're happy!")
elif not happy and short:
    print("I hope you aren't sad because of your height.")
elif not happy and not short:
    print("Feel better")

# not, and, or, if, elif, else
# 3. Respond
#     a. If the user is happy, say "Glad you're happy!"
#     b. If the user isn't happy and the user is short, say "I hope you aren't sad because of your height."
#     c. If the user isn't happy and the user is tall say "Feel better."