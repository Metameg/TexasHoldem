#auto-py-to-exe || pyInstaller
import sys, time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
from GUIController import UI
from deck import Deck
from LinkedList import *
from Player import Player

class GameController():
    def __init__(self):
        self.GUI = UI.get_GUI()
        self.deck = Deck.get_deck()
        self.player_hand_images = []
        # self.timer = QTimer(self.GUI)
        # self.timer.timeout.connect(self.assign_player_pixmaps)
        
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
        self.GUI.SendButton.clicked.connect(self.determine_opening_D_index)
        self.first_cards = []

        
    def determine_opening_D_index(self):

        for player in self.players.iterate_from(self.players.head):
            card = self.deck.select_card(True)
            self.first_cards.append(player.dataval.create_hand_images(card))
        
            print(card)
        # self.timer.start(1000)
        # self.GUI.find_winner()

        
    
    def assign_player_pixmaps(self):
        print("hello")
        
        card_index = 0
        for hand in self.first_cards:
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
        time.sleep(1.5)
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
    RC = GameController()
    RC.determine_opening_D_index()
    RC.assign_player_pixmaps()
    # QTimer.singleShot(10, RC.assign_player_pixmaps)
    # cards = RC.determine_opening_D_index()
    # UIWindow = UI()
    app.exec_()
    
    # for i in range(len(cards)):
    #     print(cards[i])