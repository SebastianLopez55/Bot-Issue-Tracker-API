# views.py contains the routes and views for the web application, handling the logic of user requests.

from flask import Blueprint, request, jsonify
from database_sim import database_sim
from .api import create_ticket, query_ticket_status, update_ticket_status_api

main_blueprint = Blueprint("main", __name__)
VALID_STATUS = ["OPEN", "IN PROGRESS", "CLOSED"]


@main_blueprint.route("/user_report", methods=["POST"])
def report_issue():
    data = request.json
    user_report = data.get("user_report")
    ticket = create_ticket(user_report)  # Call OpenAI API

    return jsonify(ticket.__dict__), 200
    # if "error" in ticket:
    #     # If there's an error key in the ticket, it means processing failed
    #     return jsonify({"error": ticket["error"]}), 400
    # else:
    #     # If processing was successful, return the ticket as is
    #     return jsonify(ticket), 200


@main_blueprint.route("/ticket_status/<ticket_id>", methods=["GET"])
def get_ticket_status(ticket_id):
    response = query_ticket_status(ticket_id)
    if "message" in response:
        # If the response contains "message", it indicates an error or info message
        return jsonify(response), 404  # Not found or specific error
    else:
        # Successful ticket lookup
        return jsonify(response), 200


@main_blueprint.route("/ticket_status/<ticket_id>", methods=["PATCH"])
def update_ticket_status(ticket_id):
    data = request.json
    new_status = data.get("new_status")
    if not new_status or new_status not in VALID_STATUS:
        return jsonify({"message": "Valid new status is required."}), 400
    if update_ticket_status_api(ticket_id, new_status):
        return jsonify({"message": "Ticket status updated successfully."}), 200
    else:
        return jsonify({"message": "Ticket not found."}), 404


@main_blueprint.route("/tickets", methods=["GET"])
def get_all_tickets():
    tickets = database_sim.db_instance.get_all_tickets()
    return jsonify([ticket.__dict__ for ticket in tickets]), 200
