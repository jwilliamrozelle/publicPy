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



