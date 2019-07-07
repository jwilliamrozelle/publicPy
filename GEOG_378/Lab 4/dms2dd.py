import math

def dms2dd(dmsTuple):
    degrees = float(dmsTuple[0]) #this section converts to float and allows for spaces if the user enters them
    minutes = float(dmsTuple[1])
    seconds = float(dmsTuple[2])
        
    if degrees < 0: #negative latitude/longitude value
        decdeg = degrees - (minutes / 60.0) - (seconds/3600.0)
    elif degrees >= 0: #positive latitude longitude value
        decdeg = degrees + (minutes / 60.0) + (seconds/3600.0)
    return decdeg

def dd2dms(decdeg):
    degrees = int(decdeg) #keeps the value positive or negative
    minutes = int((abs(decdeg) - abs(degrees)) * 60) #will always return a positive 
    seconds = (abs(decdeg) - abs(degrees) - (minutes / 60.0)) * 3600.0 #will always return a positive
    return (degrees, minutes, seconds)

loopCount = 0
print "\n----------PROGRAM START----------"
while loopCount <= 3:
    loopCount +=1
    timesLeft = 3 - loopCount
    attempt = loopCount + 1
    try:
        
        degree = raw_input("\n\nPlease enter a latitude or longitude value in DMS or DD format: \n")
        myTuple = tuple(degree.split(',')) #turns the input into a tuple
        if len(myTuple) == 1:
            output = dd2dms(float(degree)) #if tuple is length one, it ignores the tuple, and converts the input to float
            print "\nThe input value is in DD form"
            print "Its DMS form is", output
        elif len(myTuple) == 3:
            output = dms2dd(myTuple) #if tuple is length 3, it runs the dms2dd function using the tuple created above
            print "\nThe input is in DMS form"
            print "The DD form is", output
        else:
            print "\nFunction failed - wrong length" #if tuple is not the correct length, it produces this message.
            print "There are", timesLeft, "attempts left."
            print "\n\n----------ATTEMPT", attempt, "----------"
        break
    except:
        if timesLeft > 0: #prints the following message when there is still time
            print "\nYou must enter numbers"
            print "There are", timesLeft, "attempts left."
            print "\n\n----------ATTEMPT", attempt, "----------"
        else: # if you've maxed out on tries, you get this one
            print "\n\nFailed 3 times"

raw_input("\n\nPress ENTER to end >")
        
        

