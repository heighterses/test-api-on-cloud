# 🌐 Flask API Documentation

This Flask API is hosted on Azure App Service and managed in API Management Services on Azure with  Subscription KEY 🔑

## 🚀 Endpoint

The API can be accessed at the following endpoint:

- **Base URL:** [https://api-tetsing.azure-api.net](https://api-tetsing.azure-api.net)

## 🛠️ Test Endpoint

To test the API, you can append specific paths to the base URL. Here's an example test endpoint:

- **Test Path:** [https://api-tetsing.azure-api.net/test](https://api-tetsing.azure-api.net/test)

## ❌ Error Handling

The API includes error handling to provide meaningful responses in case of invalid requests or internal server errors.

## 💻 How to Use

To use the API in your application, you can make HTTP requests using any programming language or tool that supports HTTP requests. Below is an example using Python's `requests` library:

```python
import requests

# Input the path after the slash
url_val = input("Input after slash: ")
api_url = f"https://api-tetsing.azure-api.net/{url_val}"

# Replace 'FIND_IT_ON_GITHUB_REPO' with your actual API key
key = "FIND_IT_ON_GITHUB_REPO"
headers = {
    "test-key-name": key
}

response = requests.get(api_url, headers=headers)
print(response.json())
