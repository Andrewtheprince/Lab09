from dataclasses import dataclass
from tkinter import DoubleVar


@dataclass
class Airport:
    id: int
    iata_code: str
    airport: str
    city: str
    state: str
    country: str
    latitude: DoubleVar
    longitude: DoubleVar
    timezone_offset: DoubleVar

    def __hash__(self):
        return self.id

    def __str__(self):
        return f"{self.iata_code}-{self.airport}"

    def __eq__(self, other):
        return self.id == other.id

