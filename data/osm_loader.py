#Import osmnx and geopandas modules
import osmnx
import geopandas

#Load OSM data using place definition and greenspace definition
def load_osm_greenspace(place_name, tags):
    try:
        greenspace = osmnx.features.features_from_place(place_name, tags, which_result=None)
        
        #Display greenspace_data basic information
        #greenspace_data is a GeoDataFrame
        print(greenspace.head())
        print(f"Total greenspaces: {len(greenspace)}")
        print(f"The greenspace data in {place_name} has {len(greenspace.columns)} columns, or attributes, per park")

        return greenspace
    except:
        print(f"No greenspaces found for {place_name}")

place_name = 'Phoenix, Arizona'
greenspace_tags = {'leisure': ['park', 'nature_reserve']}
greenspace_data = load_osm_greenspace(place_name, greenspace_tags)