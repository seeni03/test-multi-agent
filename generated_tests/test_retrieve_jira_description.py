import pytest
from unittest.mock import patch
import requests

@pytest.fixture(scope="module")
def mock_server():
    """Setup and teardown for mock server."""
    print("Starting mock server...")
    yield
    print("Stopping mock server...")

@patch("requests.get")
def test_retrieve_and_validate_jira_description(mock_get, mock_server):
    """
    Test retrieving and validating a Jira issue description.

    Args:
        mock_get: Mocked requests.get method.
        mock_server: Fixture for mock server setup/teardown.
    """
    jira_id = "PROJ-101"
    url = f"http://localhost:8080/jira/{jira_id}"

    # Mock server response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "summary": "Fetch Jira description by ID",
        "description": "System should retrieve Jira issue description and validate text."
    }

    # Execute the request
    response = requests.get(url)

    # Validate the response
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    data = response.json()
    assert "summary" in data, "Response JSON does not contain 'summary'"
    assert "description" in data, "Response JSON does not contain 'description'"
    assert data["summary"] == "Fetch Jira description by ID", f"Unexpected summary: {data['summary']}"
    assert data["description"] == "System should retrieve Jira issue description and validate text.", f"Unexpected description: {data['description']}"