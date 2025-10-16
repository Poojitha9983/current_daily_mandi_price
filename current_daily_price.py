# VS code - Adding "commodities" in passing parameters

import requests
import pandas as pd
import os

def get_place_data(place_name, commodity_name):
    """
    User-defined function that takes place_name and commodity_name as parameters
    and returns related records from the API.
    """
    # API details
    url = "YOUR_URL_data.gov"
    api_key = "YOUR_API_KEY_FOR_data.gov"

    params = {
    "api-key": api_key,
    "format": "json",
    "limit": 10000,
    "filters[market]": place_name,       
    "filters[commodity]": commodity_name  
}


    # Fetch data
    response = requests.get(url, params=params)
    print(response)

    if response.status_code != 200:
        print("Error fetching data from API!")
        return None

    data = response.json()

    # Convert JSON → DataFrame
    df = pd.DataFrame(data["records"])

   
    # Show result
    if df.empty:
        print(f"No records found for market '{place_name}' and commodity '{commodity_name}'.")
        return None
    else:
        print(f"Found {len(df)} records for market '{place_name}' and commodity '{commodity_name}':\n")
        print(df)
        return df


# User input
if __name__ == "__main__":
    user_place = input("Enter Place Name : ")
    user_commodity = input("Enter Commodity Name : ")
    get_place_data(user_place, user_commodity)


