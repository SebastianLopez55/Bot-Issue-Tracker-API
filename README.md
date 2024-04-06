
# Bot Issue Tracker API

## Introduction

This project provides a comprehensive solution for receiving, processing, and managing reports of issues with delivery bots. By leveraging cutting-edge natural language processing techniques, the system efficiently categorizes each report into software, hardware, or field-related problems. It automatically generates a detailed ticket containing the problem's location, type, and a summary of the issue based on the user's description and the bot's status data. This documentation outlines the purpose, technologies used, and setup instructions for the project.

## Purpose

The Bot Issue Tracker API is designed to streamline the process of handling and tracking reports of operational issues with delivery bots. This system ensures that each problem is quickly identified, categorized, and documented, allowing for efficient resolution management. By automating the initial steps of the issue-reporting process, the API facilitates a more responsive and effective maintenance protocol for these advanced machines.

## Technologies Used

- **Python**: High level programming language used to develop the core logic of the API and process natural language inputs.
- **Flask**: A lightweight WSGI web application framework in Python, used to create the API endpoints and handle HTTP requests and responses.
- **OpenAI's GPT**: Utilized for natural language processing to interpret the descriptions of issues reported by users and to assist in the automatic categorization of problems.
- **pytest**: A framework for easily building simple and scalable test cases for the application's API endpoints.

## Setup Instructions

To run this project on your local machine, follow these steps:

1. **Clone the Repository**

    Start by cloning this repository to your local machine. Use the following command:

    ```
    git clone <repository-url>
    ```

2. **Environment Setup**

    Ensure that Python 3.8 or later is installed on your system. It's recommended to use a virtual environment for Python projects to manage dependencies efficiently.

    To create a virtual environment, navigate to the project's root directory and run:

    ```
    python -m venv .venv
    ```

    Activate the virtual environment:

    - On Windows:
        ```
        .\.venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```
        source .venv/bin/activate
        ```

3. **Install Dependencies**

    With the virtual environment activated, install the project dependencies using:

    ```
    pip install -r requirements.txt
    ```

4. **Environment Variables**

    Create a `.env` file in the project root directory and add the OpenAI API key:

    ```
    OPENAI_API_KEY='your_openai_api_key_here'
    ```

5. **Running the Application**

    To start the Flask application, execute:

    ```
    python run.py
    ```

    The API is now running and accessible at `http://127.0.0.1:5000`.

6. **Testing**

    Run the tests to ensure everything is set up correctly:

    ```
    pytest
    ```


    

## API Documentation

This section outlines the available endpoints within the Bot Issue Tracker API, including their purpose and how to interact with them.

### Endpoints

#### 1. Report Issue

- **Endpoint Name**: `/user_report`
- **Method**: POST
- **Description**: Receives reports about bot issues in natural language, processes the report to identify the problem's location, type, and a summary. It then creates a ticket with this information along with the bot's real-time data.
- **Request Body**: JSON object containing the user's report.
  - Example:
    ```json
    {
      "user_report": "The bot stopped moving near the main square."
    }
    ```
- **Response**: JSON object representing the created ticket, including the ticket ID, problem description, type, and bot details.
  - Example:
    ```json
    {
      "ticket_id": "123456",
      "problem_description": "The bot stopped moving near the main square.",
      "problem_type": "Hardware",
      "bot_id": "bot_001",
      "bot_location": "lat: 37.7749, lon: -122.4194",
      "bot_status": "stopped",
      "bot_battery_level": 72.5,
      "bot_software_version": "v1.2.3",
      "bot_hardware_version": "v1.0",
      "ticket_status": "OPEN"
    }
    ```

#### 2. Get Ticket Status

- **Endpoint Name**: `/ticket_status/<ticket_id>`
- **Method**: GET
- **Description**: Retrieves the current status of a ticket given its ID.
- **URL Parameter**: `ticket_id` - The unique identifier for the ticket whose status is being queried.
- **Response**: JSON object with the ticket's current status.
  - Example:
    ```json
    {
      "ticket_id": "123456",
      "ticket_status": "OPEN"
    }
    ```

#### 3. Update Ticket Status

- **Endpoint Name**: `/ticket_status/<ticket_id>`
- **Method**: PATCH
- **Description**: Updates the status of an existing ticket to reflect its current progress (e.g., from "OPEN" to "IN PROGRESS").
- **URL Parameter**: `ticket_id` - The unique identifier for the ticket whose status is being updated.
- **Request Body**: JSON object specifying the new status for the ticket.
  - Example:
    ```json
    {
      "new_status": "IN PROGRESS"
    }
    ```
- **Response**: JSON object indicating the success of the operation.
  - Example:
    ```json
    {
      "message": "Ticket status updated successfully."
    }
    ```

#### 4. Get All Tickets (Experimental)

- **Endpoint Name**: `/tickets`
- **Method**: GET
- **Description**: Retrieves a list of all tickets in the database, including their details and status. While this endpoint serves as a convenient method for administrative overview, it is currently in an experimental stage and may not be fully tested.
- **Response**: An array of JSON objects, each representing a ticket with comprehensive details.
  - **Sample Response**:
    ```json
    [
        {
            "bot_battery_level": 35.5,
            "bot_hardware_version": "1.0.0",
            "bot_id": "f7fd06d4-841f-4b08-be49-7ada7ea9c793",
            "bot_location": "lat: 37.7749, lon: -72.612",
            "bot_software_version": "1.0.1",
            "bot_status": "busy",
            "problem_description": "Bot got stuck in mud.",
            "problem_type": "Field",
            "ticket_id": "aff0e6ba-f691-43bc-aa42-821fb6fdea14",
            "ticket_status": "IN PROGRESS"
        },
        {
            "bot_battery_level": 0.0,
            "bot_hardware_version": "1.0.0",
            "bot_id": "a6dfc6f2-4007-4b82-b1db-7dc301d2b4fc",
            "bot_location": "lat: -12.7675, lon: -122.4194",
            "bot_software_version": "1.0.1",
            "bot_status": "unavailable",
            "problem_description": "Bot battery drained completely.",
            "problem_type": "Hardware",
            "ticket_id": "08d46869-0188-42ef-a529-707bdbbfbb96",
            "ticket_status": "CLOSED"
        }
    ]
    ```

**Note**: The provided `/tickets` endpoint is an experimental feature intended for exploratory or administrative purposes and has not been tested. It is recommended to approach this feature with an understanding of its potential limitations.

---


### Additional Notes

- Ensure that the `Content-Type` header is set to `application/json` when sending requests to the API.
- Replace placeholder values such as `<ticket_id>` with actual data relevant to your operation.
- The response examples provided here are illustrative and may vary based on the actual data processed by the API.

---

