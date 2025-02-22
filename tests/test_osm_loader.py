import unittest
from unittest.mock import patch
import osmnx
import geopandas
import pandas
from shapely.geometry import Point
from shapely.geometry import Polygon
import sys
import os

# Add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from osm_loader import check_boundary
from osm_loader import load_greenspace_data
from osm_loader import process_greenspace_data
from osm_loader import main_load_greenspace


class TestCheckBoundary(unittest.TestCase):
    def test_check_boundary_fail(self):
        """Test invalid OSM boundary return"""
        with patch('osmnx.geocoder.geocode_to_gdf') as mock_geocode:
            mock_geocode.side_effect = "Any error, probably geocode"

            result = check_boundary('Fake Place')

            self.assertFalse(result)

    def test_check_boundary_valid(self):
        with patch('osmnx.geocoder.geocode_to_gdf') as mock_geocode:

            # geocode_to_gdf returns a GeoDataFrame (in a list) which always has a polygon as a 'geometry'
            mock_gdf = geopandas.GeoDataFrame(
                {'geometry': [Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])]},
            )

            # Using known valid boundary
            result = check_boundary('St. Louis, Missouri')

            self.assertTrue(result)


class TestLoadOsmGreenspace(unittest.TestCase):
    def test_load_greenspace_successful(self):
        """Test successful greenspace data loading"""
        with patch('osmnx.features.features_from_place') as mock_features:
            mock_data = geopandas.GeoDataFrame({
                'geometry': [Point(0, 0)],
                'leisure': ['park'],
                'name': ['Test Park']
                })
            
            # Set mock return to defind mock data
            mock_features.return_value = mock_data

            # Run function
            result = load_greenspace_data('Valid Place', {'leisure': ['park']})
            
            # Ensure return is a GeoDataFrame
            self.assertIsInstance(result, geopandas.GeoDataFrame)

            # Ensure necesary parameters were used, specifically which_result
            mock_features.assert_called_once_with('Valid Place', {'leisure': ['park']}, which_result=1)

            # Ensure return is expected length
            self.assertEqual(len(result), 1)

    def test_load_greenspace_no_results(self):
        """ Test response if there is no data found """
        with patch('osmnx.features.features_from_place') as mock_features:
            mock_features.side_effect = osmnx._errors.InsufficientResponseError

            result = load_greenspace_data('No Greenspace Place', {'leisure': ['park']})

            # Ensure return is None if error is InsufficientResponseError
            self.assertIsNone(result)

    def test_load_greenspace_general_error(self):
        """ Test response with general error """
        with patch('osmnx.features.features_from_place') as mock_features:
            # Set the side_effect to raise an exception
            mock_features.side_effect = Exception("Any error response")

            result = load_greenspace_data('No Greenspace Place', {'leisure': ['park']})

            # Ensure return is None if any other error happens
            self.assertIsNone(result)

class TestProcessGreenspaceData(unittest.TestCase):
    def test_process_greenspace_data_normal(self):
        """ 
        Test processing with extra columns as input.
        Expected input (directly from load query) will have several extra columns before being processed. 
        """

        # Create input (all desired columns)
        mock_input = geopandas.GeoDataFrame({
            'geometry': [Point(0, 0)],
            'leisure': ['park'],
            'name': ['Test Park'],
            'addr:city': ['Test City'],
            'addr:county': ['Test County'],
            'addr:state': ['Test State'],
            'extra': ['Test extra column']
            })
        
        # Create expected output
        mock_output = pandas.DataFrame({
            'leisure': ['park'],
            'name': ['Test Park'],
            'addr:city': ['Test City'],
            'addr:county': ['Test County'],
            'addr:state': ['Test State'],
            })
        
        # Run function
        result = process_greenspace_data(mock_input)

        # assertEqual does not work here due to it using booleans
        # Using dataframe "equals" method instead
        self.assertTrue(mock_output.equals(result))

    def test_process_greenspace_data_missing(self):
        """ 
        Test processing with too few columns as input.
        This might happen when there are only a few results and they each are missing data.
        """

        # Create input (missing addr:state)
        mock_input = geopandas.GeoDataFrame({
            'geometry': [Point(0, 0)],
            'leisure': ['park'],
            'name': ['Test Park'],
            'addr:city': ['Test City'],
            'addr:county': ['Test County'],
            })
        
        # Create expected output with pandas.NA as missing column
        mock_output = pandas.DataFrame({
            'leisure': ['park'],
            'name': ['Test Park'],
            'addr:city': ['Test City'],
            'addr:county': ['Test County'],
            'addr:state': [pandas.NA], 
            })
    
        result = process_greenspace_data(mock_input)

        # assertEqual does not work here due to it using booleans
        # Using dataframe "equals" method instead
        self.assertTrue(mock_output.equals(result))
        

# Run the unittests when this file is run directly
if __name__ == '__main__':
    print("Test script is running")  
    unittest.main(verbosity=2) # More detailed output