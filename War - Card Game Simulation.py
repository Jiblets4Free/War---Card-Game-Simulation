from random import randint

#Suits = ["Clubs","Diamonds","Spades","Hearts"]
Suits = ["C","D","S","H"]

#Values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
Values = [1,2,3,4,5,6,7,8,9,10,11,12,13]

#Perhaps Deck and Hand should both inherit from a super class as they have a lot in common.
class Deck():
    def __init__(self):
        self.CardsList = []
        self.FillDeck()

    #A nicer print statement.
    def DisplayCardsList(self):
        for card in self.CardsList:
            print(str(card[0]) + str(card[1]),end=" ")
        print()
    
    #This fills the deck entirely in order.
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

    #AQA wish.
    def Shuffle(self):
        TempList = []
        while len(self.CardsList) > 1:
            TempList.append(self.CardsList.pop(randint(0,len(self.CardsList) - 1)))
        self.CardsList = TempList + self.CardsList

class Hand():
    def __init__(self):
        self.CardsList = []
    
    #Adds to the back of the List
    def AddCard(self,Card):
        self.CardsList.append(Card)
    
    def PopTopCard(self):
        return self.CardsList.pop(0)
    
    def GetNumberOfCards(self):
        return len(self.CardsList)

    # Made so that "12" takes up the same space as "1 " by adding spaces for a more clear print.
    def DisplayCardsList(self):
        for card in self.CardsList:
            if len(str(card[1])) == 1:
                print(str(card[0]) + str(card[1]),end="  ")
            else:
                print(str(card[0]) + str(card[1]),end=" ")


## This simulates one turn.
def CompleteWarTurn():
    CardsPlayed = [Hand1.PopTopCard(),Hand2.PopTopCard()]
    if CardsPlayed[0][1] > CardsPlayed[1][1]:
        Hand1.AddCard(CardsPlayed[0])
        Hand1.AddCard(CardsPlayed[1])
        #print("1")

    elif CardsPlayed[0][1] < CardsPlayed[1][1]:
        Hand2.AddCard(CardsPlayed[0])
        Hand2.AddCard(CardsPlayed[1])
        #print("2")

    else:

        #What if war occurs when a player doesnt have enough cards to do one?
        #print("war")
        for i in range(0,3):
            CardsPlayed.append(Hand1.PopTopCard())
            CardsPlayed.append(Hand2.PopTopCard())

        if CardsPlayed[-2][1] > CardsPlayed[-1][1]:
            for Card in CardsPlayed:
                Hand1.AddCard(Card)

        elif CardsPlayed[-2][1] < CardsPlayed[-1][1]:
            for Card in CardsPlayed:
                Hand2.AddCard(Card)   

        else:
            if CardsPlayed[-4][1] > CardsPlayed[-3][1]:
                for Card in CardsPlayed:
                    Hand1.AddCard(Card)

            elif CardsPlayed[-4][1] < CardsPlayed[-3][1]:
                for Card in CardsPlayed:
                    Hand2.AddCard(Card)

            else:
                if CardsPlayed[-6][1] > CardsPlayed[-5][1]:
                    for Card in CardsPlayed:
                        Hand1.AddCard(Card)

                elif CardsPlayed[-6][1] < CardsPlayed[-5][1]:
                    for Card in CardsPlayed:
                        Hand2.AddCard(Card)

                else:
                    print("GG")
                    ## If they drew on all cards, split the played cards and give each hand half.
                    for i in range(0,len(CardsPlayed)/2):
                        Hand1.AddCard(CardsPlayed[i])
                        Hand2.AddCard(CardsPlayed[len(CardsPlayed)-i])


if __name__ == "__main__":

    TheDeck = Deck()
    TheDeck.Shuffle()
    Hand1 = Hand()
    Hand2 = Hand()

    ## Splits the deck evenly into the two hands.
    for i in range(0,TheDeck.GetCardsListSize()//2):
        Hand1.AddCard(TheDeck.PopCard(0))
        Hand2.AddCard(TheDeck.PopCard(TheDeck.GetCardsListSize()-1))

    if TheDeck.GetCardsListSize() != 0:
        print("Deck Size Error")

    #Pre simulation Data
    print("Starting Hand 1: ",end="")
    Hand1.DisplayCardsList()
    print("  Size: ",end="")
    print(Hand1.GetNumberOfCards())

    print("Starting Hand 2: ",end="")
    Hand2.DisplayCardsList()
    print("  Size: ",end="")
    print(Hand2.GetNumberOfCards())

    ## SIMULATION ##
    while Hand1.GetNumberOfCards() > 0 and Hand2.GetNumberOfCards() > 0:
        CompleteWarTurn()
    
    #Post simluation Data
    print("\nEnding Hand 1: ",end="")
    Hand1.DisplayCardsList()
    print("  Size: ",end="")
    print(Hand1.GetNumberOfCards())

    print("Ending Hand 2: ",end="")
    Hand2.DisplayCardsList()
    print("  Size: ",end="")
    print(Hand2.GetNumberOfCards())
    

## PROBLEMS

# Often the simulation loops infinitely, it seems like this war will never end... :D
# There are out of range errors if a war occurs when one player does not have enough cards to partake in one.



        
