# database_sim.py
from datetime import datetime
from app import models
import uuid
import random


class SimulatedDatabase:
    lat1 = round(random.uniform(-90, 90), 4)
    lon2 = round(random.uniform(-180, 180), 4)

    def __init__(self):
        self.heartbeats = {}  # Stores heartbeat information indexed by bot_id
        self.tickets = {}  # Stores tickets indexed by ticket_id
        self._prepopulate_tickets()

    def _prepopulate_tickets(self):
        # Hardcoded tickets

        hardcoded_tickets = [
            models.Ticket(
                ticket_id=str(uuid.uuid4()),
                ticket_status="IN PROGRESS",
                problem_description="Bot got stuck in mud.",
                problem_type="Field",
                bot_id="f7fd06d4-841f-4b08-be49-7ada7ea9c793",
                bot_location=f"lat: 37.7749,, lon: {self.lon2}",
                bot_status="busy",
                bot_battery_level=35.5,
                bot_software_version="1.0.1",
                bot_hardware_version="1.0.0",
            ),
            models.Ticket(
                ticket_id=str(uuid.uuid4()),
                ticket_status="CLOSED",
                problem_description="Bot battery drained completely.",
                problem_type="Hardware",
                bot_id="a6dfc6f2-4007-4b82-b1db-7dc301d2b4fc",
                bot_location=f"lat: {self.lat1}, lon: -122.4194",
                bot_status="unavailable",
                bot_battery_level=0.0,
                bot_software_version="1.0.1",
                bot_hardware_version="1.0.0",
            ),
        ]
        for ticket in hardcoded_tickets:
            self.save_ticket(ticket)

    def update_heartbeat(self, heartbeat):
        self.heartbeats[heartbeat["bot_id"]] = heartbeat

    def get_heartbeat(self, bot_id):
        return self.heartbeats.get(bot_id, "Bot not in")

    def save_ticket(self, ticket):
        self.tickets[ticket.ticket_id] = ticket

    def get_ticket(self, ticket_id):
        return self.tickets.get(ticket_id, "Ticket not in database.")

    def update_ticket_status(self, ticket_id, new_status):
        ticket = self.get_ticket(ticket_id)
        if ticket and ticket != "Ticket not in database.":
            ticket.update_status(new_status)
            return True
        return False

    def get_all_tickets(self):
        return list(self.tickets.values())


lat = round(random.uniform(-90, 90), 4)
lon = round(random.uniform(-180, 180), 4)
battery_level = round(random.uniform(0, 100), 1)

# Initialize the simulated database instance
db_instance = SimulatedDatabase()
db_instance.update_heartbeat(
    {
        "bot_id": "bot_id",
        "timestamp": datetime.now(),
        "location": {"lat": lat, "lon": lon},
        "status": "busy",
        "battery_level": battery_level,
        "software_version": "1.0.1",
        "hardware_version": "1.0.0",
    }
)
