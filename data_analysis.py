# Import required modules
import csv
import numpy
from cdc_loader import load_cdc_places
from osm_loader import main_load_greenspace

place_name = 'St. Louis County, Missouri'
greenspace_tags = {'leisure': ['park', 'nature_reserve', 'garden']}
greenspace_data = main_load_greenspace(place_name, greenspace_tags)

state_abbr = 'MO'
cdc_data_for_analysis = load_cdc_places(county_name, state_abbr)
print(cdc_data_for_analysis)
osm_data_for_analysis = main_load_greenspace(place_name, greenspace_tags)
print(osm_data_for_analysis)

# Need to convert greenspace data to a score to correlate with CDC Depression score

# Correlation Analysis
x = numpy.array([1, 2, 3, 4, 5])
y = numpy.array([2, 4, 5, 4, 5])
correlation_coefficient = numpy.corrcoef(x, y)[0, 1]
print(correlation_coefficient)
# 0.7745966692414834

# So, for our correlation analysis, we need arrays of equal size
# Data Matrix: County, State, Depression_Value, Greenspace_Value
# Calculate numpy.corrcoef(Depression_Value, Greenspace_Value)[0, 1]
correlation_coefficient = numpy.corrcoef(Data_Value, leisure_counts)
print(correlation_coefficient)
