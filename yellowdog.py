import requests

# Set your Yellowdog API key
api_key = 'YOUR_API_KEY'

# Set the API endpoint URL
api_url = 'https://api.yellowdog.co/v1/'

# Set the headers for the API request
headers = {
    'Authorization': f'Token {api_key}',
    'Content-Type': 'application/json',
}

# Send a GET request to the /orders endpoint to retrieve a list of orders
response = requests.get(f'{api_url}orders', headers=headers)

# Check the response status code
if response.status_code == 200:
    # Print the list of orders
    orders = response.json()
    for order in orders:
        print(f'Order {order["id"]}: {order["name"]}')
else:
    # Print an error message
    print('Error retrieving orders')
