import random

suits = ('hearts','diamonds','spades','clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.cards = []

        for suit in suits:
            for rank in ranks:
                new_card = Card(suit,rank)
                self.cards.append(new_card)

    def __str__(self):
        for card in self.cards:
            print(card)
        
        return f'{len(self.cards)}  cards in deck' 
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_one(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'ace':
            self.aces += 1

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you only have {chips.total} chips to wager')
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_aces()

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("Hit or Stand? Enter 'h' or 's': ")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('Player stands')
            playing = False
        else:
            print("Sorry, I didn't understand that. Please enter 'h' or 's'")
            continue
        break

def show_some(player,dealer):
    # show only one of the dealer's cards
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])
    
    # show all of player's cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    
def show_all(player,dealer):
    # show all of dealer's cards
    print("\n Dealer's Hand: ")
    for card in dealer.cards:
        print(card)
    # display hand value
    print(f"Value of dealer's hand is {dealer.value}")
    
    # show all of player's cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    #display hand value
    print(f"Value of player's hand is {player.value}")

def player_busts(player,dealer,chips):
    print("Player bust!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer bust. Player wins!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and player tie! PUSH")

playing = True
former_chips = 0

if __name__ == '__main__':
    while True:
        # Print an opening statement
        print("Welcome to Blackjack!")
        
        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()
        
        player_hand = Hand()
        player_hand.add_card(deck.deal_one())
        player_hand.add_card(deck.deal_one())
        
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal_one())
        dealer_hand.add_card(deck.deal_one())
            
        # Set up the Player's chips
        if former_chips > 0:
            player_chips = Chips(former_chips)
        else:
            player_chips = Chips()
        
        # Prompt the Player for their bet
        take_bet(player_chips)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        while playing:
            
            # Prompt for Player to Hit or Stand
            hit_or_stand(deck,player_hand)
            
            # Show cards (but keep one dealer card hidden)
            show_some(player_hand,dealer_hand)
            
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand,dealer_hand,player_chips)

                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)
        
            # Show all cards
            show_all(player_hand,dealer_hand)
            
            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)
        
        # Inform Player of their chips total 
        print(f'\n Player total chips are: {player_chips.total}')
        
        # Ask to play again
        new_game = input("Do you want to play another hand? y/n")
        
        if new_game[0].lower() == 'y':
            playing = True
            print(f'Chips to carry over: {player_chips.total}')
            former_chips = player_chips.total
            continue
        else:
            print("Thanks for playing!")
            break