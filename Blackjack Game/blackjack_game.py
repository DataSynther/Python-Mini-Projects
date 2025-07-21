"""Blackjack, inspired by Al Sweigart and adapted for Python 3.
This is a simple implementation of the Blackjack game.
The classic card game also known as 21. (This version doesn't have
splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack
"""

#Importing necessary libraries
import random,sys

# Constants for card values
'''https://inventwithpython.com/charactermap'''
HEARTS = chr(9829)
DIAMONDS = chr(9830)
CLUBS = chr(9827)
SPADES = chr(9824)
BACKSIDE = 'backside'

# Get Bet amount / value 

def get_bet(max_bet):
    ''' Ask the player how much they want to bet for this round, 
    Keep asking until they enter a valid amount. 
    Finally return the bet amount.'''
    while True:
        print ("How much do you want to bet?(1-{}, or QUIT)".format(max_bet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for Playing!!'
                  'See you next time!')
            sys.exit()

        #If the input is not number, we should ask again     

        if not bet.isdecimal():
            print('Please enter a valid bet amount.')
            continue  

        bet = int(bet)
        if bet < 1 or bet > max_bet:
            print('Please enter a valid bet amount between 1 and {}.'.format(max_bet))
            continue
        else:
            return bet
        
# Function to create a deck of cards
def get_deck():
    """Create a deck of cards with 52 unique cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, CLUBS, SPADES):
        for value in range(2, 11):
            deck.append((str(value), suit))  # Add numbered cards
        for face_card in ('J', 'Q', 'K', 'A'):
            deck.append((face_card, suit))  # Add face cards
    random.shuffle(deck)  # Shuffle the deck
    return deck

# Function to calculate the value of a hand
def display_hands(player_hand, dealer_hand, show_dealer_hand = False):
    ''' Show the player's and dealer's cards. Hid the dealer's first 
     card if show_dealer_hand is False.'''
    print ()

    if show_dealer_hand == True:
        print ('Dealer\'s hand: ', get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print ('Dealer\'s hand: ', get_hand_value(dealer_hand[1:]))
        display_cards([BACKSIDE] + dealer_hand[1:])
    
    print ('Your hand: ', get_hand_value(player_hand))
    display_cards(player_hand)


def get_hand_value(cards):
    ''' Returns the value of the cards, Face cards are worth 10,
    aces can be worth 1 or 11, depending on the total value of the hand. 
    This function picks the most suitable ace value.'''

    value =0
    number_of_aces = 0

    #Add the value for non ace cards:
    for card in cards:
        if card[0] in ('J', 'Q', 'K'):
            value += 10
        elif card[0] == 'A':
            number_of_aces += 1
        else:
            value += int(card[0])  # Convert string to int for numbered cards

    # Add the value for aces:
    value += number_of_aces  # Count each ace as 1 initially
    for _ in range(number_of_aces):
        # If adding 10 doesn't exceed 21, count ace as 11
        if value + 10 <= 21:
            value += 10
    
    return value


# Design the cards display
def display_cards(cards):
    '''Display the cards in a readable format.'''
    rows = ['', '', '', ''] # The text to display on each row

    for i, card in enumerate(cards):
        rows[0] += ' ___  ' # Top row of the card
        if card == BACKSIDE:
            rows[1] += '|###| ' # Backside of the card
            rows[2] += '|###| ' # Backside of the card  
            rows[3] += '|###| '
        else:
            #print card's front
            rank,suit = card # The card is a tuple (rank, suit)
            rows[1] += '|{} | '.format(rank.ljust(2)) # First row of the card
            rows[2] += '| {} | '.format(suit) # Second row of the card
            rows[3] += '|_{}| '.format(rank.rjust(2, '_')) # Third row of the card

    # Print the rows of the cards
    for row in rows:   
        print(row)

#Function to ask for the player's move
def get_move(player_hand, money):
    ''' Asks the player for their move and returns 'H' for hit, 'S' for stand
    and 'D' for double down. '''
    #Keep looping until the player enters a correct move 
    # Determine 
