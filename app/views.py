# Contains the routes and views for the web application, handling the logic of user requests.

from flask import Blueprint, request, jsonify
from .api import create_ticket

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/user_report", methods=["POST"])
def report_issue():
    data = request.json
    user_report = data.get("user_report")
    ticket = create_ticket(user_report)  # Call OpenAI API
    return jsonify(ticket.__dict__), 200
