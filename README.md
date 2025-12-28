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
  The Card class represents a single card with the following attributes:  
    1. Suit - Spade, Club, Heart, or Diamond, 
    2. Rank - Ranging to an Ace, number cards 2-10, Jacks, Queens, and Kings, 
    3. Value - Numerical values from 1-11
    
### 2. Deck
  The Deck class represents the standard 52-deck of card objects that have the attributes from the Card class. It has the following attributes:
    1. cards - An empty list which is later filled by all possible playing cards using a loop.
  
  Furthermore, it has the following methods:
    1. shuffle() - Shuffles the Cards list through a "random" function random.shuffle().
    2. deal() - Removes the first-most card on the Cards list.

### 3. Hand
  The Hand class represent the cards being held by a Player and a Dealer and the total points the cards are valued.

### 4. Player

### 5. Dealer

### 6. BlackjackGame

## 🌊The Flow🎞
aaaaaaaa
