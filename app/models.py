# models.py defines the data models of the application, representing the structure of database tables.


class Ticket:
    def __init__(
        self,
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
    ):
        self.ticket_id = ticket_id
        self.ticket_status = ticket_status
        self.problem_description = problem_description
        self.problem_type = problem_type
        self.bot_id = bot_id
        self.bot_location = bot_location
        self.bot_status = bot_status
        self.bot_battery_level = bot_battery_level
        self.bot_software_version = bot_software_version
        self.bot_hardware_version = bot_hardware_version

    def update_status(self, new_status):
        if new_status in ["OPEN", "IN PROGRESS", "CLOSED"]:
            self.ticket_status = new_status
        else:
            raise ValueError("Invalid status")
