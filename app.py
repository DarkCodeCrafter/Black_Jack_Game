import random

# Boolean type to know whether play is in hand
playing = False

# Amount for buy-in
chip_pool = 100  # Initial chips

bet = 1

restart_phrase = "Press d to deal the cards again, or press q to quit."

# Card Suits and Ranks
suits = ('H', 'D', 'S', 'C')
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

# Card values
card_val = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def grab_suit(self):
        return self.suit

    def grab_rank(self):
        return self.rank

    def draw(self):
        print(self.suit + self.rank)

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False  # Track if hand has an Ace

    def __str__(self):
        hand_comp = " ".join([str(card) for card in self.cards])
        return f'The hand has {hand_comp}'

    def card_add(self, card):
        self.cards.append(card)
        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]

    def calc_val(self):
        if self.ace and self.value < 12:
            return self.value + 10
        else:
            return self.value

    def draw(self, hidden):
        starting_card = 1 if hidden and playing else 0
        for card in self.cards[starting_card:]:
            card.draw()

class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranking]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self):
        return "The deck has " + " ".join(str(card) for card in self.deck)

def make_bet():
    global bet
    print('What amount of chips would you like to bet? (Enter a whole number)')
    
    while True:
        try:
            bet_comp = int(input())
            if 1 <= bet_comp <= chip_pool:
                bet = bet_comp
                break
            else:
                print(f"Invalid bet, you only have {chip_pool} remaining.")
        except ValueError:
            print("Please enter a valid number.")

def deal_cards():
    global playing, deck, player_hand, dealer_hand, chip_pool, bet, result

    deck = Deck()
    deck.shuffle()

    make_bet()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    dealer_hand.card_add(deck.deal())

    result = "Hit or Stand? Press h for hit or s for stand: "

    if playing:
        print("Fold, Sorry")
        chip_pool -= bet

    playing = True
    game_step()

def hit():
    global playing, chip_pool, deck, player_hand, result

    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())
        
        print(f"Player hand is {player_hand}")

        if player_hand.calc_val() > 21:
            result = f'Busted! {restart_phrase}'
            chip_pool -= bet
            playing = False
    else:
        result = f"Sorry, can't hit {restart_phrase}"

    game_step()

def stand():
    global playing, chip_pool, deck, player_hand, dealer_hand, result

    if not playing:
        if player_hand.calc_val() > 0:
            result = "Sorry, you can't stand!"
        return

    while dealer_hand.calc_val() < 17:
        dealer_hand.card_add(deck.deal())

    if dealer_hand.calc_val() > 21:
        result = f'Dealer busts! You win! {restart_phrase}'
        chip_pool += bet
    elif dealer_hand.calc_val() < player_hand.calc_val():
        result = f'You beat the dealer, you win! {restart_phrase}'
        chip_pool += bet
    elif dealer_hand.calc_val() == player_hand.calc_val():
        result = f'Tied up, push! {restart_phrase}'
    else:
        result = f'Dealer Wins! {restart_phrase}'
        chip_pool -= bet

    playing = False
    game_step()

def game_step():
    print("\nPlayer Hand is:", end=" ")
    player_hand.draw(hidden=False)
    print(f'\nPlayer hand total is: {player_hand.calc_val()}')

    print("\nDealer Hand is:", end=" ")
    dealer_hand.draw(hidden=True)

    if not playing:
        print(f" --- for a total of {dealer_hand.calc_val()}")
        print(f"Chip Total: {chip_pool}")
    else:
        print(" with another card hidden upside down")

    print(f'\n{result}')
    player_input()

def game_exit():
    print("Thanks for playing!")
    exit()

def player_input():
    plin = input().lower()

    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        game_exit()
    else:
        print("Invalid Input. Enter h, s, d, or q: ")
        player_input()

def intro():
    statement = '''Welcome to BlackJack! Get as close to 21 as you can without getting over! 
Dealer hits until reaching 17. Aces count as 1 or 11. Cards are displayed in suit+rank format.'''

    print(statement)
    print('')

# Start the game
intro()
deal_cards()
