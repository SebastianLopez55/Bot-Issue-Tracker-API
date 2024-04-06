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
