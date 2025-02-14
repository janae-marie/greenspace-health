# Import required modules
import csv
from cdc_loader import load_cdc_places
from osm_loader import load_osm_greenspace

# Open the file in write mode
with open(csv_file_path, mode='w', newline='') as file:
    # Create a csv.writer object
    writer = csv.writer(file)
    # Write data to the CSV file
    writer.writerows(data)

# Write a loop to go through each unique county/state listing, use that as place_name
# for(county in cdc_data)
# problem with above: there is a Park County in both WY & MT, etc. Need to iterate through both county and state simultaneously
place_name = 'Maricopa County, Arizona'
greenspace_tags = {'leisure': ['park', 'nature_reserve']}
greenspace_data = load_osm_greenspace(place_name, greenspace_tags)

county_name = str.split(place_name)[0] # should be first word in place_name
# Two-letter state abbreviations: https://www.faa.gov/air_traffic/publications/atpubs/cnt_html/appendix_a.html
state_abbr = 'AZ' # Use website above to assign state_abbr from state name
cdc_data = load_cdc_places(county_name, state_abbr)

# Data for CSV File
# Need to combine CDC Data and Greenspace Data into one
data = cdc_data
# File path for the CSV file
csv_file_path = 'data.csv'

# Correlation Analysis
x = numpy.array([1, 2, 3, 4, 5])
y = numpy.array([2, 4, 5, 4, 5])
correlation_coefficient = numpy.corrcoef(x, y)[0, 1]
print(correlation_coefficient)
# 0.7745966692414834

# So, for our correlation analysis, we need arrays of equal size
# Data Matrix: County, State, Depression_Value, Greenspace_Value
# Calculate numpy.corrcoef(Depression_Value, Greenspace_Value)[0, 1]

