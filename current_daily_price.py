import requests
import pandas as pd

def get_place_data(place_name):
    url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
    api_key = "579b464db66ec23bdd000001a6ceed09051b4845418ca7480ea0991d"

    params = {
        "api-key": api_key,
        "format": "json",
        "limit": 10000
    }

    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data["records"])
    filtered_df = df[df.apply(lambda row: place_name.lower() in str(row.values).lower(), axis=1)]

    if filtered_df.empty:
        print(f"No records found for '{place_name}'.")
        return None
    else:
        print(f"✅ Found {len(filtered_df)} records for '{place_name}':\n")
        print(filtered_df)
        return filtered_df

# Example call
get_place_data("harippad")
