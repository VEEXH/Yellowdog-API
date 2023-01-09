# Yellowdog-API Integration
This program integrates with the Yellowdog API to retrieve and manipulate data in your Yellowdog account. It uses the requests library to send HTTP requests to the API and handle the response.

## Requirements
- Python 3.6 or higher
- A Yellowdog API key
- The requests library ``(install using pip install requests)``

## Usage
1) Set your Yellowdog API key in the ``api_key`` variable.
2) Execute the program using the following command:

``python yellowdog.py``

The program will send a GET request to the Yellowdog API's ``/orders`` endpoint to retrieve a list of orders and print the ID and name of each order.

## Customization
You can customize the program by modifying the API request and response handling logic. For example, you could add additional endpoints or parameters to the request, or modify the way the response data is processed and displayed.
You can find more information about the Yellowdog API and available endpoints at https://api.yellowdog.co/docs/ 

## Contributing
If you would like to contribute to this project, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes and push to the new branch.
- Create a pull request.

## License 
This project is licensed under the MIT License. 
