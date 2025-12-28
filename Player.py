from Hand import Hand
import random
class Player():
    def __init__(self, name, balance, bet):
        self._name = name
        self._balance = balance
        self._bet = bet
        self._hand = Hand()
    def place_bet(self):
        dialogue_broke = ["You're too poor don't to make this bet! Try betting smaller.",
                        "You think chips grow on trees? You don't have enough!", 
                        "Ermm actually, {your_balance} is less than {your_bet}. No wonder you keep losing, you don't know simple arithmetic!", 
                        "You don't have enough balance to make this bet, please bet smaller."]
        while True:
            print(f"{self._name}'s current balance: {self._balance}")
            try:
                betting = int(input(f"Please insert bet here, {self._name}: "))
                if betting <= self._balance:
                    self._bet = betting #Lol, I was making the player bet his entire balance
                    return self._bet
                else:
                    broke = random.choice(dialogue_broke).format(your_balance = self._balance, your_bet = betting)
                    print(broke)
            except:
                print("Input must be an integer! Please enter a new bet, and make sure it is an integer.")
    def hit(self, deck):
        dealt_card = deck.deal()
        self._hand._card.append(dealt_card)
        return dealt_card
    def stand(self):
        return True