# API Tests - Using Python 

## What is Python and Pytest Framework 

`Python` is a high-level, general-purpose programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python is designed to be easy to learn and has a clean and concise syntax, which makes it a popular choice for both beginners and experienced programmers.

The `pytest` framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

### Setup of dependencies for the tests 

To activate our environment, we use the command:
```bash
python -m venv venv
venv\Scripts\Activate
```
If everything is correct, your environment will be activated and on the cmd you will see like this:
```bash
(name_of_environment) C:\User\tests 
```
To disable your environment just run:
```bash
deactivate
```
### Setup:

```bash
pip install requests
```

```bash
pip install pytest
```
```bash
pip install pytest-html
```
```bash
pip freeze > requirements.txt
```
### For the report generation use 

```bash
pytest test.py --html-report=./report/report.html 
```
OR
```bash
pytest test_airports.py -s -v --html=./report/report.html
```
### To run specific test function

focused test
```bash
pytest test_airports.py -s -v -k test_get_airports --html=./report/report.html
```
### Definition of the API that will be tested

API Testing with Requests and Pytest
This repository contains Python scripts for testing an API using the requests library and the pytest framework. The API being tested is the Airport Gap API.

Configuration: Create a config.ini file with the necessary configuration parameters. Example:

### config.ini file

[API]
TOKEN = <Your API Token>
BASE_URL = https://airportgap.com/api
EMAIL = <Your Email>
PASSWORD = <Your Password>
FAVORITES_MESSAGE = "My favorite airport"
PATCHED_FAVORITES_MESSAGE = "My updated favorite airport"
OSAKA = KIX
NY = JFK
Running the Tests
Run the tests using the following command:

```bash
pytest test_airports.py
```
### Test Descriptions

    test_get_airports: Sends a GET request to retrieve a list of airports and asserts the response.

    test_get_single_airport: Sends a GET request to retrieve information about a specific airport and asserts the response.

    test_post_airport_distance: Sends a POST request to calculate the distance between two airports and asserts the response.

    test_get_token: Sends a POST request to authenticate and obtain an API token, then asserts the response.

    test_get_favorites: Sends a GET request to retrieve the list of favorite airports and asserts that the list is empty.

    test_create_favorite: Sends a POST request to add a favorite airport and asserts the response.

    test_get_favorite_by_id: Sends a GET request to retrieve information about a specific favorite airport and asserts the response.

    test_patch_favorite_note: Sends a PATCH request to update the note of a favorite airport and asserts the response.

    test_get_patched_favorite_by_id: Sends a GET request to retrieve information about a specific favorite airport after the patch and asserts the response.

    test_delete_favorite: Sends a DELETE request to remove a favorite airport and asserts the response.

For more details, check my article [here](https://)


About the API:
- Base URL: `https://airportgap.com`


For this tutorial, we will focus on three types of tests:
- Contract: If the API is able to validate the query parameters that are sent 
- Status: If the status codes are correct 
- Authentication: Even this API doesn't requires the token, we can do tests with this 

Our Scenarios:

- Positive testing of a user flow 
- Negative scenarios to test the resilency of the API endpoints to the violations

