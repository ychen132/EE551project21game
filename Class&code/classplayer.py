class Player:
    def __init__(self):
        self.cards = []

        """Initialized a list Used to save players card from players"""

    def display_card(self, display=0, showcards = True):
        finalposition = len(self.cards)-1
        """count for the final cards"""
        if display == 0:
            userchange = ' Your cards are: '
        else:
            userchange= ' Computer cards are: '

        carddisplay = ''
        for i, card in enumerate(self.cards):
            if showcards:
                carddisplay = carddisplay+ (card.card_text + card.card_index)+ ', '
            else:
                if i< finalposition:
                    carddisplay= carddisplay+ (card.card_text + card.card_index)+', '
                else:
                    carddisplay = carddisplay+ '???'

        print(userchange+' ' + carddisplay)
        print()
        """The display function is used to display the cards of the player, it has two parameters.
         Display parameters is used to distinguish between computer's card or your's card, showcards are
         used to find how many cards to show"""

    def calculate_score(self):
        rScore = 0; """initialize the score"""
        for card in self.cards:
            rScore += card.card_number
            """go through the card the player has and calculate the total"""
        Have_A = False
        for i in self.cards:
            if i.card_text =='A':
                Have_A = True
                break
            else:
                continue

        if Have_A:
            if rScore <= 11:
                rScore = rScore + 10;
        return rScore

        """calculate_score is the function to figure out the total score of the player, including the
        special case of card Ace "A". """
    def clear_card(self):
        self.cards = []
        """clean up the cards for a new round"""


