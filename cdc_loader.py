#Import required modules
import requests
import pandas

county_name = 'St. Louis'
state_abbr = 'MO'

# To do: Add location verification function

# Load PLACES data using county/state definition & Measure ID (default: depression)
def load_cdc_data(county_name, state_abbr, measure_id='DEPRESSION', limit=5000):
    """
    Load CDC PLACES data for a specific county (locationname) and 2-letter state abbeviation.
    
    Args:
        county_name (str): Name of county being retrieved
        state_abbr (str): 2-letter state abbreviation
        measure_id (str): CDC measure ID (default: DEPRESSION)
        limit (int): Maximum number of records to return (default: 5000)

    Returns:
        pandas.DataFrame: CDC PLACES data with columns:
            year, stateabbr, locationname, measureid, data_value,
            low_confidence_limit, high_confidence_limit, totalpopulation
        None: If error occurs

    Source:
        https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb
    """
    try:
        # Define the API URL and columns to retrieve
        base_url = "https://data.cdc.gov/resource/swc5-untb.json"
        columns = [
            "year", "stateabbr", "locationname", "measureid", "data_value",
            "low_confidence_limit", "high_confidence_limit", "totalpopulation"
        ]
        select_clause = ", ".join(columns)
        
        # Build query parameters
        where_clause = f"stateabbr='{state_abbr}' AND measureid='{measure_id}' AND locationname LIKE '%{county_name}%'"
        params = {
            "$select": select_clause,
            "$where": where_clause,
            "$limit": limit
        }
        
        # Get data from API
        response = requests.get(base_url, params=params)
        print("\nRetrieving CDC PLACES data...")

        # Check for HTTP request
        response.raise_for_status()
        
        # Convert to DataFrame
        cdc_data = pandas.DataFrame(response.json())
        print("Successfully retrieved CDC data")
        return cdc_data
        
    except Exception as e:
        print("\nError retrieving data")
        return None

# To do: Process data
    
# To do: Add `main` function to handle all three functions

# Runs only when executed directly, not when referenced in other scripts
if __name__ == "__main__":
    load_cdc_data(state_abbr, county_name)
