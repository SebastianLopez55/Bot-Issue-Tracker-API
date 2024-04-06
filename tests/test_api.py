# test_api.py
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


"""
POST Request test: receive report and output ticket

"""


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


"""
GET Request test: query the status of a ticket by its ID.

"""


def test_get_ticket_status_success(client):
    """
    Test that querying a ticket status by ID returns the correct status for an existing ticket.
    """
    # First, create a ticket to ensure there's at least one ticket in the database.
    report_payload = {"user_report": "The bot failed to navigate to the destination."}
    create_response = client.post("/user_report", json=report_payload)
    create_data = json.loads(create_response.data)
    ticket_id = create_data["ticket_id"]

    # Now, attempt to retrieve the status of the created ticket.
    get_response = client.get(f"/ticket_status/{ticket_id}")
    get_data = json.loads(get_response.data)

    assert get_response.status_code == 200
    assert get_data["ticket_id"] == ticket_id
    assert "ticket_status" in get_data


def test_get_ticket_status_failure(client):
    """
    Test querying a ticket status by ID for a non-existent ticket returns the appropriate error response.
    """
    non_existent_ticket_id = "non-existent-id"
    response = client.get(f"/ticket_status/{non_existent_ticket_id}")
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data["message"] == "Ticket not in database."


"""
PATCH Request test: track the status of the ticket.

"""


def test_update_ticket_status_success(client):
    # First, create a ticket
    report_payload = {"user_report": "The bot is not responding to commands."}
    create_response = client.post("/user_report", json=report_payload)
    create_data = json.loads(create_response.data)
    ticket_id = create_data["ticket_id"]

    # Now, attempt to update the status of the created ticket
    update_payload = {"new_status": "IN PROGRESS"}
    update_response = client.patch(f"/ticket_status/{ticket_id}", json=update_payload)
    update_data = json.loads(update_response.data)

    assert update_response.status_code == 200
    assert update_data["message"] == "Ticket status updated successfully."


def test_update_ticket_status_invalid_status(client):
    # Assuming there's at least one ticket created from previous tests
    report_payload = {"user_report": "Another bot issue report."}
    create_response = client.post("/user_report", json=report_payload)
    create_data = json.loads(create_response.data)
    ticket_id = create_data["ticket_id"]

    update_payload = {"new_status": "INVALID_STATUS"}
    response = client.patch(f"/ticket_status/{ticket_id}", json=update_payload)
    data = json.loads(response.data)

    assert response.status_code == 400
    assert data["message"] == "Valid new status is required."


def test_update_ticket_status_nonexistent(client):
    nonexistent_ticket_id = "nonexistent123"
    update_payload = {"new_status": "CLOSED"}
    response = client.patch(
        f"/ticket_status/{nonexistent_ticket_id}", json=update_payload
    )
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data["message"] == "Ticket not found."


"""
GET Request test: return all tickets

"""
