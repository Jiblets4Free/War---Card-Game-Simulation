import random
import fontTools
import pygame as pg
from os import path
import sys
import screeninfo

COLOURS = {
    "White": "#FFFFFF",
    "Black": "#000000",
    "Dark Green": "#164900",
    "Green": "#2E6E12",
    "Light Green": "#4E9231",
    "Pale Green": "#77B75B",
    "Very Pale Green": "#A8DB92"
    }

def resource_path(relative_path):
    "Gets the path for the resource relative to the base folder. Allows for assets to work within an executable"
    try:
        base_path = sys._MEIPASS
    except:
        base_path = path.abspath(".")

    return path.join(base_path, relative_path)

class SpriteSheet:
    def __init__(self, FileName: str, HorNumSprites: int, VertNumSprites: int):
        self._Image = pg.image.load(resource_path(FileName)).convert_alpha()
        Right = self._Image.get_size()[0] / HorNumSprites
        Down = self._Image.get_size()[1] / VertNumSprites
        self._Images = [[[]]*HorNumSprites]*VertNumSprites #type: list[list[list[pg.Surface]]]
        x, y = 0, 0
        print(self._Images)
        for i in range(HorNumSprites*VertNumSprites):
            self._Images[y][x] = pg.Surface((Right, Down)).convert_alpha()
            self._Images[y][x].blit(self._Image, (0, 0), (0, 0, x*Right, y*Down))
            x += 1
            if x >= HorNumSprites:
                y += 1
                x = 0
    
    def GetImage(self, PosRight: int, PosDown: int) -> pg.Surface:
        return self._Images[PosDown][PosRight]

class Image(pg.sprite.Sprite):

    def __init__(self, FilePath: str, border: bool, size=None, borderSize=2, borderColour="Black"):
        self.image = pg.image.load(resource_path(FilePath)).convert_alpha()
        if size:
            self.image = pg.transform.scale(self.image, size).convert_alpha()
        if border:
            pg.draw.rect(self.image, COLOURS[borderColour], )

class Rectangle(pg.sprite.Sprite):

    def __init__(self, colour: str, size: tuple[int, int], groups: list[pg.sprite.Group], pos: tuple, border: bool, borderSize=2, borderColour="Black"):
        super().__init__(groups)
        self.rect.center = pos
        self.rect.size = size
        self.image = pg.Surface(size)
        self._Border = border
        self._Colour = colour
        self._size = size
        self._BorderSize = borderSize
        self._BorderColour = borderColour
        if border:
            self.image.fill(borderColour)
            temp = pg.Surface((size[0]-(2*borderSize), size[1]-(2*borderSize))).fill(COLOURS[colour])
            self.image.blit(temp, (borderSize, borderSize))
        else:
            self.image.fill(COLOURS[colour])
    
    def GetSize(self) -> tuple:
        return self._size

class TextBox(Rectangle):

    def __init__(self, text: str, font: pg.font.Font, size: tuple, border: bool, pos: tuple, colour="White", textColour="Black", borderSize=2, borderColour="Black", groups: list[pg.sprite.Group]=[]):
        super().__init__(colour, size, groups, pos, border, borderSize, borderColour)
        self._Text = text
        self._TextColour = textColour
        self._Font = font
        self._RenderedText = font.render(text, True, textColour)
        self._Text_x = (size[0] / 2) - (self._RenderedText.get_rect().size[0]/2)
        self._Text_y = (size[1] / 2) - (self._RenderedText.get_rect().size[1]/2)
    
    def _DrawText(self):
        self.image.blit(self._RenderedText, (self._Text_x, self._Text_y))

class ScrollingTextBox(TextBox):

    def __init__(self, text: str, font: pg.font.Font, size: tuple, border: bool, pos: tuple, colour="White", textColour="Black", borderSize=2, borderColour="Black", groups: list[pg.sprite.Group] = []):
        super().__init__(text, font, size, border, pos, colour, textColour, borderSize, borderColour, groups)
        self._CurrentText = ""
        self._CurrentIndex = 1
        self._ScrollSpeed = 5
        self._Counter = 0

    def update(self):
        if self._CurrentIndex > len(self._CurrentText):
            return
        self._Counter += 1
        if self._Counter % 5 == 0:
            self._CurrentText = self._Text[:self._CurrentIndex]
            self._CurrentIndex += 1
            if self._Border:
                self.image.fill(self._BorderColour)
                temp = pg.Surface((self._size[0]-(2*self._BorderSize), self._size[1]-(2*self._BorderSize))).fill(COLOURS[self._Colour])
                self.image.blit(temp, (self._BorderSize, self._BorderSize))
            else:
                self.image.fill(COLOURS[self._Colour])
            self.image.blit(self._Font.render(self._CurrentText, True, self._TextColour), (self._Text_x, self._Text_y))

