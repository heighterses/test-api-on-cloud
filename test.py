import requests

# API KEY --> 7199a1296d944cd5b294117f513b66a4

url_val = input("input after slash: ")
api_url = f"https://api-tetsing.azure-api.net/{url_val}"
key = "FIND_IT_ON_GITHUB_REPO" 
headers = {
    "test-key-name": key
}

response = requests.get(api_url, headers=headers)
print(response.json())
