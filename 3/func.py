# Functions: reusable mini-programs

#      f   ( x  )
def welcome(name):
    print("Welcome!")
    print("I am excited to have you here")
    correctname = input("Your name is " + name + ", right (yes/no)? ").lower()
    if correctname == "yes":
        print("Good! Nice to meet you.")
    elif correctname == "no":
        print("Oh, sorry.")
    else:
        print("Didn't understand your answer.")


welcome("Jani")
print("---")
welcome("Thomas")

















#########################################################################################
# Functions can return values

def multiply_by_2(number):
    return 2 * number