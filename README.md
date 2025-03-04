# :construction: Greenspace accessibility & depression rates :construction:
🏗️ _This project has partial functionality and will not be maintained by its creators._

Does greenspace access correlate with reported depression statistics across different counties or areas of a city?

This is a simple project to gather data from [OpenStreetMap](https://www.openstreetmap.org/#map=5/38.01/-95.84) and [CDC PLACES](https://www.cdc.gov/places/index.html)'s [2024 Local Data for Better Health](https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb/about_data) to see if there is a basic correlation between greenspaces and clinical depression rates. We hope that it can be used for various places to analyze this relationship across the U.S. For now, it can handle analyzing one place at a time. Specifically, we use St. Louis county, MO as it has a small geographical area which lends itself well to loading OSM data. There is also a hard-coded correlation coefficient created as an output as a placeholder for future functionality. This number is an analysis of St. Louis County MO, Laramie County WY, and Polk County IA.

Janae Thomson and Heather Tottingham built this for a group project for Complex Adaptive Systems 502 offered through Arizona State University.

> [!TIP]
> Greenspaces are publically available nature spaces. For this project, we are defaulting the definition to OSM's `leisure` values of *park*, *nature reserve*, and *garden*. 

# How to use the project
## Install
1. Install the prerequisites
  - Python 3.1
  - Conda package manager
  - Git
2. Clone the repository using Git
3. Set up the Conda environment*
  - Using bash, create the environment: `conda env create -f environment.yml`
  - Activate it: `conda activate greenspace_env`

*All prerequisites are outlined in the environment.yml file. This will be handled by the conda package manager! 

## Run the code 

### How do you define a "place"?

Before you run the code, it's important to choose the place you want to analyze. CDC Data is at the County level, while OSM data uses geometry (via GeoDataFrames) to define places. 

We've defaulted this project to use the St. Louis county, MO place within the data loader functions. 

OSM data allows a reader-friendly format to query, such as "St. Louis County, Missouri" and CDC data requires a 2-letter state abbreviation and separate county name, e.g. `state_abbr = 'MO' county_name = 'St. Louis'`.  This is defined in the `data_analysis.py` file and can be altered at the top of the file to try different places. If it is not altered here, the functions will default to St. Louis County.

> [!WARNING]
> Places may not line up correctly due to this varying grain definition. We recommend reviewing both data sets before trying to run these scripts.
> 
> The OSM loader, when run, will tell you if the place you entered is a valid boundary or not.
> 
> We recommend using the CDC's online [data query](https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb/about_data) (Actions > Query data) to check their valid places. The CDC loader, when run, will tell you self-reported depression levels among adults over age 18 by the place you entered.
> 
> **No code in this project will verify the places chosen are the same. This must be done manually before running this project (for now!).**

1. Choose the place you'd like to analyze and enter it into the data_analysis.py file where the variables are defined.
2. Run the data_analysis.py script. The script will:
  - Load the OSM greenspace data from the osm_loader
  - Load the CDC depression data from the cdc_loader
  - Analyze potential correlations
3. Repeat!

## Running tests

This project has a few unit tests, specifically covering the osm_loader functionality. See: [out of scope for now](#out-of-scope-for-now). 

To run these tests, ensure you are in the root directory and run a command in bash for each test file. For example: `python -m unittest tests/test_osm_loader.py`. All tests are in the `/tests` directory.

# Data Sources and Definitions
## OpenStreetMap
This project utilizes the [osmnx package](https://osmnx.readthedocs.io/en/stable/) to load greenspace, defaulted to "park", "nature reserve", and "garden" designations.

**Citation**

Boeing, G. (2024). Modeling and Analyzing Urban Networks and Amenities with OSMnx. Working paper. https://geoffboeing.com/publications/osmnx-paper/

**License**

OSMnx is open source and licensed under the MIT license. OpenStreetMap’s open data license: https://www.openstreetmap.org/copyright

## CDC PLACES
To find the mental health statistics, we utilized the [CDC PLACES](https://www.cdc.gov/places/index.html)'s 2024 [Local Data for Better Health](https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb/about_data) dataset. Specifically:
- YEAR
- StateAbbr
- LocationName
- Data_Value
- Low_Confidence_Limit
- High_Confidence_Limit
- TotalPop18plus
- MeasureId = DEPRESSION

This gives us a subset of the data with the prevalence value of depression among adults by year, state, and county, with the lower and upper confidence interval values.

**Citation**

Centers for Disease Control and Prevention. PLACES: Local Data for Better Health. https://www.cdc.gov/places

**License**

PLACES data is public domain data. See: https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb/about_data

# Out of scope for now

Several features of this project were not able to be a part of the first version due to time and ability. These include:
- Location verification and further modularization of the cdc_loader.py file
- Location management (handling the inherently mismatched grain sizes of the data sources)
- Location as user input handling
- Multiple location analyses at once
- Multiple MeasureID analysis
- Full unit test coverage

## We'd love contributions!

As you can see, this project is a work in progress. If you'd like to contribute, please fork the repository, add a feature branch, commit, and open a pull request.

If you find a bug or would like to suggest a feature update, please utilize this repository's Issues by adding an Issue with enough description.

Please ensure your contributions meet the existing style, include unit test coverage, and are documented properly.

# License - MIT (see license.txt)

