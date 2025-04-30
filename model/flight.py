from dataclasses import dataclass
from datetime import datetime
from tkinter import DoubleVar


@dataclass
class Flight:
    ID: int
    AIRLINE_ID: int
    FLIGHT_NUMBER: int
    TAIL_NUMBER: str
    ORIGIN_AIRPORT_ID: int
    DESTINATION_AIRPORT_ID: int
    SCHEDULED_DEPARTURE_DATE: datetime
    DEPARTURE_DELAY: DoubleVar
    ELAPSED_TIME: DoubleVar
    DISTANCE: int
    ARRIVAL_DATE: datetime
    ARRIVAL_DELAY: DoubleVar

    def __hash__(self):
        return self.ID

    def __str__(self):
        return f"{self.ID}-{self.AIRLINE_ID}-{self.FLIGHT_NUMBER}"

    def __eq__(self, other):
        return self.ID == other.ID
