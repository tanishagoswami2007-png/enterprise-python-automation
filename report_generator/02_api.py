import requests

API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def fetch_bitcoin_data() -> dict:
    """Fetch current Bitcoin price data from a public API."""
    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()
    return response.json()
