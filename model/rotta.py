class Rotta:
    def __init__(self, airport1, airport2, distanza: int):
        self.airport1 = airport1
        self.airport2 = airport2
        self.distanza = distanza
        self.numVoli = 1

    def addVolo(self, distanza):
        self.distanza += distanza
        self.numVoli += 1

    def distanzaMedia(self):
        return self.distanza/self.numVoli