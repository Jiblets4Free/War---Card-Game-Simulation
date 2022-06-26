from random import randint
import plotly.express as px

### EDWARDS IDEA

#I am going to attempt to do this recursively (ish), and plan for a GUI as well. Lets do this properly ;)
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

    ID = 0

    def __init__(self, Hand1: list[Card], Hand2: list[Card]):
        Round.ID += 1
        self._Hand1 = Hand1
        self._Hand2 = Hand2
        
    def Start(self):
        card1 = self._Hand1.pop(0)
        card2 = self._Hand2.pop(0)

        if card1 == card2:
            self.War(card1, card2)
        elif card1 > card2:
            self._Hand1.append(card1)
            self._Hand1.append(card2)
        else:  
            self._Hand2.append(card1)
            self._Hand2.append(card2)   
        if len(self._Hand1) > 0 and len(self._Hand2) > 0:
            return True, self._Hand1, self._Hand2
        return False, self._Hand1, self._Hand2

    def War(self, card1: Card, card2: Card):
        try:      
            p1Cards = self._GetWarCards(self._Hand1)
        except:
            p1Cards = []
        try:
            p2Cards = self._GetWarCards(self._Hand2)
        except:
            p2Cards = []

        discard = []
        while card1 == card2: #This is safe to call straight away, as we know card1 is already equal to card2
            discard += [card1, card2] #Puts the two similar cards into discard, then gets the next ones

            if len(p1Cards) == 0:
                try:
                    card1 = self._Hand1.pop(0)

                except:
                    self._Hand2 += discard
                    return
            else:
                card1 = p1Cards.pop(0)
            
            if len(p2Cards) == 0:
                try:
                    card2 = self._Hand2.pop(0)
                except:
                    self._Hand1 += discard
                    return
            else:
                card2 = p2Cards.pop(0)
        
        total = len(discard) + len(p2Cards) + len(p1Cards) + 2
        if card1 > card2:
            self._Hand1 += discard + [card1, card2] + p1Cards + p2Cards
        else:
            self._Hand2 += discard + [card1, card2] + p1Cards + p2Cards
        
    def _GetWarCards(self, Hand: list[Card]) -> list[Card]: #Just made this to avoid repetition
        cards = []
        for i in range(min(len(self._Hand1)-1, 3)): # -1 so that one card is left for comparison
            cards.append(Hand.pop(0))
        return cards

def Main() -> int:
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    cards = set() #Contains only unique elements, so we dont have to worry about checking if exists
    while len(cards) < 52:
        cards.add((randint(2, 14), suits[randint(0, len(suits)-1)]))
    CardList = []
    for value in cards:
        CardList.append(Card(value[1], value[0])) #Generate the cards
    Hand1 = CardList[:26]
    Hand2 = CardList[26:]
    del(CardList) #Not necessary, just gets rid of CardList as no longer needed
    Play = True
    while Play: #Recursion takes up too much memory, this is better
        round = Round(Hand1, Hand2)
        Play, Hand1, Hand2 = round.Start()
        print(f"Round: {Round.ID}", end="\r")
        if Round.ID >= 500:
            break
    return Round.ID


if __name__ == "__main__":
    number = int(input("How many games shall we simulate?: "))
    GameLengths = {}
    for i in range(number):
        num = Main()
        Round.ID = 0
        try:
            GameLengths[num] += 1
        except:
            GameLengths[num] = 1
    fig = px.bar(x=GameLengths.keys(), y=GameLengths.values())
    fig.show()



### PROBLEMS: None, that i can find. This game does seem to go on for ages though... 