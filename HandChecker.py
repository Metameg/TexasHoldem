
RANK_NAMES = {0: "2", 1: "3", 2: "4", 3: "5", 4: "6", 5: "7", 6: "8",
                    7: "9", 8: "10", 9: "jack",  10: "queen", 11: "king", 12: "ace"}
                    
class HandChecker(object):
    def __init__(self, all_cards, exposed_cards):
        self.all_cards = all_cards
        self.exposed_cards = exposed_cards
        self.exposed_card_coordinates = []
        self.pair_list = []        

    def _find_card_index(self, theList, item):
        for i in range(len(theList)):
            suit = theList[i]
            for j in range(len(suit)):
                if suit[j] == item: 
                    return (i, j)
        
    def _create_exposed_card_coordinates(self):
        for card in self.exposed_cards:
            card_coordinate = self._find_card_index(self.all_cards, card)
            self.exposed_card_coordinates.append(card_coordinate)

        return self.exposed_card_coordinates
  
    def _is_straight(self, rank_list):
        straight_count = 0
        straight_list = []
        straight_high = -1
         
        for rank in (12, *range(0, 13)):
            if rank in rank_list:
                straight_count += 1
                straight_list.append(rank)

                if straight_count >= 5:
                    straight_list.sort()
                    # For 6 and 7 card straights
                    if len(straight_list) > 5:
    
                        if 12 in straight_list and 0 in straight_list:
                            straight_list.remove(12)
                        straight_list = straight_list[-5:]

                    # If the second to last card in the straight is a 5 (index 3) and 
                    # an ace (index 12) exist in the straight, the ace is low and 
                    # the straight is 5 high.
                    if straight_list[-2] == 3 and max(straight_list) == 12: 
                        straight_high = 3
                        
                    else:
                        straight_high = max(straight_list)

                    
            else:
                straight_count = 0
                straight_list.clear()

        return straight_high   

    def _is_flush(self, suits):
        suited_rank = []
        completed_flush = []
        straight_flush_high = -1
        
        for card1 in range(len(suits)):  
            suit_to_match = -1     # Reset rank to match for three of kind counter when card1 changes
            suited_rank.clear()
            # Iterate through the rest of the cards in the exposed cards list and compare to card1
            for card2 in range(card1+1, len(suits)):
               
                if suits[card1] == suits[card2]:
                    if suit_to_match == -1:
                        suit_to_match = suits[card1]
                        suited_rank.append(self.exposed_card_coordinates[card1][1])
                        suited_rank.append(self.exposed_card_coordinates[card2][1])
                    
                    elif suits[card2] == suit_to_match:
                        suited_rank.append(self.exposed_card_coordinates[card2][1])
                        
                    # If there are 5 or more elements in the suited_rank list, find the max     
                    if len(suited_rank) >= 5 and len(suited_rank) > len(completed_flush):
                        completed_flush = [rank for rank in suited_rank]
                        completed_flush.sort()
                        completed_flush = completed_flush[::-1]
                        
                        # Check for straight flush
                        if self._is_straight(suited_rank) != -1:
                            straight_flush_high = self._is_straight(suited_rank)
            
            
        return [completed_flush, straight_flush_high]
                    
    def update_pair_list(self, card1, card2):
        # Check if card rank is the same
        if self.exposed_card_coordinates[card1][1] not in self.pair_list:

            # Only append to pair_list if it is a unique pair, three of a kinds
            # don't count
            self.pair_list.append(self.exposed_card_coordinates[card1][1])

    def determine_fullHouse_pair(self, rank):
        if rank == self.pair_list[0]:
            if len(self.pair_list) == 1:
                full_pair = -1
            if len(self.pair_list) == 2:
                full_pair = self.pair_list[1]
            if len(self.pair_list) == 3:
                full_pair = max(self.pair_list[1], self.pair_list[2])
                  
        elif rank == self.pair_list[1]:
            
            if len(self.pair_list) == 2:
                full_pair = self.pair_list[0]
            if len(self.pair_list) == 3:
                full_pair = max(self.pair_list[0], self.pair_list[2])
              
        elif rank == self.pair_list[2]:      
            full_pair = max(self.pair_list[0], self.pair_list[1])
        
        return full_pair

    def determine_highest_pairs(self):

        if len(self.pair_list) == 1:
            first_pair = self.pair_list[0]
            second_pair = -1
            return [first_pair, second_pair]
                
        if len(self.pair_list) == 2:
            first_pair = max(self.pair_list)
            second_pair = min(self.pair_list)
            return [first_pair, second_pair]
            
        if len(self.pair_list) == 3:
            self.pair_list.remove(min(self.pair_list))  # Remove the smallest pair

            first_pair = max(self.pair_list)
            second_pair = min(self.pair_list)
            return [first_pair, second_pair]
      
    def calculate_pair_type_attributes(self):
        # Hand type counters
        three_count = 0
        three_rank = -1
        fullHouse_pair = -1
        # Iterate through each of the tuples in the list of exposed cards
        for card1 in range(len(self.exposed_card_coordinates)):  
            rank_to_match = -1     # Reset rank to match for three of kind counter when card1 changes
             
            # Iterate through the rest of the cards in the exposed cards list and compare to card1
            for card2 in range(card1+1, len(self.exposed_card_coordinates)):

                if self.exposed_card_coordinates[card1][1] == self.exposed_card_coordinates[card2][1]:
                    
                    self.update_pair_list(card1, card2)

                    if rank_to_match == -1:
                        rank_to_match = self.exposed_card_coordinates[card1][1] 
                    elif self.exposed_card_coordinates[card2][1] == rank_to_match:
                        three_count += 1

                        # Set highest three of a kind rank
                        if rank_to_match > three_rank:
                            three_rank = rank_to_match
                    
                # If there are no pairs
                if len(self.pair_list) == 0:
                    sorted_pair_list = [-1, -1]

                # If there are pairs but no three of a kind
                if three_count < 1 and len(self.pair_list) > 0:
                    sorted_pair_list = self.determine_highest_pairs()
                    
                # If a three of a kind is detected, identify the full house if it exists.
                # Returns -1 for fullHouse_pair if full house doesn't exist      
                if three_count >= 1:
                    fullHouse_pair = self.determine_fullHouse_pair(three_rank)

        return [sorted_pair_list, three_rank, fullHouse_pair, three_count ]

    def create_kicker_list(self, ranks, num):
        ranks.sort()
        kicker_list = []
        kicker_list = [rank for rank in ranks[-(num):]]
            
        return kicker_list  
        
        
        
    def identify_hand(self):
        # Rank lists for detecting straight and flush type hands
        exposed_ranks = []
        exposed_suits = []
        # create a list of tuples representing each card that is exposed
        self._create_exposed_card_coordinates()
        # creates list of ranks of exposed cards
        for i in range(len(self.exposed_card_coordinates)): 
            rank = self.exposed_card_coordinates[i][1]
            exposed_ranks.append(rank)
        # creates list of suits of exposed cards
        for i in range(len(self.exposed_card_coordinates)): 
            suit = self.exposed_card_coordinates[i][0]
            exposed_suits.append(suit)


        # Pair type attributes are responsible for determining pairs, three of kinds, 
        # four of kinds, and full houses.
        pair_type_attributes = self.calculate_pair_type_attributes()

        pairs = pair_type_attributes[0]
        threeOfKind_rank = pair_type_attributes[1]
        fullHouse_pair = pair_type_attributes[2]
            
        threeOfKind_count = pair_type_attributes[3]            
        
        if self._is_flush(exposed_suits)[1] != -1:

            print(RANK_NAMES[self._is_flush(exposed_suits)[1]], "high straight Flush")
            return [8, self._is_flush(exposed_suits)[1]]
        
        elif  threeOfKind_count == 3:
            num_kickers = 1
            kicker_ranks = exposed_ranks.remove(threeOfKind_rank)
            kicker_list = self.create_kicker_list(kicker_ranks, num_kickers)    

            print("Four of a Kind", RANK_NAMES[threeOfKind_rank] + "'s", kicker_list[0])
            return[7, threeOfKind_rank, kicker_list[0]]
        
        elif fullHouse_pair != -1:
        
            print ("Full House", RANK_NAMES[threeOfKind_rank] + "'s", "over", RANK_NAMES[fullHouse_pair] + "'s" )
            return[6, threeOfKind_rank, fullHouse_pair]
        
        elif self._is_flush(exposed_suits)[0]:
        
            flush = self._is_flush(exposed_suits)[0]
        
            print(RANK_NAMES[flush[0]], "high flush.", flush[1], flush[2], flush[3], flush[4])
            return [5, flush[0], flush[1], flush[2], flush[3], flush[4]]
        
        elif self._is_straight(exposed_ranks) != -1:
        
            print(RANK_NAMES[self._is_straight(exposed_ranks)], "high straight")
            return[4, self._is_straight(exposed_ranks)]
        
        elif threeOfKind_count == 1:
            num_kickers = 2
            kicker_ranks = [rank for rank in exposed_ranks if rank != threeOfKind_rank]
            kicker_list = self.create_kicker_list(kicker_ranks, num_kickers)    
        
            print("Three of a Kind", RANK_NAMES[threeOfKind_rank] + "'s", RANK_NAMES[kicker_list[1]], RANK_NAMES[kicker_list[0]]) 
            return[3, threeOfKind_rank, kicker_list]
        
        elif pairs[1] != -1 and threeOfKind_count < 1:
            num_kickers = 1
            kicker_ranks = [rank for rank in exposed_ranks if (rank != pairs[0] and rank != pairs[1])]
            kicker_list = self.create_kicker_list(kicker_ranks, num_kickers)    
        
            print("Two Pair", RANK_NAMES[pairs[0]] + "'s", "and", RANK_NAMES[pairs[1]] + "'s", RANK_NAMES[kicker_list[0]])      
            return[2, pairs[0], pairs[1], kicker_list]
        
        elif pairs[0] != -1 and pairs[1] == -1:
            num_kickers = 3
            kicker_ranks = [rank for rank in exposed_ranks if rank != pairs[0]]
            kicker_list = self.create_kicker_list(kicker_ranks, num_kickers) 
            if (len(kicker_list) != 0):
                print("Pair of", RANK_NAMES[pairs[0]] + "'s", RANK_NAMES[kicker_list[2]], RANK_NAMES[kicker_list[1]], RANK_NAMES[kicker_list[0]])
            else:
                print("Pair of", RANK_NAMES[pairs[0]] + "'s")
            return[1, pairs[0], kicker_list]
        
        else:
            num_kickers = 5
            kicker_ranks = [rank for rank in exposed_ranks]
            kicker_list = self.create_kicker_list(kicker_ranks, num_kickers)  
            kicker_list = kicker_list[::-1] # Reverse list

            print("High Card", kicker_list)
            return [0, kicker_list]
        
        
    

        
        
        
        