#Import required modules
import requests
import pandas
import geopandas
from pull_data_utils import load_data_from_disk
from pull_data_utils import state_name_to_abbr


def load_cdc_places(county_name, state_abbr, measure_id='DEPRESSION'):
    print("State:", state_abbr, "County:", county_name, "Depression Score:", measure_id)
    
    
def main():
    data = load_data_from_disk()
    if data is None:
        print("[ERROR] Could not load data from disk")
        return

    # only log LIMIT counties per state
    LIMIT = 5
    for state, counties in iter(data.items()):
        for i, county in enumerate(counties):
            load_cdc_places(county, state_name_to_abbr(state), measure_id)
            if i > LIMIT:
                break
    return


if __name__ == '__main__':
    main()

'''
#Load PLACES data using county/state definition & Measure ID (default: depression)
def load_cdc_places(county_name, state_abbr, measure_id='DEPRESSION', limit=5000):
    try:
        # Define the API URL
        base_url = "https://chronicdata.cdc.gov/resource/cwsq-ngmh.json"

        #Query parameters: Filter by county and state. Only gather relevant columns.
        params = {
            "$select": "year, stateabbr as StateId, countyname as CountyName, data_value as Data_Value, "
                "low_confidence_limit as Low_Confidence_Limit, high_confidence_limit as High_Confidence_Limit, "
                "totalpop18plus as TotalPop18plus, measureid",
            "$where": f"measureid='DEPRESSION' AND stateabbr='{state_abbr}' AND countyname='{county_name}'",
            "$limit": limit
        }

        # Send request to the API
        response = requests.get(base_url, params=params)

        #Turn format into DataFrame
        cdc_data = pandas.DataFrame(response.json())

        #Display basic information
        print(cdc_data.head())
        print(f"Total rows: {len(cdc_data)}")
        print(f"The CDC data in {county_name}, {state_abbr} has {len(cdc_data.columns)} columns")
        
    except:
        print(f"Error retrieving data for {county_name}, {state_abbr}")


county_name = 'Maricopa'
state_abbr = 'AZ'
cdc_data = load_cdc_places(county_name, state_abbr)
'''