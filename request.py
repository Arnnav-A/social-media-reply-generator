import requests

# API URL
url = "http://localhost:8000/reply"

# JSON payload
payload = {
    "platform": "twitter",
    "post_text": "I am pleased to announce the launch of our new product, which is a cutting-edge solution for businesses looking to boost their online presence and reach a wider audience."
}

# Send POST request
response = requests.post(url, json=payload)

# Handle response
if response.status_code == 200:
    print("Generated Replies:", response.json()["generated_replies"])
else:
    print("Error:", response.status_code, response.text)
