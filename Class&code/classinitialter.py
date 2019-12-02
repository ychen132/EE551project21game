class GameInitialter:
    def __init__(self):
        self.cards = DealCard()
        self.player= Player()
        self.computer= Player()
        self.total_score = numpy.array([0,0])
        """when initiating the class, create parameters that we wrote before"""


    def startgame(self):
        Round=1
        while len(self.cards.MoreCard())>15:
            self.player.clear_card()
            self.computer.clear_card()
            input('Start Game! <<ENTER>>')
            print('Round:',end= " ")
            print ( Round)
            print('-'*50)
            score = self.Cal_round()
            self.total_score = self.total_score + score
            print('Total score is',end=" ")
            print(self.total_score[0], end= " ")
            print(self.total_score[1])
            Round = Round+1
            self.continue_or_not()

    """Funtion start game is called when the game is started, it gives a condition that when the 
    final card pool has less than 15 cards, the game is no longer playable 
    It also clears card from the previous round and keep track of the score and runs"""


    def CardAction(self):
        AskAction = input("DO you want more cards? [Y/N]")
        if AskAction == "Y" :
            self.cards.send_card(self.player)
            return True
        elif AskAction =="N":
            print('You have finished your round, wait for computers')
        else:
            print('hmmm what?')
            return self.CardAction()
        """Card action let the player to indicate they want more card or not"""


    def continue_or_not(self):
        AnotherRound = input("Want to play another round [Y/N]")
        if AnotherRound =='Y':
            if len(self.cards.MoreCard())<15:
                print('Opps run out of cards')
                input('Gameover')
                exit(1)
            else:
                return True
        elif AnotherRound =='N':
            print("Thank you for playing this game!")
            exit(1)
        else:
            print('hmmm what?')
            self.continue_or_not()

        """Continue function is used to let player to decide whether they want to keep playing or not
        Also it is able to terminate the game if the card pool has less than 15 cards"""


    def Cal_round(self):
        self.cards.send_card(self.player,2)
        self.cards.send_card(self.computer,2)

        self.player.display_card(0)
        self.computer.display_card(1,False)

        score = numpy.array([self.player.calculate_score(),self.computer.calculate_score()])
        if score[0]==21 or score[1]==21:
            print('wow, 21 points in the first round!')
            self.player.display_card(0)
            self.computer.display_card(1)
            return self.comparescore(score[0],score[1])
        else:
            while score[0]< 21:
                AskforOneMore = self.CardAction()
                if AskforOneMore:
                    self.player.display_card(0)
                    score[0]=self.player.calculate_score()
                    if score[0]>21:
                        print( "Ouch more than 21, you lost")
                        self.computer.display_card(1)
                        return self.comparescore(score[0],score[1])
                    elif score[0]== 21:
                        print("wow, you get a BlackJack! Let's wait to see what computer gets")
                        while score[1] < score[0]:
                            self.cards.send_card(self.computer)
                            score[1]=self.computer.calculate_score()
                        if score[1]==score[0]:
                            print("Computer gets a BlackJack too! Its a tie")
                            self.player.display_card(0)
                            self.computer.display_card(1)
                            return self.comparescore(score[0],score[1])
                        else:
                            print("You win! Computer does not get a BlackJack")
                            self.player.display_card(0)
                            self.computer.display_card(1)
                            return self.comparescore(score[0],score[1])
                    else:
                        continue
                elif not AskforOneMore:
                    while score[1]<score[0]:
                        self.cards.send_card(self.computer)
                        score[1]=self.computer.calculate_score()
                    self.player.display_card(0)
                    self.computer.display_card(1)
                    print()
                    return self.comparescore(score[0],score[1])
                else:
                    continue

    """Cal_round is used to calculate the total score and compare them, it includes every possibility 
    that the players can get into. """


    def comparescore(self, score1, score2):
        if score1 >21 and score2>21:
            print("Its a tie!", end=" ")
            print(score1, end=" ")
            print(score2)
            return numpy.array([0,0])
        elif score1 >21 and score2 <=21:
            print("Computer win!")
            print(score1, end=" ")
            print(score2)
            return numpy.array([0,1])
        elif score1 <=21 and score2 >21:
            print("You win! ")
            print(score1, end=" ")
            print(score2)
            return numpy.array([1,0])
        elif score1<=21 and score2<=21:
            if score1<score2:
                print("Computer win! ")
                print(score1, end=" ")
                print(score2)
                return numpy.array([0,1])
            elif score1>score2:
                print("You win!")
                print(score1, end=" ")
                print(score2)
                return numpy.array([1,0])
            else:
                print("Its a tie!")
                print(score1, end=" ")
                print(score2)
                return numpy.array([0,0])

    """After receiving information from the Cal_round, comparescore is able to compare the score from the player
    and keeps track of the total score from the round"""
