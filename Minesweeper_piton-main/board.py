import random
from piece import Piece

class Board: #tuk suzdavame class Board kojto shte otgovarq za poleto
    def __init__(self, size, prob): #suzdavame edin modul s vsichko nujno za poleto
        self.size = size #razmera mu
        self.prob = prob
        self.lost = False #promenliva za tovadali si zagubil
        self.numClicked = 0 #broq na kliknatite blokcheta
        self.numNonBombs = 0 #broq na kliknatite blokcheta koito ne sa bombi
        self.setBoard()

    def setBoard(self):
        self.board = [] #duskata e prazna
        for row in range(self.size[0]): #za daden red
            row = [] #reda e prazen
            for col in range(self.size[1]): #za dadena kolona
                hasBomb = random.random() < self.prob #tuk slagame bombite kato te sa na random i sa po-malko ot prosenta (prob) ot duskata
                if not hasBomb: #ako blokcheto ne e bomba
                    self.numNonBombs +=1 #nomera na blokchetata koito ne sa bomba se uvelichava
                piece = Piece(hasBomb) #blokcheto da e bomba
                row.append(piece) #oduljavame reda
            self.board.append(row) #oduljavamei poleto s broq na redovete
        self.setNeighbors()

    def setNeighbors(self):
        for row in range(self.size[0]): #koj red e
            for col in range(self.size[1]): #koq kolona e
                piece = self.getPiece((row, col)) #blokcheto vzima koordinatite si
                neighbors = self.getListOfNeighbors((row, col)) #koi sa susedite
                piece.setNeighbors(neighbors) #runvame modula dolu

    def getListOfNeighbors(self, index): #gledame koi sa susedite na nasheto blokche
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2): #oglejdame okolo nego - ref
            for col in range(index[1] - 1, index[1] + 2): #oglejdame okolo nego - kolona
                outOfBounds = row < 0 or row >= self.size[0] or col < 0 or col>= self.size[1] #gledame dali susedite mu sa izvun poleto(tova vaji za blokcheta koito sa "ramkata" na poleto
                same = row == index[0] and col == index [1] #gledame dali sa ednakvi na 2 blokcheta susedite
                if same or outOfBounds: #ako sa
                    continue #produljava
                neighbors.append(self.getPiece((row,col))) #oduljavame reda i kolonata na blokcheto
        return neighbors
    
    def getSize(self): #razmera
        return self.size
    
    def getPiece(self, index): #modul za tova koe e blokcheto
        return self.board[index[0]][index[1]]

    def handleClick(self, piece, flag):
        if piece.getClicked() or (not flag and piece.getFlagged()): #kakvo stava pri natisnat flag
            return
        if flag: #pri flag vrushtame nevuzmojnost za klik
            piece.toggleFlag()
            return #te vrushta gore
        piece.click()
        if piece.getHasBomb(): #ako sme natisnali blok kojto e s momba
            self.lost = True #znachi gubim
            return #te veushta gore
        self.numClicked +=1 #i natisnatite blokove se uvelichava s 1
        if piece.getNumAround() != 0: #ako nqma veche kude da natisnem
            return #te vrushta gore
        for neighbor in piece.getNeighbors(): #za susedno blokche
            if not neighbor.getHasBomb() and not neighbor.getClicked(): #ako susednoto blokche ne e bomba i ne e kliknato
                self.handleClick(neighbor, False) #znashi e nevqrno natiskaneto

    def getLost(self): #modul za tova koga gubish
        return self.lost #gubish kogato si natisnal bomba
        
    def getWon(self): #modul za tova koga pechelish
        return self.numNonBombs == self.numClicked #ako si nameril vsichki blokcheta koito ne sa mombi pechelish
