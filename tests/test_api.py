import json
import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    with app.test_client() as client:
        yield client


def test_user_report_problem_type(client):
    """Test the /user_report endpoint for problem type correctness."""
    report_payload = {
        "user_report": "The bot seems to be stuck at the corner of 5th and Main."
    }
    response = client.post("/user_report", json=report_payload)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["problem_type"] in ["Software", "Hardware", "Field"]


def test_user_report_problem_description(client):
    """Test the /user_report endpoint for problem description being a string."""
    report_payload = {"user_report": "The bot's screen is flickering intermittently."}
    response = client.post("/user_report", json=report_payload)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(data["problem_description"], str)


def test_user_report_ticket_status(client):
    """Test the /user_report endpoint for correct ticket status."""
    report_payload = {"user_report": "The delivery bot is late for its delivery."}
    response = client.post("/user_report", json=report_payload)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["ticket_status"] == "OPEN", "The ticket status should be OPEN."


def test_user_report_bot_details(client):
    """Test the /user_report endpoint for correct bot details."""
    report_payload = {
        "user_report": "The bot's navigation seems erratic near the park."
    }
    response = client.post("/user_report", json=report_payload)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(
        data["bot_battery_level"], float
    ), "Bot battery level should be a float."
    assert isinstance(
        data["bot_software_version"], str
    ), "Bot software version should be a string."


def test_user_report_problem_type_categories(client):
    """Test the /user_report endpoint for correct problem type categorization."""
    report_payload = {
        "user_report": "It seems like the bot's lidar sensor is malfunctioning."
    }
    response = client.post("/user_report", json=report_payload)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["problem_type"] in [
        "Software",
        "Hardware",
        "Field",
    ], "Problem type must be one of software, hardware, or field."


def test_user_report_response_completeness(client):
    """Test the /user_report endpoint for response completeness."""
    report_payload = {"user_report": "The bot is unresponsive after the latest update."}
    response = client.post("/user_report", json=report_payload)
    data = json.loads(response.data)

    required_fields = [
        "ticket_id",
        "problem_type",
        "problem_description",
        "bot_id",
        "bot_location",
        "bot_status",
        "bot_battery_level",
        "bot_software_version",
        "bot_hardware_version",
        "ticket_status",  # Assuming this is the correct field name based on your initial error description.
    ]

    assert response.status_code == 200, "Response status code should be 200."
    assert all(
        field in data for field in required_fields
    ), "All required fields must be present in the response."
