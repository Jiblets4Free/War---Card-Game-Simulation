from random import randint

##Suits = ["Clubs","Diamonds","Spades","Hearts"]
#Suits = ["C","D","S","H"]
#
##Values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
#Values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#
##Perhaps Deck and Hand should both inherit from a super class as they have a lot in common.
#class Deck():
#    def __init__(self):
#        self.CardsList = []
#        self.FillDeck()
#
#    #A nicer print statement.
#    def DisplayCardsList(self):
#        for card in self.CardsList:
#            print(str(card[0]) + str(card[1]),end=" ")
#        print()
#    
#    #This fills the deck entirely in order.
#    def FillDeck(self):
#        self.CardsList = []
#        for Suit in Suits:
#            for Val in Values:
#                self.CardsList.append([Suit,Val])
#
#    def GetCardsListSize(self):
#        return len(self.CardsList)
#
#    def GetCardsList(self):
#        return self.CardsList
#
#    def PopCard(self,pos):
#        return self.CardsList.pop(pos)
#
#    #AQA wish.
#    def Shuffle(self):
#        TempList = []
#        while len(self.CardsList) > 1:
#            TempList.append(self.CardsList.pop(randint(0,len(self.CardsList) - 1)))
#        self.CardsList = TempList + self.CardsList
#
#class Hand():
#    def __init__(self):
#        self.CardsList = []
#    
#    #Adds to the back of the List
#    def AddCard(self,Card):
#        self.CardsList.append(Card)
#    
#    def PopTopCard(self):
#        return self.CardsList.pop(0)
#    
#    def GetNumberOfCards(self):
#        return len(self.CardsList)
#
#    # Made so that "12" takes up the same space as "1 " by adding spaces for a more clear print.
#    def DisplayCardsList(self):
#        for card in self.CardsList:
#            if len(str(card[1])) == 1:
#                print(str(card[0]) + str(card[1]),end="  ")
#            else:
#                print(str(card[0]) + str(card[1]),end=" ")
#
#
### This simulates one turn.
#def CompleteWarTurn():
#    CardsPlayed = [Hand1.PopTopCard(),Hand2.PopTopCard()]
#    if CardsPlayed[0][1] > CardsPlayed[1][1]:
#        Hand1.AddCard(CardsPlayed[0])
#        Hand1.AddCard(CardsPlayed[1])
#        #print("1")
#
#    elif CardsPlayed[0][1] < CardsPlayed[1][1]:
#        Hand2.AddCard(CardsPlayed[0])
#        Hand2.AddCard(CardsPlayed[1])
#        #print("2")
#
#    else:
#
#        #What if war occurs when a player doesnt have enough cards to do one?
#        #print("war")
#        for i in range(0,3):
#            CardsPlayed.append(Hand1.PopTopCard())
#            CardsPlayed.append(Hand2.PopTopCard())
#
#        if CardsPlayed[-2][1] > CardsPlayed[-1][1]:
#            for Card in CardsPlayed:
#                Hand1.AddCard(Card)
#
#        elif CardsPlayed[-2][1] < CardsPlayed[-1][1]:
#            for Card in CardsPlayed:
#                Hand2.AddCard(Card)   
#
#        else:
#            if CardsPlayed[-4][1] > CardsPlayed[-3][1]:
#                for Card in CardsPlayed:
#                    Hand1.AddCard(Card)
#
#            elif CardsPlayed[-4][1] < CardsPlayed[-3][1]:
#                for Card in CardsPlayed:
#                    Hand2.AddCard(Card)
#
#            else:
#                if CardsPlayed[-6][1] > CardsPlayed[-5][1]:
#                    for Card in CardsPlayed:
#                        Hand1.AddCard(Card)
#
#                elif CardsPlayed[-6][1] < CardsPlayed[-5][1]:
#                    for Card in CardsPlayed:
#                        Hand2.AddCard(Card)
#
#                else:
#                    print("GG")
#                    ## If they drew on all cards, split the played cards and give each hand half.
#                    for i in range(0,len(CardsPlayed)/2):
#                        Hand1.AddCard(CardsPlayed[i])
#                        Hand2.AddCard(CardsPlayed[len(CardsPlayed)-i])
#
#
#if __name__ == "__main__":
#
#    TheDeck = Deck()
#    TheDeck.Shuffle()
#    Hand1 = Hand()
#    Hand2 = Hand()
#
#    ## Splits the deck evenly into the two hands.
#    for i in range(0,TheDeck.GetCardsListSize()//2):
#        Hand1.AddCard(TheDeck.PopCard(0))
#        Hand2.AddCard(TheDeck.PopCard(TheDeck.GetCardsListSize()-1))
#
#    if TheDeck.GetCardsListSize() != 0:
#        print("Deck Size Error")
#
#    #Pre simulation Data
#    print("Starting Hand 1: ",end="")
#    Hand1.DisplayCardsList()
#    print("  Size: ",end="")
#    print(Hand1.GetNumberOfCards())
#
#    print("Starting Hand 2: ",end="")
#    Hand2.DisplayCardsList()
#    print("  Size: ",end="")
#    print(Hand2.GetNumberOfCards())
#
#    ## SIMULATION ##
#    while Hand1.GetNumberOfCards() > 0 and Hand2.GetNumberOfCards() > 0:
#        CompleteWarTurn()
#    
#    #Post simluation Data
#    print("\nEnding Hand 1: ",end="")
#    Hand1.DisplayCardsList()
#    print("  Size: ",end="")
#    print(Hand1.GetNumberOfCards())
#
#    print("Ending Hand 2: ",end="")
#    Hand2.DisplayCardsList()
#    print("  Size: ",end="")
#    print(Hand2.GetNumberOfCards())
#    
#
### PROBLEMS
#
## Often the simulation loops infinitely, it seems like this war will never end... :D
## There are out of range errors if a war occurs when one player does not have enough cards to partake in one.


