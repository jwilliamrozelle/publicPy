# This is an arrogant program calculates the area of a triangle, and 
# shames the user for needing it.

# The following line prints the next string in the shell. The next print (blank)
# adds a blank space after the line

print "\nThis program finds the area of a triangle or trapezoid."
print "If you've graduated from 4th grade, you should speak to"
print "your policy makers about the state of education where you"
print "grew up."
print 	


loopCount = 0

# The "while" statement keeps looping until its condition (loopCount<3) made False. 


while loopCount<3:
    

# loopCount will increase 1 for each loop
    
    loopCount += 1
    timesLeft = 3 - loopCount

    try:
        print "\n---------PROGRAM START-------------"

        # The next requests input from the user. The string inside parentheses is a prompt
        # that appears on screen. It prompts for two variables - height and base.
        shape = input("Type 1 for triangle or 2 for trapezoid: ")

        if shape == 1 : #where shape is 1 (for triangle) it does the following
            print  
            height = input("Please enter the height of the triangle: ") #requests height
            base = input("Please enter the base length of the triangle: ") #user inputs base
            area = 0.5 * height * base #calculates area of a triangle
            print "\nWas this really necessary? I mean, we have calculators now." #Taunts the user
            print "The area of a triangle with height", height, "and base", base, "is", area, "." #shows the result

        elif shape == 2 : # otherwise, check to see if the user entered 2 for trapezoid
            print  # puts a blank line, for aesthetics
            height = input("Please enter the height of the trapezoid: ") # Asks for trapezoid height
            baseA = input("Please enter length of base a of the trapezoid: ") #Asks for trapezoid base a length
            baseB = input("Please enter length of base b of the trapezoid: ") #Asks for trapezoid base b length
            area = 0.5 * height * (baseA + baseB) #calculates the area of a trapezoid and assigns it to the area variable
            print "\nYou definitely didn't need to use this function, but since you did..." # a little demeaining jab
            print "The area of a trapezoid with height", height, "and bases", baseA, "and", baseB, "is", area, "."

        else: #You get these errors when you don't type 1 or 2 at the prompt
            if timesLeft > 0: # if there are still loops to fix your inputs
                print "\nCome on Einstein, this isn't rocket science." # makes fun of the user for the messing up a basic request
                print "You must type 1 for triangle or 2 for a trapezoid" # repeats the instructions
                print "You have ", timesLeft, "tries left before I'm leaving."
                continue
            else: # when you've made the program run out of patience / loops
                print "\nThat's it. We're done here."
        break

        

    except:
        if timesLeft > 0: #prints the following message when there is still time
            print  
            print "\nYou didn't enter a valid number, bro." # makes fun of the user for the messing up a basic request
            print "None of this character nonesense when you are"
            print "supposed to put in a number. mkay?"
            print "You have ", timesLeft, "tries left before I'm leaving."
        else: # if you've maxed out on tries, you get this one
            print "\nThree strikes, you're out."
            print "I can't help you if you can't help yourself."
