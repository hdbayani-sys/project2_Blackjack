class Card():
    legal_Suit = ("Clubs", "Spades", "Hearts", "Diamonds")
    legal_Rank = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
    legal_Value = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    def __init__(self, Suit, Rank, Value):
        self._Suit = Suit
        self._Rank = Rank
        self._Value = Value
