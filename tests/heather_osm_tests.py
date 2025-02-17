conda init bash
conda activate greenspace_env
import unittest
from unittest.mock import patch
import osmnx
import geopandas
import pandas
from shapely.geometry import Point
import sys
import os

# Add parent directory to Python path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname('C:\Users\hatot\OneDrive\Desktop\502-Project' , '..'))))
current_dir = os.path.dirname(os.path.abspath(r"C:\Users\hatot\OneDrive\Desktop\502-Project"))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from osm_loader import check_boundary
from osm_loader import load_greenspace_data
from osm_loader import process_greenspace_data
from osm_loader import main_load_greenspace

class TestProcessOsmGreenspaceData(unittest.TestCase):
    def test_process_greenspace_data_successful(self):
        """Test successful greenspace data processing"""
        with patch('osmnx.features.features_from_place') as mock_features:
            mock_data = geopandas.GeoDataFrame({
                'geometry': [Point(0, 0)],
            })
            # Set mock return to defined mock data
            mock_features.return_value = mock_data
            # Run function
            result = load_greenspace_data('Valid Place', {'leisure': ['park']})
            # Ensure the returned value is a GeoDataFram
            self.assertIsDataFrame(result, geopandas.GeoDataFrame)
            # Ensure required paramaters were used
            mock_features.assert_called_once_with('Valid Place', which_result=1
                                                 )
            #Ensure return is expected length
            self.assertEqual(len(result), 1)