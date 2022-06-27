import pygame
import os
from time import sleep

class Game:  #pravim class Game v kojto shte opishem vsichki vuzmojnosti v igrata 
    def __init__(self, board, screenSize):   #pravim edin modul v kojto definirame terminala (poleto) koeto shte izleze
        self.board = board #vuvejda se poleto
        self.screenSize = screenSize #tova ni e goleminata na ekrana
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]   #tuk delim za da poluchim kolko golqm trqbva dani e ekrana sprqmo displaya
        self.loadImages()  #tova zarejda snimkite za poleto
            
    def run(self):  #pravim edin modul kojto da runva poleto
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:  #tuk gledame kakvo stava s butonite
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #ako quitnem igrata de zatvarq taba
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN: #tuk opredelqme butonite s koito rabotim
                    position = pygame.mouse.get_pos() #kude sa
                    rightClick = pygame.mouse.get_pressed()[2] #s koj buton rabotim v nashiq sluchaj s desniq
                    self.handleClick(position, rightClick)
            self.draw() #tuk chertaem poleto
            pygame.display.flip()
            if self.board.getWon(): #tuk gledame vuzmojnosta pri pobeda na igrata
                sound = pygame.mixer.Sound("win.wav") #ako spechelish se puska zvuka za pobeda
                sound.play() #puskame zvuka tuk
                sleep(3) #malko zabavqne za da ne grumne terminala
                running = False #spira da raboti igrata
            if self.board.getLost(): #tuk gledame vuzmojnosta za zaguba na igrata
                sound = pygame.mixer.Sound("lose.mp3") #ako zagubish se puska zvuka za zaguba
                sound.play() #tuk puskame zvuka
                sleep(3) #leko zabavqne za da ne grumne terminala
                quit() #zatvarq terminala
        pygame.quit()
        
    def draw(self): #tuk chertaem poleto
        topLeft = (0, 0) #koordinatite na topleft blokcheto
        for row in range(self.board.getSize()[0]): #kude se namira blokcheto - red
            for col in range(self.board.getSize()[1]): #kude se namirakubcheto - kolona
                piece = self.board.getPiece((row, col)) #koordinatite na kubcheto
                image = self.getImage(piece) #kakva e snimkata na kubcheto(cifra ili prazno)
                self.screen.blit(image, topLeft) #populva vsichki poleta
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1] #sledvashtoto blokche veche(dobavqme koordinat na vsqko minalo)
            topLeft = 0, topLeft[1] + self.pieceSize[1] #sledvashto kubche tozi put dobavqme red

    def loadImages(self): #tuka zarejdame snimkite nujni za nasheto pole
        self.images = {} #lista v kojto sa
        for fileName in os.listdir("images"): #za da ne gi vkarvame pootdelno gi tursim v papkata
            if not fileName.endswith(".png"): #gledame kakuv e fajl extension-a v nashiq sluchaj e ".png"
                continue #produljava s drugite snimki
            image = pygame.image.load(r"images/" + fileName) #zarejda snimkite
            image = pygame.transform.scale(image, self.pieceSize) #place-va gi na poleto
            self.images[fileName.split(".")[0]] = image

    def getImage(self, piece): #tuk sa ostanalite snimki ot sorta na bomba ili flag, i gledame kakvo stava kato se natisnat
        string = None
        if piece.getClicked():
            string = "bomb-at-clicked-block" if piece.getHasBomb() else str(piece.getNumAround()) #gledame kude sa bili bombite
        else:
            string = "flag" if piece.getFlagged() else "empty-block" #gledame sluchaq v kojto si toglevash blokcheto za potencialna bomba
        return self.images[string]

    def handleClick(self, position, rightClick): #tuk razglejdame kude mojesh da natiskash
        if self.board.getLost():
            return
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)
