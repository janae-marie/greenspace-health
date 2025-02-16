import unittest
from unittest.mock import patch
import osmnx
import geopandas
import pandas
from shapely.geometry import Point
import sys
import os

# Add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from osm_loader import check_boundary
from osm_loader import load_greenspace_data
from osm_loader import process_greenspace_data
from osm_loader import main_load_greenspace

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
            result = load_greenspace_data('Valid City', {'leisure': ['park']})
            
            # Ensure return is a GeoDataFrame
            self.assertIsInstance(result, geopandas.GeoDataFrame)

            # Ensure necesary parameters were used, specifically which_result
            mock_features.assert_called_once_with('Valid City', {'leisure': ['park']}, which_result=1)

            # Ensure return is expected length
            self.assertEqual(len(result), 1)

# Run the unittests when this file is run directly
if __name__ == '__main__':
    print("Test script is running")  
    unittest.main(verbosity=2) # More detailed output