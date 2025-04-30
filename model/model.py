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
            self._idAirports[a.ID] = a

    def buildGraph(self, distanzaMinima):
        self._grafo = nx.Graph()
        rotte = []
        for flight in self._flights:
            verifica = False
            for rotta in rotte:
                if ((flight.ORIGIN_AIRPORT_ID == rotta.airport1 and flight.DESTINATION_AIRPORT_ID == rotta.airport2) or
                    (flight.ORIGIN_AIRPORT_ID == rotta.airport2 and flight.DESTINATION_AIRPORT_ID == rotta.airport1)):
                    rotta.addVolo(flight.DISTANCE)
                    verifica = True
            if not verifica:
                rotte.append(Rotta(flight.ORIGIN_AIRPORT_ID, flight.DESTINATION_AIRPORT_ID, flight.DISTANCE))
        for rotta in rotte:
            if rotta.distanzaMedia() >= distanzaMinima:
                self._grafo.add_node(self._idAirports[rotta.airport1])
                self._grafo.add_node(self._idAirports[rotta.airport2])
                self._grafo.add_edge(str(self._idAirports[rotta.airport1]), str(self._idAirports[rotta.airport2]), weight=rotta.distanzaMedia())


    @property
    def archi(self):
        return self._grafo.edges

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)