# consume.py
import requests

# Make a GET request to retrieve drinks data from the API.
response = requests.get('http://127.0.0.1:8000/drinks')
print(response.json())

# print("Testing")