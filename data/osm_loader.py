#Import osmnx and geopandas modules
import osmnx
import geopandas

#Load OSM data using place definition and greenspace definition
def load_osm_greenspace(place_name, tags):
    greenspace = osmnx.features.features_from_place(place_name, tags, which_result=None)
    return greenspace


place_name = 'Phoenix, Arizona'
greenspace_tags = {'leisure': ['park', 'nature_reserve']}
greenspace_data = load_osm_greenspace(place_name, greenspace_tags)

#Attempt at error handling but NOT WORKING YET because osmnx doesn't return an empty data set
if greenspace_data.empty:
        print(f"No parks found for Phoenix, Arizona")
else:
    #Display greenspace_data basic information
    #greenspace_data is a GeoDataFrame
    print(greenspace_data.head())
    print(f"Total greenspace: {len(greenspace_data)}")
    print(f"{place_name} has {len(greenspace_data.columns)} columns, or attributes, per park")