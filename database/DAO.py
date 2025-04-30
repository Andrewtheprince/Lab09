from database.DB_connect import DBConnect
from model.airport import Airport
from model.flight import Flight


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAirports():
        conn = DBConnect.get_connection()
        airports = []
        cursor = conn.cursor(dictionary = True)
        query = """SELECT * FROM airports a"""
        cursor.execute(query)
        for row in cursor:
            airports.append(Airport(**row))
        cursor.close()
        conn.close()
        return airports

    @staticmethod
    def getFlights():
        conn = DBConnect.get_connection()
        flights = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM flights f"""
        cursor.execute(query)
        for row in cursor:
            flights.append(Flight(**row))
        cursor.close()
        conn.close()
        return flights


