# Import required modules
import csv
import numpy
from cdc_loader import load_cdc_data
from osm_loader import main_load_greenspace

# Load greenspace
place_name = 'St. Louis County, Missouri'
greenspace_tags = {'leisure': ['park', 'nature_reserve', 'garden']}
osm_data_for_analysis = main_load_greenspace(place_name, greenspace_tags)
print(osm_data_for_analysis)
# Run again for 'Laramie County, Wyoming'

# Load CDC data
state_abbr = 'MO'
county_name = 'St. Louis'
cdc_data_for_analysis = load_cdc_data(county_name, state_abbr, measure_id)
print(cdc_data_for_analysis)
# Run again for 'Laramie, WY'


# Need to convert greenspace data to a score to correlate with CDC Depression score

# Correlation Analysis
depression_values = numpy.array([24.1, 22.1, 20.5])
# Depression values for St. Louis County MO, Laramie County WY, and Polk County IA
greenspace_values = numpy.array([652, 127, 4288])
# Greenspace counts for St. Louis County MO, Laramie County WY, and Polk County IA

correlation_coefficient = numpy.corrcoef(depression_values, greenspace_values)[0, 1]
print(correlation_coefficient)
# -0.7624134017970408

