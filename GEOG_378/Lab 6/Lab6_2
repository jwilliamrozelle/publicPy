#pulls the previously written code for a dictionary with the information for cities.
execfile('Lab5_task1.py')

# The code block below creates a class "City", with name, label, lat, long, and population
# attributes. The population is a dictionary.

class City:
    def __init__(self, Name= "N/A", Label = 'N/A', Lat = -999, Lon = -999, popDictionary = {"yr1970": None, "yr1975": None, \
        "yr1980": None, \
        "yr1985": None, \
        "yr1990": None, \
        "yr1995": None, \
        "yr2000": None, \
        "yr2005": None, \
        "yr2010": None}):
        self.name = Name
        self.label = Label
        self.lat  = Lat
        self.lon  = Lon
        self.popDict = popDictionary
        
        #Checks for valid lat/long entries. Invalid entries are just made to be 0.
        if -90  <= self.lat <= 90  : self.lat  = float(self.lat)
        else                  : self.lat  = 0.0
                      
        if -180 <= self.lon <= 180 : self.lon  = float(self.lon)
        else                  : self.lon  = 0.0
        
        try: #makes sure that the years can be converted to float type
            self.popDict["yr1970"] = float(self.popDict["yr1970"])
            self.popDict["yr1975"] = float(self.popDict["yr1975"])
            self.popDict["yr1980"] = float(self.popDict["yr1980"])
            self.popDict["yr1985"] = float(self.popDict["yr1985"])
            self.popDict["yr1990"] = float(self.popDict["yr1990"])
            self.popDict["yr1995"] = float(self.popDict["yr1995"])
            self.popDict["yr2000"] = float(self.popDict["yr2000"])
            self.popDict["yr2005"] = float(self.popDict["yr2005"])
            self.popDict["yr2010"] = float(self.popDict["yr2010"])
            
            
        except:
            print "The population figures for one or more years were in the wrong format."
        
        
    def printCities(self): # this is a method that prints the attributes of the class City
        print "The name is: %s" % (self.name)
        print "The label is: %s" % (self.label)
        print "\n%s is at latitude %.2f" % (self.name,self.lat)
        print "The city contains the following dictionary of population over years:"
        print self.popDict
    
    
    # This creates a method for the class that calculates the distance between two points.
    # First converts degrees to radians, and than calculates the distance.
    # Finally, the method prints the distance.
    def printDistance(self, othercity):
        try:
            import math # import the math
            rlatA = math.radians(self.lat)
            rlongA = math.radians(self.lon)
            rlatB = math.radians(othercity.lat)
            rlongB = math.radians(othercity.lon)
        
            #Calculates the angle
            angle = math.acos((math.sin(rlatA)*math.sin(rlatB)) + (math.cos(rlatA)*math.cos(rlatB)*math.cos(rlongA - rlongB)))
        
            #Calculates the Spherical distance
            sphereDist = angle*6300
        
            #prints the spherical distance
            print "The distance between %s and %s is %.2f" % (self.label, othercity.label, sphereDist)
        
        except:
            print "Operation failed, it is likely that one or more coordinates is in the"
            print "wrong format."
    
    #This function will require input in the "yrXXXX" format. It takes the input, calculates
    # the difference between the values in the dictiornary. Assigns this to the variable 
    # popChange, and then prints a statement about it. There are two versions of the statement
    # depending on whether the population has increased or decreased.
    
    def printPopChange(self, year1, year2): 
        try:
            popChange = self.popDict[year2] - self.popDict[year1] #calculates the difference between years
            if popChange >= 0:
                print "The population of %s was %.2f million higher in %s and %s." % (self.label, popChange, year2, year1)
            elif popChange < 0:
                print "The population of %s was %.2f million lower in %s than %s." % (self.label, abs(popChange), year2, year1)
        except:
            print "\nThe calculation failed."
            print "Check to make sure that the population dictionary is loaded, and in the correct format"

Cities = []
for i in cities:
    try:
        instance = City()
        instance.name = cities[i]["city"]
        instance.label = cities[i]["label"]
        instance.lat = float(cities[i]["latitude"])
        instance.lon = float(cities[i]["longitude"])
        instance.popDict["yr1970"] = float(cities[i]["yr1970"])
        instance.popDict["yr1975"] = float(cities[i]["yr1975"])
        instance.popDict["yr1980"] = float(cities[i]["yr1980"])
        instance.popDict["yr1985"] = float(cities[i]["yr1985"])
        instance.popDict["yr1990"] = float(cities[i]["yr1990"])
        instance.popDict["yr1995"] = float(cities[i]["yr1995"])
        instance.popDict["yr2000"] = float(cities[i]["yr2000"])
        instance.popDict["yr2005"] = float(cities[i]["yr2005"])
        instance.popDict["yr2010"] = float(cities[i]["yr2010"])
        Cities.append(instance)
        
    except:
        print "The city creation loop failed."
        
        
for i in Cities: #Prints the attributes of all 39 Cities
    try:
        i.printCities()
    except:
        print "Printing the cities failed."

