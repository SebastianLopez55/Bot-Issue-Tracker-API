import os
from dotenv import load_dotenv
import openai

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
            "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
        },
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming.",
        },
    ],
)

# Print the generated message from the completion
print("\n", completion.choices[0].message)
