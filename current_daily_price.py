import requests
import pandas as pd

def get_state_data():
    # Step 1: Take user input
    state_name = input("Enter State Name: ")

    # Step 2: API endpoint
    url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
    
    # Step 3: API key (demo key, replace with your own if you have)
    api_key = "579b464db66ec23bdd000001a6ceed09051b4845418ca7480ea0991d"
    
    # Step 4: Request parameters
    params = {
        "api-key": api_key,
        "format": "json",
        "limit": 10000
    }
    
    # Step 5: Fetch data from API
    response = requests.get(url, params=params)
    data = response.json()
    
    # Step 6: Convert JSON → Pandas DataFrame
    df = pd.DataFrame(data["records"])
    
    # Step 7: Filter rows only for the state
    filtered_df = df[df['state'].str.lower() == state_name.lower()]
    
    # Step 8: Show result
    if filtered_df.empty:
        print(f"No records found for state '{state_name}'.")
        return None
    else:
        print(f"✅ Found {len(filtered_df)} records for state '{state_name}':\n")
        print(filtered_df.head())   # show first 5 rows
        return filtered_df

# Run function (user will be prompted to type state name)
get_state_data()
