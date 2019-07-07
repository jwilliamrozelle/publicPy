import ogr
import gdalconst
import sys


# TASK 1
filename = r'C:\Users\jroze\Google Drive\Schoolwork\University of Wisconsin\Geog_378\Labs\Lab 8\PowerLine\PowerLine.shp'

#need a driver for specific file type
driver = ogr.GetDriverByName('ESRI Shapefile')

#open the file using the required driver
dataSource = driver.Open(filename, gdalconst.GA_ReadOnly)

#verify the file was opened, exit if not
if dataSource is None:
    print 'Failed to open file'
    sys.exit(1)

#get the first (and only) data layer
layer       = dataSource.GetLayer(0)
feat = layer.GetFeature(0)
line  = feat.GetGeometryRef()
nPts = line.GetPointCount()

lineLength = 0
for i in range(nPts - 1):
    point = line.GetPoint(i)
    x1 = line.GetX(i)
    y1 = line.GetY(i)
    x2 = line.GetX(i+1)
    y2 = line.GetY(i+1)
    d = (abs(x1 - x2)**2 + abs(y1 - y2)**2)**0.5
    lineLength += d
print "cumulative distance is %.2f miles or %.2f feet" % (lineLength / 5280, lineLength)

#close the file
dataSource.Destroy()


# TASK 2: Extend the program in task 2 so that it also opens Parcels.shp. Print out the
# attribute names and attribute data types of the layer. (Note that this question does 
#vnot ask for attribute values of any parcel.)

filename = r'C:\Users\jroze\Google Drive\Schoolwork\University of Wisconsin\Geog_378\Labs\Lab 8\Parcels\Parcels.shp'

#need a driver for specific file type
driver = ogr.GetDriverByName('ESRI Shapefile')

#open the file using the required driver
dataSource = driver.Open(filename, gdalconst.GA_ReadOnly)

# get the layer
layer = dataSource.GetLayer(0)

#get basic info about the layer
layerName   = layer.GetName()
layerTypeInt = layer.GetGeomType()
layerExtent = layer.GetExtent()
 
 
#convert integer layertype to text equivalent
layerTypeStr = ogr.GeometryTypeToName(layerTypeInt)
 
#print the name, type and extent of layer
print 'Layer', layerName,'is a', layerTypeStr,'layer.'

#step 4a above ---
#get access to the layer's non-spatial info: number of fields,
#field names, field types, etc.
featureDefn = layer.GetLayerDefn()
 
#get and print the number of fields
fieldCount = featureDefn.GetFieldCount()
 
print "The layer’s feature definition has the following", fieldCount, "fields:"
 
#step 4b above --- print info about every field
for i in range(0,fieldCount):
   fieldDef   = featureDefn.GetFieldDefn(i)
   fname      = fieldDef.GetNameRef()
   fwidth     = fieldDef.GetWidth()
   fprecision = fieldDef.GetPrecision()
   ftype      = fieldDef.GetType()
 
   #convert integer ftype to text equiv
   ftypeS = fieldDef.GetFieldTypeName(ftype)
  
   values = (fname,ftypeS,fwidth,fprecision)
   fmt  = '%s: %s (%d.%d)'
   print fmt % values


