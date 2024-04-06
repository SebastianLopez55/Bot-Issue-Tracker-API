# Handles API-specific logic, managing data processing and responses for API requests.
from dotenv import load_dotenv
from flask import jsonify
from .models import Ticket
import json
import openai
import prompt
import uuid
import os


# Load environment variables
load_dotenv()

# Retrieve and set the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "API key not found. Ensure your .env file has the OPENAI_API_KEY variable."
    )


# Set OpenAI API key for use in API calls
openai.api_key = api_key


def process_report(report):
    try:
        # Make the API call to OpenAI
        completion = openai.chat.completions.create(
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

    ticket_id = str(uuid.uuid4())
    problem_location = report_details.get("Location", "Unknown location")
    problem_type = report_details.get("Problem Type", "Unknown type")
    summary = report_details.get("Description", "No description provided")
    bot_details = report_details.get("Bot Details", "No bot details provided")
    bot_id = "PlaceholderBotID"

    # Create a Ticket instance with the processed details
    ticket = Ticket(
        ticket_id, problem_location, problem_type, summary, bot_details, bot_id
    )

    # TODO Save ticket to database or in-memory data structure (not shown here)

    return ticket
