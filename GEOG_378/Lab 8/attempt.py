import ogr
import gdalconst
import sys

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
layerName   = layer.GetName()
layerType   = layer.GetGeomType()
layerExtent = layer.GetExtent()

print "SpatialRef: ", layer.GetSpatialRef()

#convert integer layertype to text equiv
layerTypeS = ogr.GeometryTypeToName(layerType)

print 'Layer', layerName, 'is a', layerTypeS, 'layer with bounding box:'
print layerExtent,'\n'

#get access to the layer's non-spatial info: number of fields,
#field names, types, etc.
featureDefn = layer.GetLayerDefn()

fieldCount = featureDefn.GetFieldCount()

print "The layer's feature definition has the following",fieldCount,"fields:"
feat = layer.GetFeature(0)

print "feature is ", feat

line  = feat.GetGeometryRef()
print "line is", line.Length(), "units in length"

nPts = line.GetPointCount()

print "there are ", nPts, "points"

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

thirdPoint = line.GetPoint(2)





for i in range(fieldCount):
    fieldDef      = featureDefn.GetFieldDefn(i)
    
    fldName       = fieldDef.GetNameRef()
    fldWidth      = fieldDef.GetWidth()
    fldPrecision  = fieldDef.GetPrecision()
    fldType       = fieldDef.GetType()

    #convert integer ftype to text equiv
    fldTypeS = fieldDef.GetFieldTypeName(fldType)
    
    values = (fldName,fldTypeS,fldWidth,fldPrecision)
    fmt    = '%s: %s (%d.%d)'
    print fmt % values

print '\n'
featureCount = layer.GetFeatureCount()
print 'There are',featureCount,'features:'

for i in range(featureCount):
   feature  = layer.GetFeature(i)
   geometry = feature.GetGeometryRef()
   
   x = geometry.GetX()
   y = geometry.GetY()
    
   airportName = feature.GetField('name')
   airportQuad = feature.GetField('quadname')
   airportLat  = feature.GetField('lat')
   airportLon  = feature.GetField('lon')

   values = (airportName,airportQuad,airportLon,airportLat)
   fmt = '%s of the %s Quad at lon, lat (%.6f,%.6f)'
   print fmt % values
   print 'has coordinates (%.2f,%.2f)\n' % (x,y)
   
    
   feature.Destroy()   # free memory for that feature   



#close the file
dataSource.Destroy()

