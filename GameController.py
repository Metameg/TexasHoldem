#auto-py-to-exe || pyInstaller
import sys, time, re
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
from GUIController import UI
from deck import Deck
from LinkedList import *
from Player import Player
from HandChecker import RANK_NAMES

class GameController():
    def __init__(self):
        self.GUI = UI.get_GUI()
        self.deck = Deck.get_deck()
        self.player_hand_images = []
        
        # Create Linked List of Players
        self.players = SLinkedList()
        self.players.head = Node(Player(True, 1)) # Hero
        # Generate Hero pixmap
        # self.player_hand_images.append(self.players.head.dataval.create_hand_images())

        # Villains
        for i in range(1, self.GUI.numPlayers):
            new_player = Player(True, i+1)
            self.players.add_node(new_player)
            # Generate Villain pixmap
            # self.player_hand_images.append(new_player.create_hand_images())
        self.first_cards = []
        self.first_card_pixmaps = []
        
    def select_opening_cards(self):

        for player in self.players.iterate_from(self.players.head):
            card = self.deck.select_card(True)
            self.first_cards.append(card)
            self.first_card_pixmaps.append(player.dataval.create_hand_images(card))
        
    def find_high(self):
        keys = list(RANK_NAMES.keys())
        vals = list(RANK_NAMES.values()) 
        seat_index = -1
        high = -1
        high_seat_index = 0

        for card in self.first_cards:
            seat_index += 1
            split_string = re.split(r'/|_', card)
            index = vals.index(split_string[1])
            card_key = keys[index]
            print (keys[index], seat_index)

            if card_key == 12:
                return seat_index        
            elif card_key > high:
                high = card_key
                high_seat_index = seat_index
        
        return high_seat_index

    def assign_player_pixmaps(self):
        
        card_index = 0
        for hand in self.first_card_pixmaps:
            # _card1 = card_no - 1
            # self.timer.stop()
            # self.timer.start(1000)
            if card_index < self.GUI.numPlayers * 2:
                card_label = self.GUI.player_card_labels[card_index]
                card_label.setPixmap(hand[0])
                card_index += 2
                # self.timer.start()
                # self.timer.timeout.connect(lambda: self.show_card(card_label))
                self.show_card(card_label)
                # card_label.show()
        
    
    def show_card(self, label):
        label.show()
        QApplication.processEvents()
        time.sleep(0.8)
        # self.timer.singleShot(1000, lambda: self.assign_player_pixmaps)
        # self.timer.stop()
        # self.timer.start(1000)

    def post_blinds(self):
        SB_index = self.GUI.D_index + 1
        pass

    def bet_round(self):
        if self.betting_round == 'preflop':
            bet_start = self.GUI.SB_pos + 2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GC = GameController()
    GC.select_opening_cards()
    GC.assign_player_pixmaps()
    
    D_seat = GC.find_high()
    GC.GUI.D_index = D_seat
    # Show the dealer button pixmap at the correct seat pos
    GC.GUI.D_buttons[GC.GUI.D_index].show()
    # Shuffle deck
    GC.deck.shuffle()
    




    # QTimer.singleShot(10, GC.assign_player_pixmaps)
    # cards = GC.select_opening_cards()
    # UIWindow = UI()
    app.exec_()
    
    # for i in range(len(cards)):
    #     print(cards[i])