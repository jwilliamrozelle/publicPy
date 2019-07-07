# I had some spare time, so I made the output a little different
# just seemed nicer to me - but the code that does exactly what's requested
# is below.

print "This little script will tell you some interesting"
print "tidbits about latitudes and longitudes you enter."

loopCount = 0

while loopCount < 3: # limits the number of attempts to 3
    loopCount+= 1

    try:
        print "\n --------------PROGRAM START----------------"
        lat = input("\nLatitude: ")
        lat = float(lat)
        longitude = input("\nLongitude: ")
        longitude = float(longitude)

        if lat == 0:
            latmess = "\nThat location is on the equator"
        elif lat > 0 and lat <= 90:
            latmess = "\nThat location is north of the equator"
        elif lat < 0 and lat >= -90:
            latmess = "\nThat location is south of the equator"
        else: # since all remaining possibilities are greater than 90 or less than -90, no specification is needed
            latmess = "\nThat location does not have a valid latitude"

        if longitude == 0:
            longmess = "and on the prime meridian."
        elif longitude > 0 and longitude <= 180:
            longmess = "and east of the prime meridian"
        elif longitude < 0 and longitude >= -180:
            longmess = "and west of the prime meridian"
        else: # since all remaining possibilities are greater than 180 or less than -180, no specification is needed
            longmess = "and does not have a valid longitude!"

        print latmess, longmess
        break
    
    except:
        print "Enter a valid number for latitude and longitude"




#loopCount = 0

#while loopCount < 3: # limits the number of attempts to 3
#    loopCount+= 1
#
#    try:
#        print "\n --------------PROGRAM START----------------"
#        lat = input("\nLatitude: ")
#        lat = float(lat)
#        longitude = input("\nLongitude: ")
#        longitude = float(longitude)
#
#        if lat == 0:
#            print "\nThat location is on the equator."
#        elif lat > 0 and lat <= 90:
#            print "\nThat location is north of the equator"
#        elif lat < 0 and lat >= -90:
#            print "\nThat location is south of the equator"
#        else: # since all remaining possibilities are greater than 90 or less than -90, no specification is needed
#            print "\nThat location does not have a valid latitude!"
#
#        if longitude == 0:
#            print "That location is on the prime meridian."
#        elif longitude > 0 and longitude <= 180:
#            print "That location is east of the prime meridian"
#        elif longitude < 0 and longitude >= -180:
#            print "That location is west of the prime meridian"
#        else: # since all remaining possibilities are greater than 180 or less than -180, no specification is needed
#            print "That location does not have a valid longitude!"
#        break
    
#    except:
#        print "Enter a valid number for latitude and longitude"

raw_input("Press enter to close") #Keeps the command prompt window open until enter
            

        
        
        
