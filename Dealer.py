from Hand import Hand
class Dealer():
    def __init__(self):
        self._hand = Hand()
    def play_turn(self, deck):
        drawn_card = None
        while self._hand.total() < 17:
            card = deck.deal()
            self._hand._card.append(card)
            print(f"Dealer dealt the {card._Rank} of {card._Suit}")
            input(f"Dealer's hand: {self._hand.total()}")
            drawn_card = card
        return drawn_card