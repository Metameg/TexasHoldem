from PyQt5.QtGui import QPixmap
from deck import Deck
from HandChecker import HandChecker
#from PIL import Image, ImageTk

class Player(object):
    def __init__(self, faceup, seat_no, amount = 1000):
        self.deck = Deck.get_deck()
        self.seat = seat_no
        # Select cards from deck
        self.card1 = self.deck.select_card(faceup)
        self.card2 = self.deck.select_card(faceup)
        self.faceup = faceup
        self.auto_muck = True
        self.player_turn = False
        self.stack_size = amount
    
    # def __del__(self):
        #pass

    def create_hand_images(self, card1, card2):
   
        if (self.faceup):
            card1_image = QPixmap(card1)
            card2_image = QPixmap(card2)
        else:
            card1_image = QPixmap("Graphics/card_back.png")
            card2_image = QPixmap("Graphics/card_back.png")

        return [card1_image, card2_image]

    def determine_hand_rank(self):
        hand_checker = HandChecker(self.deck.all_cards, self.deck.exposed_cards)
        score = hand_checker.identify_hand()
        del hand_checker

        return score