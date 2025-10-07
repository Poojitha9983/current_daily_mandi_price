#VS code
import requests
import pandas as pd
import os

def get_place_data(place_name):
    """
    User-defined function that takes a place name as parameter 
    and returns related records from the API. Also saves to CSV.
    """
    # API details
    url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
    api_key = "579b464db66ec23bdd000001a6ceed09051b4845418ca7480ea0991d"

    params = {
        "api-key": api_key,
        "format": "json",
        "limit": 10000
    }

    # Fetch data
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print("Error fetching data from API!")
        return None

    data = response.json()

    # Convert JSON → DataFrame
    df = pd.DataFrame(data["records"])

    # Filter rows containing place name in any column
    filtered_df = df[df.apply(lambda row: place_name.lower() in str(row.values).lower(), axis=1)]

    # Show result
    if filtered_df.empty:
        print(f"No records found for '{place_name}'.")
        return None
    else:
        print(f"✅ Found {len(filtered_df)} records for '{place_name}':\n")
        print(filtered_df)
        return filtered_df


# ------------------------------
# User input
if __name__ == "__main__":
    user_place = input("Enter Place Name: ")
    get_place_data(user_place)

