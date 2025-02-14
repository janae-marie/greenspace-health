#Import needed modules
import osmnx
import geopandas
import pandas

#Load OSM data using place definition and greenspace definition
def load_osm_greenspace(place_name, tags):
    try:
        greenspace = osmnx.features.features_from_place(place_name, tags, which_result=None)

        # List of columns we want to keep
        desired_columns = ['leisure', 'name', 'addr:city', 'addr:county', 'addr:state', 'type']

        # Add missing columns with NaN values
        for col in desired_columns:
            if col not in greenspace.columns:
                greenspace[col] = pandas.NA  # Assign missing columns with NaN values
                
        # Keep only the columns that exist
        greenspace = greenspace[desired_columns]
        
        #Display greenspace_data basic information
        #greenspace_data is a GeoDataFrame
        print(greenspace.head())
        print(f"Total greenspaces: {len(greenspace)}")
        print(f"The greenspace data in {place_name} has {len(greenspace.columns)} columns, or attributes, per park")

        return greenspace
    except:
        print(f"No greenspaces found for {place_name}")
        greenspace = None

place_name = 'Phoenix, Arizona'
greenspace_tags = {'leisure': ['park', 'nature_reserve']}
greenspace_data = load_osm_greenspace(place_name, greenspace_tags)