from Card import Card
from Deck import Deck
from Hand import Hand
from Player import Player
from Dealer import Dealer
import random
class BlackjackGame():
    def __init__(self):
        self._players = []
        self._dealer = Dealer()
        self._deck = Deck()
        self._round_number = 0
        pass
    def start(self):
        self.setup_players() #only this is working
        while len(self._players) != 0: #removed the condition that ask_continue == True
            self._deck.shuffle()
            self.place_bets()
            self.initial_deal()
            self.run_player_turns()
            self.run_dealer_turn()
            self.resolve_round()
            self.eliminate_broke_players()
            self.ask_continue() #only this is working

    def setup_players(self):
        while True:
            try:
                num_players = int(input("Insert number of players. Min. no. of players: 1, Max no. of players: 7.: "))
                if 0 < num_players < 8:
                    break
                else:
                    if num_players < 1:
                        print("No one's playing! Please input a reasonable value.")
                    elif num_players > 7:
                        print("Too many players to accomodate! Please input a reasonable value.")
            except:
                print("Invalid input! Please enter a number that is more than 0 and less than 8, please.")
        for i in range(num_players):
            player = Player(name = f"Player_{i+1}", balance = 10000, bet = 0)
            self._players.append(player)

    def place_bets(self):
        for each_player in self._players:
            each_player.place_bet()

    def initial_deal(self): #inital totals were calculated before the card was appended. Solution: I appended the card first before getting the total.
        dealing_dialogue = ["Eyes up, {player}! You're given the {Rank} of {Suit}!",
                         "{player} was given the {Rank} of {Suit}.", 
                         "A {Rank} of {Suit} has spwaned in the {player}'s hand!",
                         "{Rank} of {Suit}, {player} has chosen you!"]
        d_dealing_dialogue = ["Attention, players! The dealer's dealt himself the {Rank} of {Suit}.",
                              "Dealer drew the {Rank} of {Suit}. Take notes inside your head.",
                              "Alright people, the dealer has the {Rank} of {Suit}. Got it?"]
        self._round_number += 1
        print(f"Round {self._round_number}")
        for i in range(2):
            for each_player in self._players:
                hand_cards = each_player._hand._card
                dealt = self._deck.deal()
                dealing = random.choice(dealing_dialogue).format(player = each_player._name, Rank = dealt._Rank, Suit = dealt._Suit)
                input(dealing)
                hand_cards.append(dealt)
                init_total = each_player._hand.total()
                input(f"{each_player._name}'s total: {init_total}")
            d_hand_cards = self._dealer._hand._card
            d_dealt = self._deck.deal()
            if i == 0:
                d_dealing = random.choice(d_dealing_dialogue).format(Rank = d_dealt._Rank, Suit = d_dealt._Suit)
                print(d_dealing)
                input(f"Dealer has drawn the {d_dealt._Rank} of {d_dealt._Suit}")
                d_hand_cards.append(d_dealt)
                d_init_total = self._dealer._hand.total()
                input(f"Dealer's total: {d_init_total}")
            else:
                input("Dealer has drawn a card facing down.")
                input("Dealer's total: ???")
                d_hand_cards.append(d_dealt)
                return

    def run_player_turns(self):
        active_players = self._players.copy()
        blackjack_players = []
        for each_player in active_players.copy():
            blackjack = each_player._hand.is_blackjack()
            if blackjack == True:
                input(f"{each_player._name} achieved Blackjack!")
                blackjack_players.append(each_player)
                active_players.remove(each_player)
        while len(active_players) != 0:
            for each_player in active_players.copy():
                totalled = each_player._hand.total()
                print(f"{each_player._name}'s turn!")
                while True:
                    move = input(f"(Current score: {totalled}) 1 for hit, 2 for stand: ").strip() #idk why, but when I type 1, it won't accept it as 1 as an integer but it would accept 2. So I removed the int() entirely
                    if move == "1":
                        hitted = each_player.hit(self._deck)
                        totalled = each_player._hand.total()
                        input(f"{each_player._name} was given the {hitted._Rank} of {hitted._Suit}")
                        input(f"{each_player._name}'s total: {totalled}")
                        busted = each_player._hand.is_bust()
                        if busted == True:
                            active_players.remove(each_player)
                            input(f"{each_player._name}'s hand is a bust. They're out!")
                            break
                        elif totalled == 21:
                            active_players.remove(each_player)
                            input(f"{each_player._name}'s hand is a 21. Their turn is over!")
                            break
                    elif move == "2":
                        print(f"{each_player._name} chose to stand!")
                        active_players.remove(each_player)
                        break
                    else:
                        print("Only input 1 for hitting and 2 for standing")

    def run_dealer_turn(self): #sometimes, I get a NoneType object at input(f"Dealer dealt the {dealt._Rank} of {dealt._Suit}"). Solution: I transferred return after the loop at play_turn() and added a condition if it returns a none type.
        if len(self._dealer._hand._card) >= 2:
            reveal = self._dealer._hand._card[1]
            d_total = self._dealer._hand.total()
            print(f"Delear reveals his faced down card! It's the {reveal._Rank} of {reveal._Suit}.")
            print(f"Dealer's current score: {d_total}")
        blackjack = self._dealer._hand.is_blackjack()
        if blackjack == True:
            return
        self._dealer.play_turn(self._deck)
        d_total = self._dealer._hand.total()
        if d_total > 21:
            return

    def resolve_round(self):
        if self._dealer._hand.is_bust() == True:
            print("Dealer's hand was a bust! All active players won!")
            for each_player in self._players:
                if each_player._hand.is_bust() == False:
                    each_player._balance += each_player._bet
                    print(f"{each_player._name} won {each_player._bet}. New balance: {each_player._balance}.")
                    
                else:
                    each_player._balance -= each_player._bet
                    print(f"{each_player._name} lost {each_player._bet}. New balance: {each_player._balance}.")
        elif self._dealer._hand.is_blackjack() == True:
            print("Dealer's hand is a blackjack! All active players that have no blackjack lose!")
            for each_player in self._players:
                if each_player._hand.is_blackjack() == False:
                    each_player._balance -= each_player._bet
                    print(f"{each_player._name} lost {each_player._bet}. New balance: {each_player._balance}.")
                else:
                    print(f"{each_player._name}'s is also a blackjack. It's a push. New balance: {each_player._balance}.")
        else:
            for each_player in self._players:
                if each_player._hand.is_blackjack() == True:
                    each_player._balance += each_player._bet
                    print(f"Blackjack! {each_player._name} has won {each_player._bet}. New balance: {each_player._balance}.")
                elif each_player._hand.is_bust() == True:
                    each_player._balance -= each_player._bet
                    print(f"{each_player._name}'s hand was a bust! They lose {each_player._bet}. New balance: {each_player._balance}.")
                else:
                    if self._dealer._hand.total() == each_player._hand.total():
                        print(f"{each_player._name} tied with the dealer. New balance: {each_player._balance}.")
                    elif self._dealer._hand.total() > each_player._hand.total():
                        each_player._balance -= each_player._bet
                        print(f"{each_player._name}'s hand was less than the dealer! They lose {each_player._bet}. New balance: {each_player._balance}.")
                    else:
                        each_player._balance += each_player._bet
                        print(f"{each_player._name}'s hand was more than the dealer! They won {each_player._bet}. New balance: {each_player._balance}.")
        for each_player in self._players:
            for player_cards in each_player._hand._card:
                self._deck._cards.append(player_cards)
            each_player._hand._card.clear()
        for dealer_cards in self._dealer._hand._card:
            self._deck._cards.append(dealer_cards)
        self._dealer._hand._card.clear()


    def eliminate_broke_players(self):
        broke_players = [broke_player for broke_player in self._players if broke_player._balance <= 0]
        for broke_player in broke_players:
            if broke_player._balance < 0:
                print(f"{broke_player._name} is swimming with the sharks due to being in debt.")
            else:
                print(f"{broke_player._name} cannot play any further due to being broke.")
        self._players = [each_player for each_player in self._players if each_player._balance > 0]

    def ask_continue(self):
        active_player = self._players.copy()
        for each_player in active_player:
            go_on = input(f"Do you want to continue the game {each_player._name}? input y if continue, leave blank or any other letter otherwise: ")
            go_on = go_on.strip().upper() 
            if go_on == "Y" or go_on == "YES" or go_on == "YE":
                print(f"{each_player._name} has chosen to keep playing!")
            else:
                print(f"{each_player._name} has chosen to stop playing and has cashed out ${each_player._balance}!")
                self._players.remove(each_player)