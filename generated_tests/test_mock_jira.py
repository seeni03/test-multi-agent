import pytest
from unittest.mock import patch
import requests

@pytest.mark.parametrize("jira_id, expected_status, expected_error", [
    ("PROJ-101", 200, None),
    ("INVALID-001", 404, "Not Found"),
    ("", 404, "Not Found"),
    ("!@#$%^&*", 404, "Not Found"),
    ("12345", 404, "Not Found"),
    ("proj-101", 404, "Not Found"),  # Case sensitivity
    ("PROJ-101 ", 404, "Not Found"),  # Trailing whitespace
    (" PROJ-101", 404, "Not Found"),  # Leading whitespace
    ("A" * 256, 404, "Not Found"),  # Long ID
])
@patch("requests.get")
def test_jira_id(mock_get, jira_id, expected_status, expected_error):
    """
    Test retrieving Jira issue descriptions with various edge cases.

    Args:
        mock_get: Mocked requests.get method.
        jira_id: The Jira ID to test.
        expected_status: Expected HTTP status code.
        expected_error: Expected error message in the response.
    """
    # Mock server response
    if expected_status == 200:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "summary": "Fetch Jira description by ID",
            "description": "System should retrieve Jira issue description and validate text."
        }
    else:
        mock_get.return_value.status_code = expected_status
        mock_get.return_value.json.return_value = {"error": expected_error}

    # Perform the request
    response = requests.get(f"http://localhost:8080/jira/{jira_id}")

    # Validate the response
    assert response.status_code == expected_status
    if expected_status == 200:
        data = response.json()
        assert data["summary"] == "Fetch Jira description by ID"
        assert data["description"] == "System should retrieve Jira issue description and validate text."
    else:
        data = response.json()
        assert "error" in data
        assert data["error"] == expected_error