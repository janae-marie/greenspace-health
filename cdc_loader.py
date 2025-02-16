#Import required modules
import requests
import pandas
import geopandas
#Call R from Python
import rpy2.robjects as robjects
#Test that R has been imported
robjects.f("print('Hello from R!')")
#Create an R object
r_vector = robjects.StrVector(["a" ,"b", "c"])
print(r_vector)

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