from Card import Card
import random

class Deck():
    def __init__(self):
        self._cards = []
        for suit in Card.legal_Suit:
            for rank in Card.legal_Rank:
                if rank == "Ace":
                    value = [1, 11]
                elif rank == "King" or rank == "Queen" or rank == "Jack":
                    value = 10
                else:
                    value = int(rank)
                play_card = Card(suit, rank, value)
                self._cards.append(play_card)

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self._cards.pop(0)