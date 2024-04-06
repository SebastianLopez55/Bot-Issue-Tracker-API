# Contains the routes and views for the web application, handling the logic of user requests.

from flask import Blueprint, request, jsonify
from .api import create_ticket, query_ticket_status

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/user_report", methods=["POST"])
def report_issue():
    data = request.json
    user_report = data.get("user_report")
    ticket = create_ticket(user_report)  # Call OpenAI API
    return jsonify(ticket.__dict__), 200


@main_blueprint.route("/ticket_status/<ticket_id>", methods=["GET"])
def get_ticket_status(ticket_id):
    response = query_ticket_status(ticket_id)
    if "message" in response:
        # If the response contains "message", it indicates an error or info message
        return jsonify(response), 404  # Not found or specific error
    else:
        # Successful ticket lookup
        return jsonify(response), 200
