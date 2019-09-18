from Deck import * 
from Hand import *
from Chips import *
import random
#suits =('Hearts', 'Diamonds', 'Spades', 'clubs')
#ranks =('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen','King', 'Ace')
#values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10,'King':10, 'Ace':11}
playing =True

def take_bet(chips):
     while True:
         try:
            chips.bet = int(input("How many chips would you like to bet?"))
         except: 
            print("Sorry Please provide an integer")
         else:
            if chips.bet > chips.total:
                print(f"Sorry, you do not have enough chips! You have : {chips.total} CHIPS")

            else :
                break

def hit(deck, hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x=input('Hit or Stand? Enter h or s: ')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print('Player stands Dealer''s Turn')
            playing = False

        else:
            Print('Sorry, I did not understand that, Please enter h or s only: ')
            continue
        break

def show_some(player, dealer):
    print('Dealer''s Hand :')
    print('One card hidden! ')
    print(dealer.cards[0])
    print('\n')
    print('Players Hand: ')
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print('Dealers hand:')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('Players hand: ')
    for card in player.cards:
        print(card)

def player_bursts(player, dealer, chips):
    print('Bust Player')
    chips.lose_bet()
def player_wins(player, dealer, chips):
    print('Player Wins!')
    chips.win_bet()

def dealer_bursts(player, dealer, chips):
    print('Player wins! Dealer Bursted!')
    chips.win_bet()
def dealer_wins(player, dealer, chips):
    print('Dealer wins')
    chips.lose_bet()
def push(player, dealer):
    print('Dealer and player tied! Push!')



while True:
    print('Welcome to BlackJack!')

    deck =Deck()
    deck.shuffle()
     
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand= Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()


    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_bursts(player_hand,dealer_hand, player_chips)

            break
        if player_hand.value <= 21:

            while dealer_hand.value < player_hand.value:
                hit(deck, dealer_hand)

            show_all(player_hand, dealer_hand)


            if dealer_hand.value > 21:
                dealer_bursts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)


        print('\nPlayer total chips are at:{}'.format(player_chips.total))
    new_game= input("Would you like to player another hand? Y/N")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else: 
        print("Thank you for playing!")

        break






