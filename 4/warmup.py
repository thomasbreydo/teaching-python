"""
 1. Write a program that asks the user for the length and width of a
    rectangle and prints the area of the rectangle.


    (Bonus: print the perimeter.)


 2. Hard. (I haven't fully covered this yet, so *skip it* if you want.)
    Turn the area calculation above into a function. Define a function
    called area() that takes in a width and height and returns their product.

    IF YOU FINISH this problem, send me a message on Zoom.

 3. Write a program that asks the user for their age and tells them if they
    can vote (18 or older)
"""

# f(x) = 2x
# f(x, y) = 2x + 5y

def area(width, length):
    return width * length

x = area(5, 6)

print(x)

def perimeter(width, length):
    # return the perimeter
    pass


#
# length = int(input("Length? "))
# width = int(input("Width? "))
#
# print(length * width)