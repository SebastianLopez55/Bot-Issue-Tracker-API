# Defines the data models of the application, representing the structure of database tables.
from datetime import datetime


class Heartbeat:
    def __init__(
        self,
        bot_id,
        location,
        status,
        battery_level,
        software_version,
        hardware_version,
    ):
        self.bot_id = bot_id
        self.timestamp = datetime.now()
        self.location = location
        self.status = status
        self.battery_level = battery_level
        self.software_version = software_version
        self.hardware_version = hardware_version


class Ticket:
    def __init__(
        self,
        ticket_id,
        problem_location,
        problem_type,
        summary,
        bot_details,
        bot_id,
        status="open",
    ):
        self.ticket_id = ticket_id
        self.problem_location = problem_location
        self.problem_type = problem_type
        self.summary = summary
        self.bot_details = bot_details
        self.bot_id = bot_id
        self.status = status