class Button(TextBox):
    ID = 0
    def __init__(self, text: str, font: pg.font.Font, size: tuple, border: bool, colour: str, highlightColour: str, pos: tuple, borderSize=2, borderColour="Black", groups: list[pg.sprite.Group]=[]):
        self._ID = Button.ID
        Button.ID += 1
        super().__init__(text, font, size, groups, border, pos, colour, borderSize, borderColour)
        self._DrawText()
        self._Highlighted = False
        self._HighlightColour = highlightColour
    
    def Get_ID(self) -> int:
        return self._ID
    
    def Highlight(self):
        self._Highlighted = True
    
    def update(self):
        if self._Highlighted:
            colour = self._HighlightColour
        else:
            colour = self._Colour
        if self._Border:
            self.image.fill(self._BorderColour)
            temp = pg.Surface((self._size[0]-(2*self._BorderSize), self._size[1]-(2*self._BorderSize))).fill(COLOURS[colour])
            self.image.blit(temp, (self._BorderSize, self._BorderSize))
        else:
            self.image.fill(COLOURS[colour])
        self._DrawText()


class Card:
    def __init__(self, suit: str, value: int):
        self._Suit = suit
        if self._Suit == "Hearts":
            suitValue = 0
        elif self._Suit == "Diamonds":
            suitValue = 1
        elif self._Suit == "Clubs":
            suitValue = 2
        elif self._Suit == "Spades":
            suitValue = 3
        self._NumericValue = value #This value is used for comparison
        if self._NumericValue == 11:
            self._CardValue = "Jack"
        elif self._NumericValue == 12:
            self._CardValue = "Queen"
        elif self._NumericValue == 13:
            self._CardValue = "King"
        elif self._NumericValue == 14:
            self._CardValue = "Ace"
        else:
            self._CardValue = str(self._NumericValue)
        self._Flipped = False
        self._Flipping = True
        if self._NumericValue == 14:
            self._FlippedImage = SPRITESHEET.GetImage(0, suitValue)
        else:
            self._FlippedImage = SPRITESHEET.GetImage(self._NumericValue -1, suitValue)
    
    def GetNumericValue(self) -> int: #Used for comparison
        return self._NumericValue
    
    def __repr__(self) -> str: #Used by print(Card)
        return self._CardValue + " of " + self._Suit

    def __gt__(self, card: "Card") -> bool: #Used by Card > Card
        return self._NumericValue > card.GetNumericValue()
    
    def __eq__(self, card: "Card") -> bool: #Used by Card == Card
        return self._NumericValue == card.GetNumericValue()

class Round:

    ID = 1

    def __init__(self, Hand1: list[Card], Hand2: list[Card]):
        print(f"Round {Round.ID}")
        Round.ID += 1
        self._Hand1 = Hand1
        self._Hand2 = Hand2
        
    def Start(self):
        print(f"PLAYER 1 has {len(self._Hand1)} cards left")
        print(f"PLAYER 2 has {len(self._Hand2)} cards left")
        card1 = self._Hand1.pop(0)
        card2 = self._Hand2.pop(0)
        print(f"Player 1 played {card1}")
        print(f"Player 2 played {card2}")

        if card1 == card2:
            self.War(card1, card2)
        elif card1 > card2:
            print("Player 1 wins and takes both cards")
            self._Hand1.append(card1)
            self._Hand1.append(card2)
        else:
            print("Player 2 wins and takes both cards")     
            self._Hand2.append(card1)
            self._Hand2.append(card2)   
        if len(self._Hand1) > 0 and len(self._Hand2) > 0:
            return True, self._Hand1, self._Hand2
        return False, self._Hand1, self._Hand2

    def War(self, card1: Card, card2: Card):    
        print("WAR!")    
        p1Cards = self._GetWarCards(self._Hand1)
        p2Cards = self._GetWarCards(self._Hand2)

        print(f"Player 1 has {len(p1Cards)} card/s face down!") #Can differ, if one player only has
        print(f"Player 2 has {len(p2Cards)} card/s face down!") #a few cards left

        discard = []
        while card1 == card2: #This is safe to call straight away, as we know card1 is already equal to card2
            discard += [card1, card2] #Puts the two similar cards into discard, then gets the next ones

            if len(p1Cards) == 0:
                try:
                    card1 = self._Hand1.pop(0)
                    print("Another card has been drawn from player 1s hand!")
                except:
                    print("Player 1 has run out of cards!")
                    self._Hand2 += discard
                    return
            else:
                card1 = p1Cards.pop(0)
            
            if len(p2Cards) == 0:
                try:
                    card2 = self._Hand2.pop(0)
                    print("Another card has been drawn from player 2s hand!")
                except:
                    print("Player 2 has run out of cards!")
                    self._Hand1 += discard
                    return
            else:
                card2 = p2Cards.pop(0)
            
            print(f"Player 1 played {card1}")
            print(f"Player 2 played {card2}")
        
        total = len(discard) + len(p2Cards) + len(p1Cards) + 2
        if card1 > card2:
            print(f"Player 1 has won this round and taken the {total} cards!")
            self._Hand1 += random.shuffle(discard + [card1, card2] + p1Cards + p2Cards) #Shuffled to make the game finite
        else:
            print(f"Player 2 has won this round and taken the {total} cards!")
            self._Hand2 += random.shuffle(discard + [card1, card2] + p1Cards + p2Cards)
        
    def _GetWarCards(self, Hand: list[Card]) -> list[Card]: #Just made this to avoid repetition
        cards = []
        for i in range(min(len(self._Hand1)-1, 3)): # -1 so that one card is left for comparison
            cards.append(Hand.pop(0))
        return cards

