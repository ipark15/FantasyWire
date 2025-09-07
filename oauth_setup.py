from requests_oauthlib import OAuth2Session

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = ""  

AUTH_BASE_URL = "https://api.login.yahoo.com/oauth2/request_auth"
TOKEN_URL = "https://api.login.yahoo.com/oauth2/get_token"

yahoo = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
authorization_url, state = yahoo.authorization_url(AUTH_BASE_URL)
print("Go to this URL and authorize:", authorization_url)

redirect_response = input("Paste the full redirect URL you got after login: ")

token = yahoo.fetch_token(
    TOKEN_URL,
    client_secret=CLIENT_SECRET,
    authorization_response=redirect_response,
)

print("Access token:", token["access_token"])
print("Refresh token:", token["refresh_token"])
