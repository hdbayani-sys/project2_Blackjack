# ♣️♥️Blackjack Overview♦️♠️
Blackjack is my second software project to be submitted for EEE 111 under my instructor, Sr. Philip Tuason. This project contains an interactive and digital recreation of Blackjack, with the standard Blackjack game rules and procedures, accompanied with other features to bring some charm to the game. This was built using Visual Studio Code with Python ver 3.13 as the programming language.

## 🕹Features🃏
**Blackjack** includes the following game features:
- Multiple players competing against a dealer locally.
- Betting system where players are initially given a balance which they can use to place bets each round.
- Eliminates broke players (Or if somehow, be in debt.).
- Great replayability as the game can handle an almost infinite amount rounds.
- A dealer controlled by a computer that follows standard blackjack rules.
- User friendly outputs that allow the player to see each output at their own pace as well as seeing who's turn it is, their current score, and their new balance when resolving rounds.
- Randomized dialogue during betting and dealing.
- Option for players to continue playing or to cash out early. Game ends if all players are eliminated by having insufficient balance or voluntarily quitting

# 🛠Process⚒
### ♣️Setting Up the Pre-requisite Classes♣️
I started with setting up all the classes with their required attributes and methods. After that, I coded Card, Deck, Hand, Player, and Dealer, in that order. I only added the attributes and methods needed in each class, as stated by the instructions and the UML-like overview provided. I went into this project thinking that the instructor might try to manipulate the variables from the outside as someone who isn't knowledgeable of python encapsulation, so almost all attributes are protected. 

Now, in making the code for each class, the Card, Deck, and Hand classes were all instinctively easy to write their code, which they were. Card was very straightforward, Deck just utilized for loops and random functions, and for Hand, specifically for Ace handling, I just let it default to 11 and drop it to 1 if the current total is over 21, much like what I saw when I was playing GTA: San Andreas' Blackjack when I was looking for motivation and inspiration during breaks. 

The next classes I worked on were the player and dealer. When working on player, I had the idea of randomizing dialogue so that there's charm to my project. Since I am more or less aware of the test cases for betting, I have already set-up fail safes, makign sure it wouldn't result to an error early on. For dealer, it was fairly simple since it doesn't rely much on user input, rather only on conditions.

### ♠️Setting Up the Main Controller Class♠️
  The main controller class was not exactly a struggle, but very VERY tedious to do. Sure, it only consists of no less than 200 lines of code, but the syntax of OOP was very much different to what I'm used to and remembering them was the hardest part. To not overwhelm myself and to avoid burnouts, I did the methods() in order to make sure I wouldn't go back in forth, with the exception of doing resolve_rounds() last because it had the most test cases out of all methods() to consider. __init__() was straightforward, much like all __init__()'s from previous classes. For start(), I settled with assigning it as the one who controls the game flow and decides when to stop. Most other methods() I made using iteration, while others have numerous if condition statements for covering test cases.
  
### ♥️Setting up the Entry Point♥️
  Because I made start() the game flow organizer, Entry point was fairly simple and was only robust because of implementing the optional rules if people wanted to. I got the format from researching how to access start() from Class Blackjackgame(), which reminded me of that one item in the 2nd Long Exam. 

### ♦️Problems Encountered Along the Way and Debugging Process♦️
  Since I haven't fully mastered OOP, I struggled more in making the code than debugging it because I oftentimes forget the syntax and had to search every like 5 or 6 lines of code. After some time, I had some moments where I where able to code some methods in Game.py 10-20 lines of code in without searching up the syntax. This also means that when I started initially, I struggled with getting into the mindset that OOP is very different from usual Python programming since I oftentimes find myself letting the other classes interact with each other instead of making them independent and letting Game.py do the work. It feels wrong since it feels like the code is not yet complete, the back of my mind always tells me "Hey how would they interact?", "You sure it's done? It doesn't seem to be". Eventually I got over it, and was able to continue normally.

  As I have said before, I had a much easier time in debugging because like I said previously, I'm aware of almost every test case scenario in blackjack, so I was able to setup failsafes early on. But that didn't mean I did minimal debugging. One of my first bugs was that the player was betting it's entire balance since I coded the amount it bets to be equal to its balance and not the number it inputted as its bet. Took me about 5 minutes to notice that. Other errors I encountered where syntax errors at class Hand() because I wrote Rank and Card as _Rank and _Card respectivelyand getting NoneType when I print the dialogue ("Dealer dealt the {dealt._Rank} of {dealt._Suit}"), which I fixed by transferring the return after the loop at play_turn() and added a condition if it returns a none type, which also solved the dealer sometimes dealing only once even if it's current total is still less than 17. The weirdest error I got was when I type 1 to hit, move variable doesn't register it as 1 when I turn it into the variable no matter what I do. I don't know why but I just removed the int() ultimately since to be fair, I'm just seeing if the user entered "1" or "2",  not the numerical value 1 and 2 have.

# 👀Visual Representation of the Program👀
This part will provide the details and visual representation of how the Program works so that everyone may be able to understand both the "main show" and the "behind the scenes" of the software project.

## 🗃The Classes🗃

### 1. Card
  - The Card class represents a single card with the following attributes:
    1. Suit - Spade, Club, Heart, or Diamond, 
    2. Rank - Ranging to an Ace, number cards 2-10, Jacks, Queens, and Kings,
    3. Value - Numerical values from 1-11
    
