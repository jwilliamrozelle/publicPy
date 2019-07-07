# Imports gdal
try:
    from osgeo import gdal
    from osgeo import gdalconst
    print 'Imported gdal from osgeo'
 
except:
    print "Unable to import gdal, osgeo may not be installed"

# imports numpy and matplotlib
try:
    import numpy as N
    import matplotlib.pyplot as pyplot
except:
    print "\nFailed to import numpy and/or matplotlib"

# Sets data directory
dataDir = r'C:\\Users\\jroze\\Google Drive\\Schoolwork\\University of Wisconsin\\Geog_378\\Labs\\Lab 7\\landsat\\'

# Open layers and converts them to arrays
try:
    layer1 = gdal.Open(dataDir+'L71026029_02920000609_B40_CLIP.TIF')
    layer2 = gdal.Open(dataDir+'L71026029_02920000609_B30_CLIP.TIF')
    nearIR = layer1.ReadAsArray()
    red = layer2.ReadAsArray()
    print "\nSuccessfully opened layers and red into Near Infrared and Red"
except:
    print "\nUnable to open layers. Check file path"

# uses the NDVI eqution for the two rasters. Forces them to a float type, and
# for instances where the equation would divide by 0, simply sets the value to 0
print "\nCalculating NDVI..."
try:
    ndvi = N.where(((red * 1.0) + (nearIR * 1.0)) == 0, 0, ((nearIR * 1.0) - (red * 1.0)) / ((red * 1.0) + (nearIR * 1.0)))
    print "Success!"
except:
    print "Failed"

# Set output driver to GTiff
print "\nSetting output driver..."
try:
    format    = 'GTiff'
    outDriver = gdal.GetDriverByName(format)
    print "Success!"
except:
    print "Failed"

# Create output dataset using driver. Saves to NDVIimage.tif in data directory
print "\nCreating output dataset using driver..."
try:
    cols = layer1.RasterXSize
    rows = layer1.RasterYSize
    nBands = 1
    dataType = gdalconst.GDT_Float32
    dsOut = outDriver.Create(dataDir+"NDVIimage.tif",cols,rows,nBands,dataType)
    print "Success!"
except:
    print "Failed"
    

# Set geotransform (geoTransform values are taken from layer1, assigned above)

print "\nSetting geotransform..."
try:
    geoT = layer1.GetGeoTransform()
    dsOut.SetGeoTransform(geoT)
    print "Success!"
except:
    print "Failed"

# Set projection (retrieved from one of the original images)
print "\nSetting projection from earlier image..."
try:
    dsOut.SetProjection(layer1.GetProjection())
    print "Success!"
except:
    print "Failed"

# add array to bands. In this case, there is only 1 band.
print "\nAdding calculated array to band..."
try:
    loopCount = 0
    for i in range(dsOut.RasterCount):
        loopCount = loopCount + 1
        band = dsOut.GetRasterBand(i+1)
        band.WriteArray(ndvi)
        print "Success!"
except:
    print "Failed"

# Close the connection
try:
    dsOut = None
    print "\nClosed"
except:
    print "\nUnable to close the dataset"
