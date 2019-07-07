# This program calculates the area of a triangle.

# The following line prints the next string in the shell. The next print (blank)
# adds a blank space after the line
print "This program finds the area of a triangle."
print 	

# The next requests input from the user. The string inside parentheses is a prompt
# that appears on screen. It prompts for two variables - height and base.
height = input("Please enter the height of the triangle: ")
base = input("Please enter the base length of the triangle: ")

# This section calculates the variable 'area' with a formula
area = 0.5 * height * base

# The following prints the string, then the value of the height variable, then
# a string, then the value of the base variable, then a string and the area of the
# base value, finally a string and the newly calculated area.
print "The area of a triangle with height", height, "and base", base, "is", area, "."

raw_input() #Keeps the command prompt window open until "enter"