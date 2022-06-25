from random import randint

#Suits = ["Clubs","Diamonds","Spades","Hearts"]
Suits = ["C","D","S","H"]

#Values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
Values = [1,2,3,4,5,6,7,8,9,10,11,12,13]

class Deck():
    def __init__(self):
        self.CardsList = []
        self.FillDeck()

    def DisplayCardsList(self):
        for card in self.CardsList:
            print(str(card[0]) + str(card[1]),end=" ")
        print()
    
    def FillDeck(self):
        self.CardsList = []
        for Suit in Suits:
            for Val in Values:
                self.CardsList.append([Suit,Val])

    def GetCardsListSize(self):
        return len(self.CardsList)

    def GetCardsList(self):
        return self.CardsList

    def PopCard(self,pos):
        return self.CardsList.pop(pos)

    def Shuffle(self):
        TempList = []
        for i in range(0,len(self.CardsList)):
            TempList.append(self.CardsList.pop(randint(0,len(self.CardsList) - 1)))
        self.CardsList = TempList

class Hand():
    def __init__(self):
        self.CardsList = []
    
    def AddCard(self,Card):
        self.CardsList.append(Card)
    
    def PopTopCard(self):
        return self.CardsList.pop(0)
    
    def DisplayCardsList(self):
        for card in self.CardsList:
            print(str(card[0]) + str(card[1]),end=" ")
        print()

def CompleteWarTurn():
    CardsPlayed = [Hand1.PopTopCard(),Hand2.PopTopCard()]
    if CardsPlayed[0][1] > CardsPlayed[1][1]:
        Hand1.AddCard(CardsPlayed[0])
        Hand1.AddCard(CardsPlayed[1])
        return
    elif CardsPlayed[0][1] < CardsPlayed[1][1]:
        Hand2.AddCard(CardsPlayed[0])
        Hand2.AddCard(CardsPlayed[1])
        return
    else:
        for i in range(0,3):
            CardsPlayed.append(Hand1.PopTopCard())
            CardsPlayed.append(Hand2.PopTopCard())
        ##NOT FINISHED
        return

if __name__ == "__main__":

    TheDeck = Deck()
    TheDeck.Shuffle()
    Hand1 = Hand()
    Hand2 = Hand()

    for i in range(0,TheDeck.GetCardsListSize()//2):
        Hand1.AddCard(TheDeck.PopCard(0))
        Hand2.AddCard(TheDeck.PopCard(TheDeck.GetCardsListSize()-1))

    if TheDeck.GetCardsListSize() != 0:
        print("Deck Size Error")




        
