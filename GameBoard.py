import Player
import Deck

class GameBoard:
    didWin = False
    didLose = False

    def __init__(self,numPlayers = 4):
        self.playerList = [Player.Player for i in range(4)]
        self.Deck = Deck.Deck()
        self.Deck.dealHands(self.playerList)
        self.piles = [1,1,100,100]


    def checkWin(self):
        if self.Deck.isEmpty:
            for player in self.playerList:
                if len(player.hand) != 0:
                    return False
            return True
        else:
            return False