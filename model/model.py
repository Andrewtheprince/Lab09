from database.DAO import DAO
import networkx as nx

from model.rotta import Rotta


class Model:
    def __init__(self):
        self._airports = DAO.getAirports()
        self._flights = DAO.getFlights()
        self._grafo = nx.Graph()
        self._idAirports = {}
        for a in self._airports:
            self._idAirports[a.id] = a

    def buildGraph(self, distanzaMinima):
        rotte = []
        for flight in self._flights:
            verifica = False
            for rotta in rotte:
                if ((flight.origin_airport_id == rotta.airport1 and flight.destination_airport_id == rotta.airport2) or
                    (flight.origin_airport_id == rotta.airport2 and flight.destination_airport_id == rotta.airport1)):
                    rotta.addVolo(flight.distance)
                    verifica = True
            if not verifica:
                rotte.append(Rotta(flight.origin_airport_id, flight.destination_airport_id, flight.distance))
        for rotta in rotte:
            if rotta.distanzaMedia() >= distanzaMinima:
                self._grafo.add_node(self._idAirports[rotta.airport1])
                self._grafo.add_node(self._idAirports[rotta.airport2])
                self._grafo.add_edge(self._idAirports[rotta.airport1], self._idAirports[rotta.airport2], weight=rotta.distanzaMedia())


    @property
    def archi(self):
        return self._grafo.edges

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)