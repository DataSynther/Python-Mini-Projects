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
    try:
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
    except Exception as e:
        print ("The following ERROR occured while collecting player's bet ", e)       


# Function to create a deck of cards
def get_deck():
    try:
        """Create a deck of cards with 52 unique cards."""
        deck = []
        for suit in (HEARTS, DIAMONDS, CLUBS, SPADES):
            for value in range(2, 11):
                deck.append((str(value), suit))  # Add numbered cards
            for face_card in ('J', 'Q', 'K', 'A'):
                deck.append((face_card, suit))  # Add face cards
        random.shuffle(deck)  # Shuffle the deck
        return deck
    except Exception as e:
        print ('An Exception occured during DECK Creation ',e)


# Function to calculate the value of a hand
def display_hands(player_hand, dealer_hand, show_dealer_hand = False):
    try:
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
    except Exception as e:
        print ('An ERROR occured while displaying player hands, ', e)


#Caluclate Player Hand Values
def get_hand_value(cards):
    try:
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

    except Exception as e:
        print ('An ERROR occured while calculating Hand Value. ',e)


# Design the cards display
def display_cards(cards):
    try:
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
    except Exception as e:
        print ('The following Error occured while displaying the cards ',e)


#Function to ask for the player's move
def get_move(player_hand, money):
    try:
        ''' Asks the player for their move and returns 'H' for hit, 'S' for stand
        and 'D' for double down. '''
        #Keep looping until the player enters a correct move 
        # Determine what moves the the player can make:
        while True:
            moves = ['(H)it', '(S)tand']

            #Since there is only two cards in this game, a player can double down in the first move itself
            if len(player_hand) == 2 and money > 0: 
                moves.append ('(D)ouble Down')

            #Get the player's move :
            move_promt = ', '.join(moves)+ '> '
            move = input(move_promt).upper()

            if move in ('H','S'):
                return move # The player has entered a valide move.
            elif move == 'D' and '(D)ouble Down' in moves: # The player is satisfying conditions for double douwn
                return move
    except Exception as e:
        print ('The Following error occured while calculating player move ', e)




### Designing the MAIN GAME 

def main():
    try:
        print ('''  HELLO !!! WELCOME TO BACKJACK GAME !!!!   
            
            RULES:
            
                    Try to get as close to 21 without going over.
                    Kings, Queens and Jacks are worth 10 points.
                    Aces are worth 1 and 11 points
                    Cards 2 through 10 are worth their face value.
                    
                    (H)it to take another card.
                    (S)tand to stop taking cards.
                    On your first play, you can (D)ouble down to increase your bet 
                    but must hit exactly one more time before standing.
                    In case of a tie, the bet is returned to the player.
                    The dealer stops hitting at 17.''')
        
        #Defining the initial money value
        money = 5000

        #Main Game Loop
        while True: 
            #Check if the player has run out of money or not 
            if money <= 0:
                print ("""You're broke!
                    Good Thing you weren't playing with real money !
                    Thanks for playing! """)
                sys.exit()
            
            #Let the player enter their bet for this round

            print ( 'Current Balance  :' , money )
            bet = get_bet(money)

            #Give the dealer and the player two cards from the deck each:
            deck = get_deck()
            dealer_hand = [deck.pop(),deck.pop()] # Note: pop takes the last item from the iterative
            player_hand = [deck.pop(),deck.pop()]

            ## Handle player actions
            print ('Bet :', bet)

            # keep looping for player actions until player stands or busts
            while True:
                display_hands (player_hand, dealer_hand)
                print()

                #check if the player has bust:
                if get_hand_value(player_hand)>21:
                    break

                #Get the player's move, either H,S or D
                move = get_move(player_hand, money - bet)

                #Dealing the player move based on the chosen move

                #Calculate New Bet in case the player is doubling down
                if move == 'D':
                    # Player is doubling down, they can increase their bet:
                    additional_bet = get_bet(min(bet, (money - bet)))
                    bet += additional_bet
                    print("Bet is increased to {}".format(bet))
                    print ("Bet :", bet)

                # Drawing new card if doubling down (which is similar as asking for Hit)
                if move in ('H','D'):
                    #Hit / doubling down takes another card 
                    new_card = deck.pop()
                    rank,suit = new_card
                    print ('You drew a {} of {}.'.format (rank, suit))
                    player_hand.append(new_card)

                    # check if the player is busted after the draw
                    if get_hand_value(player_hand)>21:
                        continue
                
                # After one draw after doubling down the game must end for that round
                # Which is similer to the stand action
                if move in ('S','D'):
                    break
            

            #Handle the delar's actions:
            if get_hand_value(player_hand) <= 21:
                while get_hand_value(dealer_hand) < 17:
                    # The dealer hits
                    print ('Delaer Hits ............................')
                    dealer_hand.append(deck.pop())
                    display_hands (player_hand, dealer_hand)


                    # check if the dealer is busted or not
                    if get_hand_value(dealer_hand)>21:
                        break

                    input ('Press Enter to Continue.................')
                    print ('\n\n')

            # Show the final Hands
            display_hands(player_hand, dealer_hand, show_dealer_hand= True)

            #Calculating final value of each of the players
            player_value = get_hand_value(player_hand)
            dealer_value = get_hand_value(dealer_hand)

            #Handle whether the player won, lost or tied:

            if dealer_value > 21 :
                print ('Dealer busts! You win ${}'.format (bet))
                money += bet
            elif (player_value >21) or (player_value < dealer_value):
                print ('You Lost!')
                money -= bet
            elif player_value>dealer_value:
                print ("You Won ${}",format(bet))
                money += bet
            elif player_value == dealer_value :
                print ("It's a tie, the bet is returned to you. ")
            
            input ('Press Enter to Continue .........')
            print ('\n\n')

    except Exception as e:
        print ('An ERROR Occured due to ', e)


# If h=the program is run (instead of imported), run the game

if __name__ == '__main__' :
    main()

