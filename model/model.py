from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._airports = DAO.getAirports()
        self._flights = DAO.getFlights()
        self._grafo = nx.DiGraph()

    def buildGraph(self, distanzaMassima):
        pass

    @property
    def archi(self):
        return self._grafo.edges

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)