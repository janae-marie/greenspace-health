import osmnx
import geopandas
import pandas

# Define variables
place_name = 'St. Louis, Missouri'

greenspace_tags = {
    'leisure': ['park', 'nature_reserve']
}

def check_boundary(place_name):
    """
    Check if a place has a valid boundary in OpenStreetMap.

    Args:
        place_name (str): Name of place being checked

    Returns: 
        None: This is a validation function

    Raises: 
        Boundary error: if osmnx does not recoginize place as having a valid boundary via geocoder
    
    """
    try:
        # Attepmt finding geocode for the requested place
        area = osmnx.geocoder.geocode_to_gdf(place_name)
        print(f"Found boundary of type: {type(area.geometry.iloc[0])}")
        return True
    except Exception as boundary_error:
        # If error, suggest a known place with valid boundary
        print(f"Boundary error: {str(boundary_error)}")
        print("Suggestion: Try a different place name like: 'St. Louis, Missouri'")
        return False

def load_greenspace_data(place_name, tags):
    """
    Load greenspace features for a given place.
    
    Args:
        place_name (str): Name of place being retrieved from osmnx
        tags (list): List of tags to filter query

    Returns:
        geopandas.GeoDataFrame: Geometry (required for all GeoDataFrames)
            Tagged columns dependent on `tags`
        None: If no features were found or if error occurs

    Raises:
        No exceptions are raised, errors will return `None`
    """
    try:
        # which_result stops osmnx from searching all possible places and returns only first result.
        # Needed for loading well.
        greenspace = osmnx.features.features_from_place(place_name, tags, which_result=1)
        print("Successfully retrieved features")
        return greenspace
    except osmnx._errors.InsufficientResponseError:
        print("No greenspace features found in this area")
        return None
    except Exception as feature_error:
        print(f"Error getting features: {str(feature_error)}")
        return None
  
def process_greenspace_data(greenspace):
    """
    Process the greenspace data.
    
    Args:
        greenspace (geopandas.GeoDataFrame): Response from osmnx
    
    Returns:
        pandas.DataFrame : Cleaned DataFrame with desired columns of 
            'leisure', 'name', 'addr:city', 'addr:county', 'addr:state', 'type'
            All columns will exist with pandas.NA for missing values
        None if input is empty or if error occurs during processing

    Raises:
        No exceptions are raised, errors will return `None`
    """
    if greenspace is None:
        return None
        
    try:
        desired_columns = ['leisure', 'name', 'addr:city', 'addr:county', 'addr:state', 'type']
        
        # Ensure data is always uniform by adding NA if no data is returned for a column. 
        # This is common for places with little data.
        for col in desired_columns:
            if col not in greenspace.columns:
                greenspace[col] = pandas.NA

        # Only selects the desired_columns, in that order.
        # Because there is no "geometry" in the columns, the data frame is now pandas.DataFrame       
        greenspace = greenspace[desired_columns]
        
        print("\nResults:")
        print(f"Found {len(greenspace)} greenspaces")
        print(f"Columns: {', '.join(greenspace.columns)}")
        print(f"Data type: {type(greenspace)}")
        
        return greenspace
        
    except Exception as e:
        print(f"Error processing data: {str(e)}")
        return None
        

def main_load_greenspace(place_name, tags):
    """
    Main function to load, process, and analyze greenspace data.
    
    Args:
        place_name (str): Name of place being retrieved from osmnx
        tags (list): List of tags to filter query

    Returns:
        pandas.DataFrame : Cleaned greenpace data. See `process_greenspace_data` function.

    Raises:
        No exception raised
    
    """
    # Step 1: Check boundary
    print(f"Step 1: Checking boundary for {place_name}...")

    # To Do: break this down a bit more
    if not check_boundary(place_name):
        return None

    # Step 2: Load data
    print(f"\nStep 2: Loading greenspace data...")
    unprocessed_greenspace = load_greenspace_data(place_name, tags)
    if unprocessed_greenspace is None:
        return None

    # Step 3: Process data
    print("\nStep 3: Processing data...")
    greenspace_data = process_greenspace_data(unprocessed_greenspace)
    
    # Step 4: If we have data, show additional info
    if greenspace_data is not None:
        # Display unique values in 'leisure' column
        print("\nUnique values in leisure column:")
        print(greenspace_data['leisure'].unique()) 
        
        # Show the count for each unique value
        leisure_counts = greenspace_data['leisure'].value_counts()
        print("\nCounts by type:")
        print(leisure_counts)

    return greenspace_data

# Runs only when executed directly, not when referenced in other scripts
if __name__ == "__main__":
    main_load_greenspace(place_name, greenspace_tags)
