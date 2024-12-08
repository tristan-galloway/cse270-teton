import requests

def test_users_endpoint_unauthorized(mocker):
    # Mock the requests.get method
    mocked_get = mocker.patch("requests.get")
    
    # Configure the mock for unauthorized response
    mocked_get.return_value.status_code = 401
    mocked_get.return_value.text = ""
    
    # Define the URL and parameters
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "admin"}
    
    # Send GET request
    response = requests.get(url, params=params)
    
    # Assert the response code is 401
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"
    
    # Assert the response body is empty
    assert response.text == "", f"Expected empty response, got: {response.text}"

def test_users_endpoint_valid_credentials(mocker):
    # Mock the requests.get method
    mocked_get = mocker.patch("requests.get")
    
    # Configure the mock for valid credentials response
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.text = ""
    
    # Define the URL and parameters
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "qwerty"}
    
    # Send GET request
    response = requests.get(url, params=params)
    
    # Assert the response code is 200
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Assert the response body is empty
    assert response.text == "", f"Expected empty response, got: {response.text}"