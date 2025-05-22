import requests
from typing import Dict, Optional
import os
from dotenv import load_dotenv

class PirschClient:
    def __init__(self, client_id: str, client_secret: str, base_url: str = "https://api.pirsch.io"):
        """
        Initialize the Pirsch client with client credentials.
        
        :param client_id: Your Pirsch client ID.
        :param client_secret: Your Pirsch client secret.
        :param base_url: Base URL of the Pirsch API (default is https://api.pirsch.io).
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.token = None

    def authenticate(self) -> None:
        """
        Obtain an access token from the Pirsch API.
        """
        url = f"{self.base_url}/api/v1/token"
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error if the request fails
        self.token = response.json().get("access_token")
        if not self.token:
            raise ValueError("Failed to obtain access token.")

    def request(self, endpoint: str, method: str = "GET", params: Optional[Dict] = None, data: Optional[Dict] = None) -> Dict:
        """
        Make an authenticated request to the Pirsch API.

        :param endpoint: API endpoint (e.g., "/api/v1/stats").
        :param method: HTTP method (default is "GET").
        :param params: URL parameters (optional).
        :param data: Request body for POST/PUT requests (optional).
        :return: Parsed JSON response as a dictionary.
        """
        if not self.token:
            raise ValueError("Client is not authenticated. Call authenticate() first.")

        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.request(method, url, headers=headers, params=params, json=data)
        response.raise_for_status()  # Raise an error for non-2xx responses
        return response.json()

# Example usage:
if __name__ == "__main__":
    load_dotenv()
    # Replace with your client credentials
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    BLOG_STATS_ID = os.getenv('BLOG_STATS_ID_PF')

    pirsch = PirschClient(CLIENT_ID, CLIENT_SECRET)

    try:
        # Authenticate the client
        pirsch.authenticate()

        # Example: Fetching stats (modify endpoint as needed)
        stats = pirsch.request("/api/v1/statistics/page/", params={"from": "2024-11-24","to": "2024-11-24", "id": BLOG_STATS_ID, "tz": "Europe/Berlin"})
        print("Stats:")
        for entry in stats:
            print(f"{entry['path']} \t {entry['views']} \t {entry['visitors']}")
    except Exception as e:
        print("Error:", e)
