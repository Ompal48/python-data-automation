import requests
import json
from config import API_URL, API_PARAMS, RAW_DATA_FILE

def fetch_crypto_data():
    """
    Fetches cryptocurrency data from CoinGecko API.
    Saves raw data to JSON file and returns parsed data.
    """
    try:
        response = requests.get(API_URL, params=API_PARAMS)
        response.raise_for_status()  # Raise an error for bad status codes

        # Save raw data to file
        with open(RAW_DATA_FILE, 'w') as f:
            json.dump(response.json(), f, indent=4)

        print("Raw data saved to data/raw.json")
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None
