from make_requests import get_request, post_request, get_request_qp
from faker import Faker
from faker.providers import person

# import ipdb
import re

fake = Faker()
fake.add_provider(person)

base_url = "https://gorest.co.in/public/v2/users/"
headers = {
    "Authorization": "Bearer a3672aea6955926bf817d58232ae42882c6eaba1d6a5a10d148482a884ff354d"
}
user = {
    "name": fake.name(),
    "email": fake.email(),
    "gender": "male",
    "status": "active",
}
name = ""
email = ""
id = ""


class TestClass:
    def test_get_users(self):
        # ipdb.set_trace()
        # Arrange:
        # Act:
        response = get_request(base_url)
        # Assertion:
        assert response.status_code == 200  # Validation of status code
        data = response.json()
        # Assertion of body response content:
        assert len(data) > 0
        assert data[0]

    def test_post_request(self):
        # Arrange:
        body = user
        # Act:
        response = post_request(base_url, body, headers)
        data = response.json()
        global name, email, id
        name = data["name"]
        email = data["email"]
        id = data["id"]
        print(name, email, id)
        # Assertion:
        assert response.status_code == 201

    def test_get_created_user(self):
        # Arrange:
        global name, email, id

        name = re.sub(" ", "%20", name)
        query_parameters = f"?name={name}&email={email}"
        # Act:
        print(f"https://gorest.co.in/public/v2/users{query_parameters}")
        response = get_request_qp(
            f"https://gorest.co.in/public/v2/users{query_parameters}"
        )
        # Assertion:
        assert response.status_code == 200
        data = response.json()
        print(data)
        # assert data[0]["name"] == name
        # assert data[0]["email"] == email

    # def test_search_asteroids_with_end_date(self):
    #     # Arrange:
    #     query_parameters = "api_key=DEMO_KEY&end_date=2023-11-10"
    #     # Act:
    #     response = make_request(query_parameters)
    #     # Assertion:
    #     assert response.status_code == 200
    #     data = response.json()
    #     assert len(data) > 0
    #     assert data["element_count"] > 0

    # def test_search_asteroids_in_valid_range(self):
    #     # Arrange:
    #     query_parameters = "api_key=DEMO_KEY&start_date=2023-11-09&end_date=2023-11-10"
    #     # Act:
    #     response = make_request(query_parameters)
    #     # Assertion:
    #     assert response.status_code == 200
    #     data = response.json()
    #     assert len(data) > 0
    #     assert data["element_count"] > 0

    # def test_search_asteroids_in_invalid_range(self):
    #     # Arrange:
    #     query_parameters = "api_key=DEMO_KEY&start_date=2023-11-19&end_date=2023-11-10"
    #     # Act:
    #     response = make_request(query_parameters)
    #     # Assertion:
    #     assert response.status_code == 400

    # def test_search_asteroids_in_invalid_token(self):
    #     # Arrange:
    #     query_parameters = "api_key=INVALID_TOKEN"
    #     # Act:
    #     response = make_request(query_parameters)
    #     # Assertion:
    #     assert response.status_code == 403
