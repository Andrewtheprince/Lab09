from dataclasses import dataclass
from datetime import datetime
from tkinter import DoubleVar


@dataclass
class Flight:
    id: int
    airline_id: int
    flight_number: int
    tail_number: str
    origin_airport_id: int
    destination_airport_id: int
    scheduled_departure_date: datetime
    departure_delay: DoubleVar
    elapsed_time: DoubleVar
    distance: int
    arrival_date: datetime
    arrival_delay: DoubleVar

    def __hash__(self):
        return self.id

    def __str__(self):
        return f"{self.id}-{self.airline_id}-{self.flight_number}"

    def __eq__(self, other):
        return self.id == other.id
