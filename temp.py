import requests

TOKEN_URL = "https://public-api.wordpress.com/oauth2/token"

data = {
    "client_id": "121947",
    "client_secret": "n8t9z7qwmzeMuxWYBcg2KVobNDLoZI95mZIRzPwa6HfPwzuPVc05xvzzhnrZQKEI",
    "redirect_uri": "https://localhost",
    "grant_type": "authorization_code",
    "code": ""
}

response = requests.post(TOKEN_URL, data=data)

if response.status_code == 200:
    token_info = response.json()
    print("✅ Access Token:", token_info['access_token'])
else:
    print("❌ Failed to get token:", response.status_code)
    print(response.text)
