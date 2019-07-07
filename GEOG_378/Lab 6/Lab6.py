
class City:
    def __init__(self, Name=’n/a’, Lat = -999, Lon = -999, Pop1970 = 0, Pop1975 = 0, Pop1980 = 0, Pop1985 = 0, Pop1990 = 0, Pop1995 = 0, Pop2000 = 0, Pop2005 = 0, Pop2010 = 0):
        self.name = Name
        self.label = Label
        self.lat  = Lat
        self.lon  = Lon
        self.yr1970 = Pop1970
        self.yr1975 = Pop1975
        self.yr1980 = Pop1980
        self.yr1985 = Pop1985
        self.yr1990 = Pop1990
        self.yr1995 = Pop1995
        self.yr2000 = Pop2000
        self.yr2005 = Pop2005
        self.yr2010 = Pop2010
        
        if -90  <= lat <= 90  : self.lat  = float(lat)
        else                  : self.lat  = 0.0
                      
        if -180 <= lon <= 180 : self.lon  = float(lon)
        else                  : self.lon  = 0.0
        
        try:
            yr1970 = float(yr1970)
            yr1975 = float(yr1975)
            yr1980 = float(yr1980)
            yr1985 = float(yr1985)
            yr1990 = float(yr1990)
            yr1995 = float(yr1995)
            yr2000 = float(yr2000)
            yr2005 = float(yr2005)
            yr2010 = float(yr2010)
        except:
            print "The population figures for one or more years were in the wrong format."
        
        
    def printCities(self):
        print "%s is at latitude %.2f" % (self.name,self.lat)
        print "Population in 1970: %s" % (self.yr1970)
        print "Population in 1975: %s" % (self.yr1975)
        print "Population in 1980: %s" % (self.yr1980)
        print "Population in 1985: %s" % (self.yr1985)
        print "Population in 1990: %s" % (self.yr1990)
        print "Population in 1995: %s" % (self.yr1995)
        print "Population in 2000: %s" % (self.yr2000)
        print "Population in 2005: %s" % (self.yr2005)
        print "Population in 2010: %s" % (self.yr2010)
        
       
    def printMilesNorth(self,city):
        dist = (self.lat-city.lat)*24859./360.
        Fmt  = ‘%s is %.1f miles north of %s’
        vals = (self.name, dist, city.name)
        print fmt % vals
 
       
#create LA and over-ride all default values
LA = City(name = ‘Los Angeles’,Lat=33.93,Lon=-120.)
 
#create Mad and over-ride two default values
Mad = City(name=’Madison’,Lat=43.08)
 
print “longitude of LA is”,LA.lon
print “longitude of Mad is”,Mad.lon


with open("C:\\Users\\jroze\\Google Drive\\Schoolwork\\University of Wisconsin\\Geog_378\\Labs\\Lab 5\\CityPop.csv", 'r') as infile:

    data = infile.read()



