# api.py handles API-specific logic, managing data processing and responses for API requests.
from dotenv import load_dotenv
from database_sim import database_sim
from flask import jsonify
from .models import Ticket
import json
import openai
import prompt
import uuid
import os

# Load environment variables
load_dotenv()

# Set OpenAI API key for use in API calls
client = openai.OpenAI()


def process_report(report):
    try:
        # Make the API call to OpenAI
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": prompt.system_prompt + "USE JSON FOR OUTPUT",
                },
                {
                    "role": "user",
                    "content": report,
                },
            ],
            temperature=0.5,
        )

        # Extract the message content from the response
        message_content = completion.choices[0].message.content
        message_content_dict = json.loads(message_content)

        return message_content_dict
    except Exception as e:
        return "Error processing report: " + str(e)


def create_ticket(user_report):
    report_details = process_report(user_report)

    if isinstance(report_details, str):
        # Handle the error case, perhaps log the error, and return an appropriate response
        return {"error": "Failed to process report due to an error: " + report_details}

    heartbeat_info_dict = database_sim.db_instance.get_heartbeat("bot_id")

    # Ticket info
    ticket_id = str(uuid.uuid4())
    ticket_status = "OPEN"
    # OPENAI API info
    problem_description = report_details.get("Description", "No description provided")
    problem_type = report_details.get("Problem Type", "Unknown type")
    # Heartbeat info
    bot_id = heartbeat_info_dict.get("bot_id", "Unknown bot ID")
    bot_location = (
        f" lat: {heartbeat_info_dict.get('location', {}).get('lat', 'Unknown')}, lon: {heartbeat_info_dict.get('location', {}).get('lon', 'Unknown')} "
        if heartbeat_info_dict
        else "Unknown"
    )
    bot_status = heartbeat_info_dict.get("status", "Unknown status")
    bot_battery_level = heartbeat_info_dict.get(
        "battery_level", "Unknown battery level"
    )
    bot_software_version = heartbeat_info_dict.get(
        "software_version", "Unknown software version"
    )
    bot_hardware_version = heartbeat_info_dict.get(
        "hardware_version", "Unknown hardware version"
    )

    # Create a Ticket instance with the processed details
    ticket = Ticket(
        ticket_id,
        ticket_status,
        problem_description,
        problem_type,
        bot_id,
        bot_location,
        bot_status,
        bot_battery_level,
        bot_software_version,
        bot_hardware_version,
    )

    # Save ticket to  database
    database_sim.db_instance.save_ticket(ticket)

    return ticket


def query_ticket_status(ticket_id):
    ticket = database_sim.db_instance.get_ticket(ticket_id)
    if ticket and ticket != "Ticket not in database.":
        # Ticket found
        return {"ticket_id": ticket.ticket_id, "ticket_status": ticket.ticket_status}
    else:
        # Ticket not found
        return {"message": "Ticket not in database."}


def update_ticket_status_api(ticket_id, new_status):
    # Call the database method to update the ticket status
    return database_sim.db_instance.update_ticket_status(ticket_id, new_status)
