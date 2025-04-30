from dataclasses import dataclass
from tkinter import DoubleVar


@dataclass
class Airport:
    ID: int
    IATA_CODE: str
    AIRPORT: str
    CITY: str
    STATE: str
    COUNTRY: str
    LATITUDE: DoubleVar
    LONGITUDE: DoubleVar
    TIMEZONE_OFFSET: DoubleVar

    def __hash__(self):
        return self.ID

    def __str__(self):
        return f"{self.IATA_CODE}-{self.AIRPORT}"

    def __eq__(self, other):
        return self.ID == other.ID

