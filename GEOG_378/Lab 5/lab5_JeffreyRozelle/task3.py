#Gives the option of changing the directory.
print "Would you like to manually enter a file name?"
manualFile = raw_input("Type 'y' for YES. Any other input will use the default > ")

if manualFile.lower() == 'y': #manual input of directory and file
    lab5Directory = raw_input("Enter the directory (without the file name) > ")
    inputFile = raw_input("Enter the file name > ")
    filename = lab5Directory + inputFile
else:
    # This is where the CityPop.csv file is stored on my computer
    lab5Directory = "C:\\Users\\jroze\\Google Drive\\Schoolwork\\University of Wisconsin\\Geog_378\\Labs\\Lab 5"
    filename = lab5Directory + "\\CityPop.csv"

try:
    cityPopulation = open(filename, "rt")
except:
    print "can't open", filename
    raw_input("Press ENTER to terminate the program")
    exit()

lstCity = cityPopulation.readlines() #Creates a list from the csv where each new line is an element of the list

#Stores the first element from the lstCity list as its own list. These are the column headers
columnHeads = lstCity[0].split(",")
columnHeads[13] = "yr2010" #simply to remove the \n
cities = {} #empty dictionary called 'cities'

# The following loop goes to the second row of the data (element [1], where
# the data starts after the column heads. If the loop fails, program gracefully
# exits

try:
    for city in lstCity[1:]:
        fields = city.split(",") #splits the string object by the comma and produces a list called field
        fields[13] = float(fields[13]) #Just removes the \n and turns it into a float object
        cityName = fields[4] #extracts the column with city name, to be used for the dictionary key
        cityName = cityName.upper() # makes it upper case. This is used to mitigate data entry error
        #The following line creates a dictionary of the row, where keys are taken from column heads, then paired with values
        #from the fields list. This dictionary becomes the value for each key in the cities dictionary.
        cities[cityName] = dict(zip(columnHeads, fields))
except:
    print "For loop failed."
    raw_input("Press ENTER to terminate the program")
    exit()

# This block asks the user to input the name of the cities and converts them to
# upper case. It then checks to see if the inputed names match a keys in the
# cities dictionary. If it does not, the user has two more chances for each to
# enter a name that matches. On the third try, the program is terminated.


loopCount = 0
while loopCount < 3:
    
    loopCount += 1
    inputCity1 = raw_input("Type in the name of the FIRST city > ").upper()
    if inputCity1 in cities:
        break
    elif loopCount < 3:
        print inputCity1, "is not one of the cities in the database"
        continue
    else:
        print "After three attempts, you have not entered any matching cities"
        raw_input("Press ENTER to terminate the program")
        exit()

loopCount = 0
while loopCount < 3:
    
    loopCount += 1
    inputCity2 = raw_input("Type in the name of the SECOND city > ").upper()
    if inputCity2 in cities:
        break
    elif loopCount < 3:
        print inputCity2, "is not one of the cities in the database"
        continue
    else:
        print "After three attempts, you have not entered any matching cities"
        raw_input("Press ENTER to terminate the program")
        exit()

import math # import the math
loopCount = 0 #starts the loop count at 0

# The section below takes the latitude and longitude of two cities from the
# dictionary cities, and assigns the values found to latA, latB, longA and longB.
# if it fails, error messages are produced. Additionally - it checks for valid
# latitudes and longitudes.


while loopCount < 3: # limits the number of attempts to 3
    loopCount+= 1

    try:
        latA = cities[inputCity1]["latitude"]
        latA = float(latA)
        if latA > 90 or latA < -90:
            print "Invalid latitude, must be between 90 and -90"
            continue # if there is an invalid lat, the loop will restart
        longA = cities[inputCity1]["longitude"]
        longA = float(longA)
        if longA > 180 or longA < -180:
            print "Invalid longitude, must be between 180 and -180"
            continue # if there is an invalid long, the loop will restart
        latB = cities[inputCity2]["latitude"]
        latB = float(latB)
        if latB > 90 or latB < -90:
            print "Invalid latitude, must be between 90 and -90"
            continue
        longB = cities[inputCity2]["longitude"]
        longB = float(longB)
        if longB > 180 or longB < -180:
            print "Invalid longitude, must be between 180 and -180"
            continue
        break
    except:
        print "There appears to be a missing number"
        
# the section below converts from degrees to radians
rlatA = math.radians(latA)
rlongA = math.radians(longA)
rlatB = math.radians(latB)
rlongB = math.radians(longB)

#Calculates the angle     
angle = math.acos((math.sin(rlatA)*math.sin(rlatB)) + (math.cos(rlatA)*math.cos(rlatB)*math.cos(rlongA - rlongB)))

#Calculates the Spherical distance
sphereDist = "%8.1f" % (angle*6300, )

#prints the spherical distance
print "\nSpherical distance between", inputCity1, "and", inputCity2, "is", sphereDist
