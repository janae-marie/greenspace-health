This is the group project for CAS502, which includes Janae Thomson and Heather Tottingham. 

# Greenspace accessibility & health
## Project Overview

Does greenspace access correlate with reported mental health statistics across different neighborhoods or areas of a city?

Utilizing open-source data sets, we aim to analyze what “access” to greenspace might mean for city residents, including distance, greenspace type, and public access designations. Then, we will utilize mental health statistics to see if and how these correlate to access types. We hope to visualize these correlations.

## Data Sources and Definitions
### OpenStreetMap
- Utilizing osmnx package to load greenspace, defaulted to "park" and "nature reserve" designations
#### Citation
Boeing, G. (2024). Modeling and Analyzing Urban Networks and Amenities with OSMnx. Working paper. https://geoffboeing.com/publications/osmnx-paper/
#### License
OSMnx is open source and licensed under the MIT license. OpenStreetMap’s open data license: https://www.openstreetmap.org/copyright 
### CDC PLACES

## Project Plan
### Challenges
- Heather is new to GitHub, version control systems, and writing code in collaboration with others.
- Janae is more novice at data analysis and quality control over the analysis.

### Collaboration: 
- Direct messages via Slack as primary interaction.
- GitHub feature branching
  + Utilize feature branching where each person will work on certain functionality within a branch. We may collaborate on the same branch for the same functionality (i.e. an issue at a time).
  + familiarize with workflow
  + review each other's code via pull requests to better collaborate and create a cohesive product

  # Environment set-up
  To recreate the environment, ensure Conda is installed on your computer, and run
  - conda env create -f environment.yml
  - conda activate greenspace_env

  ## Dependencies
  - osmnx--2.0.1 Note that osmnx, geopandas, and matplotlib do not have versions specified. 
