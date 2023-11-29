import requests
import configparser
import pytest

config = configparser.ConfigParser()
config.read("config.ini")

api_key = config.get("API", "TOKEN")
base_url = config.get("API", "BASE_URL")
email = config.get("API", "EMAIL")
password = config.get("API", "PASSWORD")
favorites_message = config.get("API", "FAVORITES_MESSAGE")
patched_favorites_message = config.get("API", "PATCHED_FAVORITES_MESSAGE").strip('"')
osaka = config.get("API", "OSAKA")
ny = config.get("API", "NY")
id = ""

class TestClass:
    def test_get_airports(self):
        # Send a GET request to the API endpoint
        response = requests.get(f"{base_url}/airports")

        # Check if the response status code is 200 (OK)
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"

        # Parse the JSON response
        json_response = response.json()

        # Check if the 'data' key is present in the response
        assert "data" in json_response, "Response does not contain 'data' key"

        # Check if 'data' is a non-empty list
        assert (
            isinstance(json_response["data"], list) and len(json_response["data"]) > 0
        ), "No data in the response"

        # Iterate through each airport in the response and make assertions
        for airport in json_response["data"]:
            assert "id" in airport, "Airport object does not contain 'id' key"
            assert (
                "type" in airport and airport["type"] == "airport"
            ), "Invalid 'type' in airport object"
            attributes = airport.get("attributes", {})
            assert (
                "altitude" in attributes
            ), "Airport attributes do not contain 'altitude' key"
            assert "city" in attributes, "Airport attributes do not contain 'city' key"
            assert (
                "country" in attributes
            ), "Airport attributes do not contain 'country' key"
            assert "iata" in attributes, "Airport attributes do not contain 'iata' key"
            assert "icao" in attributes, "Airport attributes do not contain 'icao' key"
            assert (
                "latitude" in attributes
            ), "Airport attributes do not contain 'latitude' key"
            assert (
                "longitude" in attributes
            ), "Airport attributes do not contain 'longitude' key"
            assert "name" in attributes, "Airport attributes do not contain 'name' key"
            assert (
                "timezone" in attributes
            ), "Airport attributes do not contain 'timezone' key"

        # Check if the 'links' key is present in the response
        assert "links" in json_response, "Response does not contain 'links' key"

        # Check if the 'self' link is present in the 'links' section
        assert "self" in json_response["links"], "Links do not contain 'self' key"

        # Add more assertions as needed based on your specific requirements

    def test_get_single_airport(self):
        # Send a GET request to the specific airport endpoint
        response = requests.get(f"{base_url}/airports/{osaka}")

        # Check if the response status code is 200 (OK)
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"

        # Parse the JSON response
        json_response = response.json()

        # Check if the 'data' key is present in the response
        assert "data" in json_response, "Response does not contain 'data' key"

        # Check if 'data' is a dictionary
        assert isinstance(
            json_response["data"], dict
        ), "Data in the response is not a dictionary"

        # Make assertions about the attributes of the specific airport
        airport_data = json_response["data"]
        assert "id" in airport_data, "Airport data does not contain 'id' key"
        assert (
            "type" in airport_data and airport_data["type"] == "airport"
        ), "Invalid 'type' in airport data"
        attributes = airport_data.get("attributes", {})
        assert (
            "altitude" in attributes and attributes["altitude"] == 26
        ), "Invalid 'altitude' in airport attributes"
        assert (
            "city" in attributes and attributes["city"] == "Osaka"
        ), "Invalid 'city' in airport attributes"
        assert (
            "country" in attributes and attributes["country"] == "Japan"
        ), "Invalid 'country' in airport attributes"
        assert (
            "iata" in attributes and attributes["iata"] == "KIX"
        ), "Invalid 'iata' in airport attributes"
        assert (
            "icao" in attributes and attributes["icao"] == "RJBB"
        ), "Invalid 'icao' in airport attributes"
        assert (
            "latitude" in attributes and attributes["latitude"] == "34.427299"
        ), "Invalid 'latitude' in airport attributes"
        assert (
            "longitude" in attributes and attributes["longitude"] == "135.244003"
        ), "Invalid 'longitude' in airport attributes"
        assert (
            "name" in attributes
            and attributes["name"] == "Kansai International Airport"
        ), "Invalid 'name' in airport attributes"
        assert (
            "timezone" in attributes and attributes["timezone"] == "Asia/Tokyo"
        ), "Invalid 'timezone' in airport attributes"

    def test_post_airport_distance(self):
        # Data for the POST request
        payload = {"from": osaka, "to": "NRT"}

        # Send a POST request to the airport distance endpoint
        response = requests.post(f"{base_url}/airports/distance", data=payload)

        # Check if the response status code is 200 (OK)
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"

        # Parse the JSON response
        json_response = response.json()

        # Check if the 'data' key is present in the response
        assert "data" in json_response, "Response does not contain 'data' key"

        # Check if 'data' is a dictionary
        assert isinstance(
            json_response["data"], dict
        ), "Data in the response is not a dictionary"

        # Make assertions about the attributes of the airport distance
        airport_distance_data = json_response["data"]
        assert (
            "id" in airport_distance_data and airport_distance_data["id"] == "KIX-NRT"
        ), "Invalid 'id' in airport distance data"
        assert (
            "type" in airport_distance_data
            and airport_distance_data["type"] == "airport_distance"
        ), "Invalid 'type' in airport distance data"

        attributes = airport_distance_data.get("attributes", {})
        assert (
            "from_airport" in attributes and "to_airport" in attributes
        ), "Missing 'from_airport' or 'to_airport' in airport distance attributes"

        from_airport = attributes.get("from_airport", {})
        assert (
            "id" in from_airport and from_airport["id"] == 3158
        ), "Invalid 'id' in from_airport attributes"
        assert (
            "name" in from_airport
            and from_airport["name"] == "Kansai International Airport"
        ), "Invalid 'name' in from_airport attributes"
        # Add more assertions as needed for other attributes

        to_airport = attributes.get("to_airport", {})
        assert (
            "id" in to_airport and to_airport["id"] == 1721
        ), "Invalid 'id' in to_airport attributes"
        assert (
            "name" in to_airport
            and to_airport["name"] == "Narita International Airport"
        ), "Invalid 'name' in to_airport attributes"
        # Add more assertions as needed for other attributes

        assert "kilometers" in attributes and isinstance(
            attributes["kilometers"], float
        ), "Invalid 'kilometers' in airport distance attributes"
        assert "miles" in attributes and isinstance(
            attributes["miles"], float
        ), "Invalid 'miles' in airport distance attributes"
        assert "nautical_miles" in attributes and isinstance(
            attributes["nautical_miles"], float
        ), "Invalid 'nautical_miles' in airport distance attributes"

    def test_get_token(self):
        # Data for the POST request
        payload = {"email": email, "password": password}

        # Send a POST request to the tokens endpoint
        response = requests.post(f"{base_url}/tokens", data=payload)

        # Check if the response status code is 200 (OK)
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"

        # Parse the JSON response
        json_response = response.json()

        # Check if the 'token' key is present in the response
        assert "token" in json_response, "Response does not contain 'token' key"

    def test_get_favorites(self):
        # Set up the request headers with the authorization token
        headers = {"Authorization": f"Token {api_key}"}

        # Send a GET request to the favorites endpoint with the authorization token
        response = requests.get(f"{base_url}/favorites", headers=headers)

        # Check if the response status code is 200 (OK)
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"

        # Parse the JSON response
        json_response = response.json()
        assert "data" in json_response, "Response does not contain 'data' key"

        # Assert that the 'data' key contains an empty list
        assert (
            isinstance(json_response["data"], list) and len(json_response["data"]) == 0
        ), "Expected an empty list in 'data'"

    def test_create_favorite(self):
        # Set up the request headers with the authorization token
        headers = {"Authorization": f"Bearer token={api_key}"}

        # Set up the request data
        data = {"airport_id": ny, "note": favorites_message}

        # Send a POST request to the favorites endpoint with the authorization token
        response = requests.post(f"{base_url}/favorites", data=data, headers=headers)

        # Check if the response status code is 201 (Created)
        assert (
            response.status_code == 201
        ), f"Expected status code 201, but got {response.status_code}"

        # Parse the JSON response
        json_response = response.json()

        # Add assertions based on the structure of the response
        assert "data" in json_response, "Response does not contain 'data' key"

        favorite_data = json_response["data"]
        global id
        id = favorite_data["id"]
        assert (
            "id" in favorite_data and favorite_data["id"]
        ), "Invalid 'id' in favorite data"
        assert (
            "type" in favorite_data and favorite_data["type"] == "favorite"
        ), "Invalid 'type' in favorite data"

        attributes = favorite_data.get("attributes", {})
        assert (
            "airport" in attributes
        ), "Favorite attributes do not contain 'airport' key"
        assert (
            "note" in attributes
            and attributes["note"] == "My usual layover when visiting family"
        ), "Invalid 'note' in favorite attributes"

        airport_info = attributes.get("airport", {})
        assert (
            "altitude" in airport_info and airport_info["altitude"] == 13
        ), "Invalid 'altitude' in airport info"
        assert (
            "city" in airport_info and airport_info["city"] == "New York"
        ), "Invalid 'city' in airport info"
        assert (
            "country" in airport_info and airport_info["country"] == "United States"
        ), "Invalid 'country' in airport info"

    def test_get_favorite_by_id(self):
        # Set up the request headers with the authorization token
        headers = {"Authorization": f"Bearer token={api_key}"}

        # Send a GET request to the specified favorites endpoint with the authorization token
        response = requests.get(f"{base_url}/favorites/{id}", headers=headers)

        # Check if the response status code is 200 (OK)
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"

        # Parse the JSON response
        json_response = response.json()

        # Add assertions based on the structure of the response
        assert "data" in json_response, "Response does not contain 'data' key"

        favorite_data = json_response["data"]
        assert (
            "id" in favorite_data and favorite_data["id"] == id
        ), "Invalid 'id' in favorite data"
        assert (
            "type" in favorite_data and favorite_data["type"] == "favorite"
        ), "Invalid 'type' in favorite data"

        attributes = favorite_data.get("attributes", {})
        assert (
            "airport" in attributes
        ), "Favorite attributes do not contain 'airport' key"
        assert (
            "note" in attributes and attributes["note"] == favorites_message
        ), "Invalid 'note' in favorite attributes"

        airport_info = attributes.get("airport", {})
        assert (
            "altitude" in airport_info and airport_info["altitude"] == 13
        ), "Invalid 'altitude' in airport info"
        assert (
            "city" in airport_info and airport_info["city"] == "New York"
        ), "Invalid 'city' in airport info"
        assert (
            "country" in airport_info and airport_info["country"] == "United States"
        ), "Invalid 'country' in airport info"

    def test_patch_favorite_note(self):
        # Set up the request headers with the authorization token
        headers = {"Authorization": f"Bearer token={api_key}"}

        # Set up the request data for the PATCH request
        data = {
            "note": "My usual layover when visiting family, although it's really far away..."
        }

        # Send a PATCH request to the specified favorites endpoint with the authorization token
        response = requests.patch(
            f"{base_url}/favorites/{id}", data=data, headers=headers
        )

        # Check if the response status code is 200 (OK)
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"

        # Parse the JSON response
        json_response = response.json()

        # Add assertions based on the structure of the response
        assert "data" in json_response, "Response does not contain 'data' key"

        favorite_data = json_response["data"]
        assert (
            "id" in favorite_data and favorite_data["id"] == id
        ), "Invalid 'id' in favorite data"
        assert (
            "type" in favorite_data and favorite_data["type"] == "favorite"
        ), "Invalid 'type' in favorite data"

        attributes = favorite_data.get("attributes", {})
        assert (
            "airport" in attributes
        ), "Favorite attributes do not contain 'airport' key"
        assert (
            "note" in attributes and attributes["note"] == patched_favorites_message
        ), "Invalid 'note' in favorite attributes"

        airport_info = attributes.get("airport", {})
        assert (
            "altitude" in airport_info and airport_info["altitude"] == 13
        ), "Invalid 'altitude' in airport info"
        assert (
            "city" in airport_info and airport_info["city"] == "New York"
        ), "Invalid 'city' in airport info"
        assert (
            "country" in airport_info and airport_info["country"] == "United States"
        ), "Invalid 'country' in airport info"

    def test_get_patched_favorite_by_id(self):
        # Set up the request headers with the authorization token
        headers = {"Authorization": f"Bearer token={api_key}"}

        # Send a GET request to the specified favorites endpoint with the authorization token
        response = requests.get(f"{base_url}/favorites/{id}", headers=headers)

        # Check if the response status code is 200 (OK)
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"

        # Parse the JSON response
        json_response = response.json()

        # Add assertions based on the structure of the response
        assert "data" in json_response, "Response does not contain 'data' key"

        favorite_data = json_response["data"]
        assert (
            "id" in favorite_data and favorite_data["id"] == id
        ), "Invalid 'id' in favorite data"
        assert (
            "type" in favorite_data and favorite_data["type"] == "favorite"
        ), "Invalid 'type' in favorite data"

        attributes = favorite_data.get("attributes", {})
        assert (
            "airport" in attributes
        ), "Favorite attributes do not contain 'airport' key"
        assert (
            "note" in attributes and attributes["note"] == patched_favorites_message
        ), "Invalid 'note' in favorite attributes"

        airport_info = attributes.get("airport", {})
        assert (
            "altitude" in airport_info and airport_info["altitude"] == 13
        ), "Invalid 'altitude' in airport info"
        assert (
            "city" in airport_info and airport_info["city"] == "New York"
        ), "Invalid 'city' in airport info"
        assert (
            "country" in airport_info and airport_info["country"] == "United States"
        ), "Invalid 'country' in airport info"

    def test_delete_favorite(self):
        # Set up the request headers with the authorization token
        headers = {"Authorization": f"Bearer token={api_key}"}

        # Send a DELETE request to the specified favorites endpoint with the authorization token
        response = requests.delete(f"{base_url}/favorites/{id}", headers=headers)

        # Check if the response status code is 204 (No Content)
        assert (
            response.status_code == 204
        ), f"Expected status code 204, but got {response.status_code}"


# Run the tests using Pytest
if __name__ == "__main__":
    pytest.main([__file__])