### EDWARDS IDEAS

#I am going to attempt to do this recursively, and plan for a GUI as well. Lets do this properly ;)
#On top of that, I think we should work on turning this into a full game, and releasing it too.
#I can do all the paperwork, although help with the short design documents would be appreciated

class Card:
    def __init__(self, suit: str, value: int):
        self._Suit = suit
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
        print(f"Player 1 has {len(p1Cards)} card/s face down!")
        print(f"Player 2 has {len(p2Cards)} card/s face down!")

        discard = []
        while card1 == card2:
            discard += [card1, card2]
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
        
        if card1 > card2:
            print(f"Player 1 has won this round and taken the {len(discard)+2} cards!")
            self._Hand1 += discard + [card1, card2] + p1Cards + p2Cards
        else:
            print(f"Player 2 has won this round and taken the {len(discard)+2} cards!")
            self._Hand2 += discard + [card1, card2] + p1Cards + p2Cards
        
    def _GetWarCards(self, Hand: list[Card]) -> list[Card]:
        cards = []
        for i in range(min(len(self._Hand1)-1, 3)): # -1 so that one card is left for comparison
            cards.append(Hand.pop(0))
        return cards

def Main():
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    cards = set()
    while len(cards) < 52:
        cards.add((randint(2, 14), suits[randint(0, len(suits)-1)]))
    CardList = []
    for value in cards:
        CardList.append(Card(value[1], value[0]))
    Hand1 = CardList[:26]
    Hand2 = CardList[26:]
    del(CardList)
    print("Setup finished")
    input("Ready? :)")
    Play = True
    while Play:
        Play, Hand1, Hand2 = Round(Hand1, Hand2).Start()
        if input(":") == "":
            continue
        else:
            break
    if len(Hand1) == 0:
        print("Player 2 has won the game!")
    else:
        print("Player 1 has won the game!")


if __name__ == "__main__":
    Main()