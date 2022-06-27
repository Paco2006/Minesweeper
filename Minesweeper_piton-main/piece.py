class Piece: #suzdavane class Piece kojto e za tova da opredeli vsqko ot blokchetata i kakvo stava ako sa kliknati
    def __init__(self, hasBomb): #modul kojto opredelq kakvo e vsqko ot blokchetata
        self.hasBomb = hasBomb #bombata si e bomba
        self.clicked = False #ne e kliknato blokcheto
        self.flagged = False #ne e flaggnato blokcheto

    def getHasBomb(self): #dali e bba blokcheto
        return self.hasBomb

    def getClicked(self): #dali e kliknato blokcheto
        return self.clicked

    def getFlagged(self): #dali e flaggnato blokcheto
        return self.flagged

    def setNeighbors(self, neighbors): #koi sa mu susedite
        self.neighbors = neighbors #susedite mu
        self.setNumAround()

    def setNumAround(self):
        self.numAround = 0
        for piece in self.neighbors:
            if piece.getHasBomb():
                self.numAround += 1

    def getNumAround(self):
        return self.numAround

    def toggleFlag(self): #dali si kliknal blokcheto da e flag
        self.flagged = not self.flagged #ako e flagg-nato i ako ne e flagg-nato sa ravni

    def click(self): #dali blokcheto e kliknato
        self.clicked = True #vqrno e che e kliknato
        
    def getNeighbors(self): #kude sa susedite
        return self.neighbors
