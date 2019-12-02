import random
import numpy

class PokerCard:
    def __init__(self, card_number, card_text, card_index):
        self.card_text = card_text
        self.card_number = card_number
        self.card_index = card_index
        """Create the first class which is pokercard, as we all know, In the game of BlackJack, there is three 
        identity, which are card text, card number, and index. Card text is the card's image about what it is;
        card index is its type including  spates clubs diamonds and hearts. Finally, card number is what is worths"""


class DealCard:
    def __init__(self):
        self.cards = []
        total_card_number = [1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        total_card_text = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        total_card_index = "HSCD"
        """Define the index of the poker card as well as the numbers & texts
        Create the total card list"""

        for card_index in total_card_index:
            for i in range(len(total_card_text)):
                card=PokerCard(total_card_number[i], total_card_text[i],card_index)
                self.cards.append(card)
            """" Using for loops to create every single cards in the poker game.
                all cards are created in to a list with their types, text and related value
            THen we randomize the cards to create the card pool and be able to deal cards"""

        random.shuffle(self.cards)

    def MoreCard(self):
        return self.cards

    """Give cards to the player"""
    def send_card(self,player, num=1):
        for i in range(num):
            card = self.cards.pop()
            player.cards.append(card)
    """pop up one card initially from the card pool, reduce that card from the pool and
    then append it to the player's card list"""
