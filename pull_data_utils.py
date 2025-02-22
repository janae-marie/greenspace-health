import json
import requests


####################
# GLOBAL CONSTANTS #
####################
# API endpoint for querying the dataset
_URL = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/georef-united-states-of-america-county/records"

# Output file for the state county dictionary
_OUTPUT_FILE = "state_county_dict.json"

# Dictionary of state names to abbreviations
_STATE_NAME_ABBR_DICT = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY"
}


def state_name_to_abbr(name):
    """
    Converts a state name to an abbreviation
    Raises a KeyError if the input is not a valid state name
    """
    return _STATE_NAME_ABBR_DICT[name]


def get_all_counties_in_state(state_name):
    """
    Returns a list of all counties in a given state
    Returns None if there was a failure
    """
    # API limits to 100 records per request so we will use an offset counter and make multiple requests
    def _call_wrapper(url, params):
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return None
        return response.json()

    def _county_result_to_list(response):
        return [x['county'][0] for x in response['results']]
    offset = 0
    limit = 100
    params = {
        "select": "coty_name as county",
        "where": f"ste_name='{state_name}' AND coty_type = 'county'",
        "format": "json",
        "order_by": "county ASC",
        "limit": limit,
        "offset": offset
    }
    response = _call_wrapper(_URL, params)
    if response is None:
        return None
    data = _county_result_to_list(response)
    number_of_counties = response["total_count"]
    if number_of_counties > limit:
        # number of records exceeds the limit, make additional requests
        while offset < number_of_counties:
            offset += limit
            params["offset"] = offset
            response = _call_wrapper(_URL, params)
            if response is None:
                return None
            data.extend(_county_result_to_list(response))
    return data


def generate_state_county_dict():
    """
    Generates a dictionary of states to counties
    Returns None if there was a failure
    """
    state_county_dict = {}
    for state_name in _STATE_NAME_ABBR_DICT.keys():
        counties = get_all_counties_in_state(state_name)
        if counties is None:
            return None
        state_county_dict[state_name] = counties
    return state_county_dict


def load_data_from_disk():
    """
    Loads the state county dictionary from JSON file on disk
    Returns None if there was a failure
    """
    try:
        with open(_OUTPUT_FILE, "rb") as f:
            state_county_dict = json.load(f)
    except FileNotFoundError:
        return None
    return state_county_dict


def main():
    state_county_dict = generate_state_county_dict()
    if state_county_dict is None:
        print("Failed to generate state county dictionary")
        return
    with open(_OUTPUT_FILE, "w") as f:
        json.dump(state_county_dict, f)
    print(f"State county dictionary saved to {_OUTPUT_FILE}")
    return


if __name__ == '__main__':
    main()