import os
import requests
from dotenv import load_dotenv

load_dotenv()
YAHOO_CLIENT_ID = os.getenv("YAHOO_CLIENT_ID")
YAHOO_CLIENT_SECRET = os.getenv("YAHOO_CLIENT_SECRET")
YAHOO_REFRESH_TOKEN = os.getenv("YAHOO_REFRESH_TOKEN")
LEAGUE_KEY = os.getenv("LEAGUE_KEY")
def refresh_access_token():
    url = "https://api.login.yahoo.com/oauth2/get_token"
    data = {
        "client_id": YAHOO_CLIENT_ID,
        "client_secret": YAHOO_CLIENT_SECRET,
        "redirect_uri": "http://localhost/",
        "refresh_token": YAHOO_REFRESH_TOKEN,
        "grant_type": "refresh_token",
    }
    r = requests.post(url, data=data)
    r.raise_for_status()
    return r.json()["access_token"]

def get_transactions(access_token, league_key=LEAGUE_KEY):
    url = f"https://fantasysports.yahooapis.com/fantasy/v2/league/{league_key}/transactions"
    headers = {"Authorization": f"Bearer {access_token}", "Accept": "application/xml"}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.text