### 2. Deck
  - The Deck class represents the standard 52-deck of card objects that have the attributes from the Card class. It has the following attributes:
    1. cards - An empty list which is later filled by all possible playing cards with their values using a loop.
  
  - Furthermore, it has the following methods:
    1. shuffle() - Shuffles the Cards list through a "random" function random.shuffle().
    2. deal() - Removes the first-most card on the Cards list.

### 3. Hand
  - The Hand class represents the cards being held by a Player and a Dealer and the total points the cards are valued. It has the following attributes:
    1. card - An empty list that stores the cards that either a player or the dealer has

  - Furhtermore, it has the following methods:
    1. total() - Stores the current total of the card list and handles the Ace point if it's either 11 points or 1. It sends back the current summation.
    2. is_blackjack() - Checks if the current summation from total() is 21 AND the number of cards in the card list is 2. If so, it will send back True, otherwise, it will send back False.
    3.  is_bust() - Similar in structure to is_blackjack(), it checks if the current summation from total() is 22 and above. If so, sends back True, otherwise, False.

### 4. Player
  - The Player class represents a human player. It has the following attributes:
    1. name - Player_x, where x is a number ranging from 1-7.
    2. balance - All players start with 10000 which increase or decrease depending on the bet made and whether they wonor lost the round.
    3. bet - The amount from the balance that the players will "pay" to play a round of Blackjack.
    4. hand - Provides the player access to their own Hand class.

  - Furthermore, it has the following methods:
    1. place_bet() - Allows the player to place a bet and is stored in attribute bet. The input must be a number AND is less than or equal to the balance while being greater than zero.
    2. hit(deck) - Gives a player a card from the deck and adds it to their hand.
    3. stand() - Ends a players turn by giving the BlackjackGame the signal to end their turn.

### 5. Dealer
  - The Dealer class represents a dealer controlled by the computer. It has the following attributes:
    1. hand - Provides the dealer access to their own Hand class.

  - Furthermore, it has the following methods:
    1. play_turn() - Allows the dealer to draw a card if their current hand doesn't sum up to 17 or more and stops until the hand does sum up to 17 or more.
    
### 6. BlackjackGame
  - The Blackjackgame class is what's called the "main controller" since it is the that allows the subsequent classes to interact with one another to make a cohesive flow of a blackjack game. It has the following attrributes:
    1. players = It's an empty list that will be filled by the players created by setup_players().
    2. dealer - "Creates" the dealer by calling the Dealer class.
    3. deck - Accesses the Deck class to create the card deck and give each card a Value.
    4. round_number - A number representing how many rounds of blackjack have currently played.
  
  - Furthermore, it has the following methods:
    1. start() - Contains all the subsequent methods and a shuffle method and organizes them to create the flow of a blackjack game
    2. setup_players() - Asks how many players will join and creates that many players each having their own access to the Player class.
    3. place_bets() - For each player currently playing, ask them how much they will bet.
    4. initial_deal() - Gives each player 2 cards from the deck face up while giving the dealer a card facing upwards and a card facing downwards
    5. run_player_turns() - Checks if any of the players have a blackjack hand and removes them from the list of active players. For each player actively playing, ask them to hit or stand. Remove the player from the list of active players if they either get 21 points, bust, or stand.
    6. run_dealer_turn() - Reveals the faced down card and would either draw until they have 17 points or more, or stand if they already do.
    7. resolve_round() - Ends the round by giving or taking the amount each player betted in their balance, depending on the outcome of the game.
    8. eliminate_broke_players() - Players with 0 or if possible, negative balance, will be removed from the list of players eligible to play.
    9. ask_continue() - For the remaining players, asks if they want to continue playing or quit early and "cash out". If they want to continue, they continue playing, else they are removed from the list of players eligible to play.

## 🌊The Flow🎞
The following images below provide the flowchart of the blackjack game the program follows:

![image alt](https://github.com/hdbayani-sys/project2_Blackjack/blob/31327c7cb0e1ff663d927ad97423a4f7179b96b7/Flowchart_Assets/1.png)
![image alt](https://github.com/hdbayani-sys/project2_Blackjack/blob/31327c7cb0e1ff663d927ad97423a4f7179b96b7/Flowchart_Assets/2.png)
![image alt](https://github.com/hdbayani-sys/project2_Blackjack/blob/31327c7cb0e1ff663d927ad97423a4f7179b96b7/Flowchart_Assets/3.png)
![image alt](https://github.com/hdbayani-sys/project2_Blackjack/blob/31327c7cb0e1ff663d927ad97423a4f7179b96b7/Flowchart_Assets/4.png)
![image alt](https://github.com/hdbayani-sys/project2_Blackjack/blob/31327c7cb0e1ff663d927ad97423a4f7179b96b7/Flowchart_Assets/5.png)
![image alt](https://github.com/hdbayani-sys/project2_Blackjack/blob/31327c7cb0e1ff663d927ad97423a4f7179b96b7/Flowchart_Assets/6.png)
![image alt](https://github.com/hdbayani-sys/project2_Blackjack/blob/31327c7cb0e1ff663d927ad97423a4f7179b96b7/Flowchart_Assets/7.png)

# ⚙️Setting up the program🐍
## Prerequisite
- Make sure to have a laptop/desktop that has Visual Studio Code with Python version 3.13 for the best experience.

## Setup
1. Download all the files in the repository apart from the README.md and the Flow_Chart Assets folder
2. Place the files on a single folder and make sure all are at the same directory.
3. Open Visual Code and locate File on the top left.
4. File -> Open File -> Find and select Main.py
5. Run Python File by pressing the playbutton on the top right.
6. You're now ready to not-so gamble!

