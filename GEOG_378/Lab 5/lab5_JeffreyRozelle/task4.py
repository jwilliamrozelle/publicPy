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
# the data starts after the column heads.

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

# This block asks the user to input the years in the correct format. It then
# checks to see if the inputed years match a objects in the columnHeads list. If
# it does not, the user has two more chances for each to enter a name that
# matches. On the third try, the program is terminated.


loopCount = 0
while loopCount < 3:
    
    loopCount += 1
    inputYear = raw_input("Type in the first requested year (in yr####) format > ")
    if inputYear in columnHeads:
        break
    elif loopCount < 3:
        print inputYear, "is not a year in the database, be certain to use yr#### format"
        continue
    else:
        print "After three attempts, you have not entered any matching year"
        raw_input("Press ENTER to terminate the program")
        exit()

loopCount = 0
while loopCount < 3:
    
    loopCount += 1
    inputYear2 = raw_input("Type in the second requested year (in yr####) format > ")
    if inputYear2 in columnHeads:
        break
    elif loopCount < 3:
        print inputYear2, "is not a year in the database, be certain to use yr#### format"
        continue
    else:
        print "After three attempts, you have not entered any matching year"
        raw_input("Press ENTER to terminate the program")
        exit()

# This try/except section attempts to open a file for writing (overwrite if a
# file of the same name exists) in the lab5Directory. if it fails, the program
# exits.

try:
    f = open(lab5Directory + '\\CityPopChg.csv', 'wt')
except:
    print "Could not open target file ", lab5Directory + '\\CityPopChg.csv'
    raw_input("Press ENTER to terminate the program")
    exit()

# writes column heads id, city and population change to the first row of the csv
# file specified above.
newColumnHeads = 'id,city,population_change\n'
f.write(newColumnHeads)

# This loop goes into each city 'sub' dictionary, and converts the population
# from the entered year into a float variable (they are stored as strings) in
# the cities dictionary). Then it calculates the difference between population
# from the two inputted years for each city. It gathers the cities into lines of
# string text, and writes the row to the csv file "f". The file is closed, and
# a variable is printed.

try:
    for i in cities:
        year1 = float(cities[i][inputYear])
        year2 = float(cities[i][inputYear2])
        pop_chg = year2 - year1
        cityID = cities[i]["id"]
        cityCity = cities[i]["city"]
        values = cityID    + "," + \
                 cityCity + "," + \
                 str(pop_chg)
        f.write(values + "\n")
    f.close()
except:
    print "Writing the values failed."
    raw_input("Press ENTER to terminate the program")
    exit()
    
print "The output file has been written to", lab5Directory + "\\CityPopChg.csv"
