# This is an arrogant program calculates the area of a triangle, and 
# shames the user for needing it.

# The following line prints the next string in the shell. The next print (blank)
# adds a blank space after the line

print "This program finds the area of a triangle or trapezoid."
print "If you've graduated from 4th grade, you should frankly be ashamed of using it."
print 	

# The next requests input from the user. The string inside parentheses is a prompt
# that appears on screen. It prompts for two variables - height and base.
shape = input("Type 1 for triangle or 2 for trapezoid: ")

if shape == 1 : #where shape is 1 (for triangle) it does the following
    print  
    height = input("Please enter the height of the triangle: ") #requests height
    base = input("Please enter the base length of the triangle: ") #user inputs base
    area = 0.5 * height * base #calculates area of a triangle
    print
    print "Was this really necessary? I mean, we have calculators now." #Taunts the user
    print "The area of a triangle with height", height, "and base", base, "is", area, "." #shows the result

elif shape == 2 : # otherwise, check to see if the user entered 2 for trapezoid
    print  # puts a blank line, for aesthetics
    height = input("Please enter the height of the trapezoid: ") # Asks for trapezoid height
    baseA = input("Please enter length of base a of the trapezoid: ") #Asks for trapezoid base a length
    baseB = input("Please enter length of base b of the trapezoid: ") #Asks for trapezoid base b length
    area = 0.5 * height * (baseA + baseB) #calculates the area of a trapezoid and assigns it to the area variable
    print
    print "You definitely didn't need to use this function, but since you did..." # a little demeaining jab
    print "The area of a trapezoid with height", height, "and bases", baseA, "and", baseB, "is", area, "."


else:
    print  
    print "Come on Einstein, this isn't rocket science." # makes fun of the user for the messing up a basic request
    print "You must type 1 for triangle or 2 for a trapezoid" # repeats the instructions
    
raw_input() #keeps the command prompt window open until 'enter' when running this program