class Game:

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        cards = set() #Contains only unique elements, so we dont have to worry about checking if exists
        while len(cards) < 52:
            cards.add((random.randint(2, 14), suits[random.randint(0, len(suits)-1)]))
        CardList = []
        for value in cards:
            CardList.append(Card(value[1], value[0])) #Generate the cards
        self._Hand1 = CardList[:26]
        self._Hand2 = CardList[26:]

    def PlayGame(self):
        Play = True
        while Play: #Recursion takes up too much memory, this is better
            Play, Hand1, Hand2 = Round(Hand1, Hand2).Start()

    def _DrawMenu(self):
        pass

class MainMenu:

    def __init__(self, PlayedBefore: bool, HighestScore: str, FastestWin: str, GamesPlayed: str):
        self._BackgroundImage = pg.transform.scale(pg.image.load(resource_path("WAR.png")), SCREENSIZE)
        self._HighestScore = HighestScore
        self._FastestWin = FastestWin
        self._GamesPlayed = GamesPlayed
        self._ButtonActions = {
            0: self._PlayGame,
            1: self._Exit,
        }
        self._ButtonGroup = pg.sprite.Group()
        self._StatsGroup = pg.sprite.Group()
        text = f"Highest Score: {HighestScore} \n Fastest Win: {FastestWin} \n, Total Games Played: {GamesPlayed}"
        Textbox = TextBox(text, FONTS[1], (200, 100), True, (SCREENSIZE[0]-200, 0), "Green", "Pale Green", 2, "Black", self._StatsGroup)
        Button1 = Button("Play Game", FONTS[0], (100, 50), True, "Dark Green", "Light Green", (SCREENSIZE[0]/2, SCREENSIZE[1]/2), 2, "Black", self._ButtonGroup)
        Button2 = Button("Exit", FONTS[0], (100, 50), True, "Dark Green", "Light Green", ((SCREENSIZE[0]/2)-200, SCREENSIZE[1]/2), 2, "Black", self._ButtonGroup)

    def _PlayGame(self):
        return self._HighestScore, self._FastestWin, True

    def _Exit(self):
        return self._HighestScore, self._FastestWin, False
    
    def Run(self) -> tuple[str, str, bool]:
        while True:
            SCREEN.fill(COLOURS["Black"])
            SCREEN.blit(self._BackgroundImage, (0, 0))
            self._ButtonGroup.update()
            self._StatsGroup.update()
            self._ButtonGroup.draw(SCREEN)
            self._StatsGroup.draw(SCREEN)
            mousePos = pg.mouse.get_pos()
            button = GetPointCollisions(mousePos, self._ButtonGroup)
            if button is not None:
                button.Highlight()
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if button is not None:
                        self._ButtonActions[button.Get_ID()]()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return self._Exit()
                    

def GetPointCollisions(point: tuple[int, int], SpriteGroup: pg.sprite.Group) -> pg.sprite.Sprite | None:
    for sprite in SpriteGroup:
        if sprite.rect.collidepoint(point[0], point[1]):
            return sprite

def Main():
    pg.init()

    global PRIMARY_MONITOR
    MONITORS = screeninfo.get_monitors()
    PRIMARY_MONITOR = None
    for monitor in MONITORS:
        if monitor.is_primary:
            PRIMARY_MONITOR = monitor 
            global SCREENSIZE
            SCREENSIZE = (PRIMARY_MONITOR.width, PRIMARY_MONITOR.height)
            break

    global SCREEN
    SCREEN = pg.display.set_mode((PRIMARY_MONITOR.width, PRIMARY_MONITOR.height))
    pg.display.set_caption("WAR", "WAR")

    global SPRITESHEET
    SPRITESHEET = SpriteSheet("cards.png", 13, 5)

    pg.display.set_icon(SPRITESHEET.GetImage(0, 4))

    global GAME
    GAME = Game()

    global FONTS 
    FONTS = []
    for i in range(1, 5):
        FONTS.append(pg.font.Font(resource_path("Abel-Regular.ttf"), i*8))

    PlayedBefore = False
    try:
        with open("save.SAVE", "w+") as f:
            info = f.readlines()
            HighestScore = info[0]
            FastestWin = info[1]
            PlayedBefore = True
    except FileNotFoundError:
        with open(resource_path("save.SAVE"), "w") as f:
            f.writelines(["0", "0"])
            HighestScore = "0"
            FastestWin = "Never" 

    playing = True
    while playing:
        MAINMENU = MainMenu(PlayedBefore, HighestScore, FastestWin)
        playing, HighestScore, FastestWin = MAINMENU.Run()


if __name__ == "__main__":
    Main()