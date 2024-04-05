import os
from dotenv import load_dotenv
import openai
import prompt

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key was found
if not api_key:
    raise ValueError(
        "API key not found. Ensure your .env file has the OPENAI_API_KEY variable."
    )

# Set the OpenAI API key for use in API calls
openai.api_key = api_key

# Create a chat completion
completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": prompt.system_prompt,
        },
        {
            "role": "user",
            "content": prompt.user_reports,
        },
    ],
)

# Print the generated message from the completion
message_content = completion.choices[0].message.content

# Breaking down the message into lines for better readability
lines = message_content.split("\n")

# Formatting and printing each line with annotations for clarity
print("\nTicket Summary:\n")
for line in lines:
    # Check if the line contains valuable information before printing
    if line.strip() != "":  # This removes any lines that are just whitespace
        # Here, you can customize how each line is displayed.
        # For example, adding "->" before each line item for clarity.
        print(f"{line}")
