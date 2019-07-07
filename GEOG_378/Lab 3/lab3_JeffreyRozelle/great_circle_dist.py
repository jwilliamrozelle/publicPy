print "This will calculate the distance between point A and point B"

import math # import the math
loopCount = 0 #starts the loop count at 0

while loopCount < 3: # limits the number of attempts to 3
    loopCount+= 1

    print "----------PROGRAM START----------"

#The section below gathers the latitude and longitude of points A and B

    try:
        latA = input("Latitude of Point A: ")
        latA = float(latA)
        if latA > 90 or latA < -90:
            print "Invalid latitude, must be between 90 and -90"
            continue # if there is an invalid lat, the loop will restart
        longA = input("Longitude of Point A: ")
        longA = float(longA)
        if longA > 180 or longA < -180:
            print "Invalid longitude, must be between 180 and -180"
            continue # if there is an invalid long, the loop will restart
        latB = input("Latitude of Point B: ")
        latB = float(latB)
        if latB > 90 or latB < -90:
            print "Invalid latitude, must be between 90 and -90"
            continue
        longB = input("Longitude of Point B: ")
        longB = float(longB)
        if longB > 180 or longB < -180:
            print "Invalid longitude, must be between 180 and -180"
            continue
        break
    except:
        print "Must be a valid number, please try again"
        
# the section below converts from degrees to radians
rlatA = math.radians(latA)
rlongA = math.radians(longA)
rlatB = math.radians(latB)
rlongB = math.radians(longB)

#Calculates the angle
angle = math.acos((math.sin(rlatA)*math.sin(rlatB)) + (math.cos(rlatA)*math.cos(rlatB)*math.cos(rlongA - rlongB)))

#Calculates the Spherical distance
sphereDist = angle*6300

#prints the spherical distance
print "\nSpherical distance is", sphereDist


raw_input("Press enter to close") #keeps command prompt open until finished