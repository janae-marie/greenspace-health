#Import osmnx and geopandas modules
import osmnx
import geopandas

#Load OSM data using place definition
def load_osm_greenspace():
 greenspace = osmnx.features.features_from_place(\"Phoenix, Arizona\", {'leisure': 'park'}, which_result=None)
 return greenspace
 
load_osm_greenspace()
print(greenspace)
