# :construction: Greenspace accessibility & depression rates :construction:
🏗️ _This project is still being built_

Does greenspace access correlate with reported depression statistics across different counties or areas of a city?

This is a simple project to gather data from [OpenStreetMap](https://www.openstreetmap.org/#map=5/38.01/-95.84) and [CDC PLACES](https://www.cdc.gov/places/index.html)'s [2024 Local Data for Better Health](https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb/about_data) to see if there is a basic correlation between greenspaces and clinical depression rates. We hope that it can be used for various places to analyze this relationship across the U.S. For now, it can handle analyzing one place at a time.

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

## Run the code-TBD

### How do you define a "place"?-TBD

Before you run the code, it's important to choose the place you want to analyze. CDC Data is at the County level, while OSM data uses geometry (via GeoDataFrames) to define places. We've defaulted this project to use the _enter place here_ place. It is managed in the _file name?)_ file. 

> [!WARNING]
> Places may not line up correctly due to this varying grain definition. We recommend reviewing both data sets before trying to run this code.
> 
> The OSM loader, when run, will tell you if the place you entered is a valid boundary or not.
> 
> The CDC loader, when run, will tell you self-reported depression levels among adults over age 18 by the place you entered.
> 
> **No code in this project will verify the places chosen are the same. This must be done manually before running this project.**


## Running tests

## I want to contribute!-TBD

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

# License - MIT (see license.txt)

