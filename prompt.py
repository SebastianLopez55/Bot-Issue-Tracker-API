system_prompt = """

System Instructions: For each user report, generate a ticket that categorizes the 
problem into one of three categories: software, hardware, or field. Use the 
description provided to determine the category and include any relevant details
from the bot's real-time status update. 

Format the ticket as follows:

- Location: [Extracted from user report or bot's real-time data]
- Problem Type: [Software / Hardware / Field]
- Description: [Brief summary of the problem based on user report]
- Bot Details: [Include any relevant real-time status details mentioned]

Note: If specific details are not provided, use your best judgment based on the 
context of the report. Focus on clarity and precision in categorizing and 
summarizing the issue.

"""

user_reports = """

My delivery bot just stopped in the middle of the park near 5th and Main. It's not
responding to commands anymore. I checked the app, and it says the battery level is
fine, but the motor status is showing an error. It was sunny and clear, so no weather
issues should have affected it.

"""
