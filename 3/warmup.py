"""
Write a program that tells a student what they should depending on if it's the weekend:

1.
  Ask, "Is it the weekend (yes/no)? "

2.
  If it's the weekend, use 3 print statements to say:
    sleep
    brunch
    chill

  If it's a weekday, use 2 print statements to say:
    wake up
    go to school

*3.
  If the user says something other than "yes" or "no", print with "Invalid input"

*4.
  Treat inputs like "Yes" and "YES" as valid, and print responses correctly.
"""

is_weekend = input("Is it the weekend? ")
if is_weekend.lower() == "yes":
    print("sleep")
    print("brunch")
    print("chill")
elif is_weekend.lower() == "no":
    print("wake up")
    print("go to school")
else:
    print("invalid input")