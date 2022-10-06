import random
from tkinter import *
from PyQt5.QtGui import QPixmap

deck_object = None
class Deck(object):
    
    def __init__(self):
        # All 52-Playing Cards
        self.all_cards = [ 
            # List of Clubs
            ['Graphics/2_of_clubs.png',
            'Graphics/3_of_clubs.png',
            'Graphics/4_of_clubs.png',
            'Graphics/5_of_clubs.png',
            'Graphics/6_of_clubs.png',
            'Graphics/7_of_clubs.png',
            'Graphics/8_of_clubs.png',
            'Graphics/9_of_clubs.png',
            'Graphics/10_of_clubs.png',
            'Graphics/jack_of_clubs.png',
            'Graphics/queen_of_clubs.png',
            'Graphics/king_of_clubs.png',
            'Graphics/ace_of_clubs.png'],

            # List of Diamonds 
            ['Graphics/2_of_diamonds.png',
            'Graphics/3_of_diamonds.png',
            'Graphics/4_of_diamonds.png',
            'Graphics/5_of_diamonds.png',
            'Graphics/6_of_diamonds.png',
            'Graphics/7_of_diamonds.png',
            'Graphics/8_of_diamonds.png',
            'Graphics/9_of_diamonds.png',
            'Graphics/10_of_diamonds.png',
            'Graphics/jack_of_diamonds.png',
            'Graphics/queen_of_diamonds.png',
            'Graphics/king_of_diamonds.png',
            'Graphics/ace_of_diamonds.png'],

            # List of Hearts 
            ['Graphics/2_of_hearts.png',
            'Graphics/3_of_hearts.png',
            'Graphics/4_of_hearts.png',
            'Graphics/5_of_hearts.png',
            'Graphics/6_of_hearts.png',
            'Graphics/7_of_hearts.png',
            'Graphics/8_of_hearts.png',
            'Graphics/9_of_hearts.png',
            'Graphics/10_of_hearts.png',
            'Graphics/jack_of_hearts.png',
            'Graphics/queen_of_hearts.png',
            'Graphics/king_of_hearts.png',
            'Graphics/ace_of_hearts.png'],

            # # List of Spades 
            ['Graphics/2_of_spades.png',
            'Graphics/3_of_spades.png',
            'Graphics/4_of_spades.png',
            'Graphics/5_of_spades.png',
            'Graphics/6_of_spades.png',
            'Graphics/7_of_spades.png',
            'Graphics/8_of_spades.png',
            'Graphics/9_of_spades.png',
            'Graphics/10_of_spades.png',
            'Graphics/jack_of_spades.png',
            'Graphics/queen_of_spades.png',
            'Graphics/king_of_spades.png',
            'Graphics/ace_of_spades.png']

        ]
        
        # A list to store resized images. This stores the cards that 
        # are already pulled from the deck and stores them in memory so
        # they can be drawn.
        self.card_images = []
        # A copy of the images list that will be used to remove cards
        # already pulled from the deck.
        self.taken_cards = []
        # A list to keep track of the exposed cards
        self.exposed_cards = []

        self.temp_card_images = []
    
    def get_deck():
        global deck_object
    
        if deck_object is None:
            deck_object = Deck()

        return deck_object

    def select_card(self, exposed):
        # keep pulling cards until a unique card is selected
        while (True):
            # Get random suit, then random card from that suit
            suit_selected = random.choice(self.all_cards)
            card_selected = random.choice(suit_selected)
            # Remove card from deck
            if (card_selected not in self.taken_cards):
                self.taken_cards.append(card_selected)
                break

        # Add card to exposed_cards list
        if(exposed):
            self.exposed_cards.append(card_selected)

        return card_selected

    def draw_flop(self):
        # Selet cards from deck
        card1 = QPixmap(self.select_card(True))
        card2 = QPixmap(self.select_card(True))
        card3 = QPixmap(self.select_card(True))
        
        return [card1, card2, card3]
        

    def draw_one(self):
        card = QPixmap(self.select_card(True))
        
        return card

    