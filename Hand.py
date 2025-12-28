class Hand():
    def __init__(self):
        self._card = []    
    def total(self):
        A_count = 0
        summation = 0
        for card in self._card:
            if card._Rank == "Ace": #syntax error. rank instead of _Rank
                    summation += 11
                    A_count += 1
            else:
                summation += card._Value #syntax error. value instead of _Value
        while A_count > 0 and summation > 21:
            summation -= 10
            A_count -= 1
        return summation
    def is_blackjack(self):
        if self.total() == 21 and len(self._card) == 2:
            return True
        else:
            return False
    def is_bust(self):
        if self.total() > 21:
            return True
        else:
            return False