from Card import * 
import random
suits =('Hearts', 'Diamonds', 'Spades', 'clubs')
ranks =('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen','King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10,'King':10, 'Ace':11}
playing =True
class Deck():
    """description of class"""
    def __init__(self):
        self.deck=[]
        #.suits=suits
        #self.ranks=ranks
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp +='\n'+ card.__str__()
        return "The deck has: "+deck_comp 
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card= self.deck.pop()
        return single_card



