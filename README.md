
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
