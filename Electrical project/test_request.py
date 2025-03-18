import requests

# API endpoint
url = "http://127.0.0.1:5001/predict"

# Input features (Modify as needed)
data = {
    "features": [14.96, 41.76, 1024.07, 73.17]
}

# Send POST request
response = requests.post(url, json=data)

# Print the response
print("Response JSON:", response.json())  
