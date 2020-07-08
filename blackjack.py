﻿
import random 

suits =('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True
# card class
class Card():

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return self.rank + " of " + self.suit

#deck class
class Deck():

  def __init__(self):
    self.deck = []
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit, rank))

  def __str__(self):
    deck_comp = ''
    for card in self.deck:
      deck_comp += '\n' + card.__str__()
    return "The deck has:  "+ deck_comp

  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self):
    single_card = self.deck.pop()
    return single_card

class Hand():
  def __init__(self):
    self.cards = []         # start with an empty lists as we did in the Deck class
    self.value = 0         # start with zero value
    self.aces = 0          # add an attribute to keep track of aces

  def add_card(self, card):
    # card passed in
    # from Deck.deal() --> single Card(suit, rank)
    self.cards.append(card)
    self.value += values[card.rank]

    #track of aces
    if card.rank == 'Ace':
      self.aces += 1

  def adjust_for_ace(self):

    # IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
    # THEN CHANGE MY ACE TO BE A 1 INSTEAD OF AN 11
    while self.value > 21 and self.aces:
      self.value -= 10
      self.aces -= 1

class Chips():
  def __init__(self, total = 100):
    self.total = total
    self.bet = 0

  def win_bet(self):
    self.total += self.bet

  def lose_bet(self):
    self.total -= self.bet