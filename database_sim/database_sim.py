# database_sim.py
from datetime import datetime
import uuid


class SimulatedDatabase:
    def __init__(self):
        self.heartbeats = {}  # Stores heartbeat information indexed by bot_id
        self.tickets = {}  # Stores tickets indexed by ticket_id

    def update_heartbeat(self, heartbeat):
        self.heartbeats[heartbeat["bot_id"]] = heartbeat

    def get_heartbeat(self, bot_id):
        return self.heartbeats.get(bot_id, None)

    def save_ticket(self, ticket):
        self.tickets[ticket.ticket_id] = ticket

    def get_ticket(self, ticket_id):
        return self.tickets.get(ticket_id, None)


# Initialize the simulated database instance
db_instance = SimulatedDatabase()
db_instance.update_heartbeat(
    {
        "bot_id": "bot_1",
        "timestamp": datetime.now(),
        "location": {"lat": 37.7749, "lon": -122.4194},
        "status": "busy",
        "battery_level": 75.0,
        "software_version": "1.0.1",
        "hardware_version": "1.0.0",
    }
)
