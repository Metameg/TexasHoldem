#auto-py-to-exe || pyInstaller

from GUIController import UI
from deck import Deck
from LinkedList import *
from Player import Player

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
        for i in range(1, self.numPlayers):
            new_player = Player(False, i+1)
            self.players.add_node(new_player)
            # Generate Villain pixmap
            # self.player_hand_images.append(new_player.create_hand_images())
    
    def determine_opening_D_index(self):
        first_cards = []
        
        for card in range(self.GUI.numPlayers):

            card = self.deck.select_card(True)
            first_cards.append(card)
        self.players
        # self.GUI.find_winner()

        return first_cards

    def post_blinds(self):
        SB_index = self.GUI.D_index + 1
        
        pass
    def bet_round(self):
        if self.betting_round == 'preflop':
            bet_start = self.GUI.SB_pos + 2


if __name__ == '__main__':
    RC = GameController()
    cards = RC.determine_opening_D_index()
    
    
    for i in range(len(cards)):
        print(cards[i])