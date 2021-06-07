import Player
import Deck

class GameBoard:
    didWin = False
    didLose = False
    handsize = 0
    piles = [1, 1, 100, 100]

    def __init__(self, player, deck):
        '''
        A constructor for testing
        :param player: A player object
        :param deck: A deck object
        '''
        self.player = player
        self.deck = deck

    # def __init__(self,numPlayers = 4):
    #     self.playerList = [Player.Player for i in range(4)]
    #     self.Deck = Deck.Deck()
    #     self.Deck.dealHands(self.playerList)



    def playTurn(self):
        for player in self.playerList:
            self.checkJump(player)



    def checkJump(self,player):
        '''
        Checks to see if the player can make a jump in the opposite direction, and checks for double jumps
        :param player: The player object whose hand is in question
        :return:
        '''
        didJump = True
        while didJump:
            didJump = False
            numPlaced = 0
            for i in range(len(player.hand)):
                if player.hand[i - numPlaced] + 10 == self.piles[0]:
                    self.piles[0] = player.hand.pop(i - numPlaced)
                    didJump = True
                    numPlaced += 1
                elif player.hand[i - numPlaced] + 10 == self.piles[1]:
                    self.piles[1] = player.hand.pop(i - numPlaced)
                    didJump = True
                    numPlaced += 1
                elif player.hand[i - numPlaced] - 10 == self.piles[2]:
                    self.piles[2] = player.hand.pop(i - numPlaced)
                    didJump = True
                    numPlaced += 1
                elif player.hand[i - numPlaced] - 10 == self.piles[3]:
                    self.piles[3] = player.hand.pop(i - numPlaced)
                    didJump = True
                    numPlaced += 1


    def checkWin(self):
        if self.Deck.isEmpty:
            for player in self.playerList:
                if len(player.hand) != 0:
                    return False
            return True
        else:
            return False