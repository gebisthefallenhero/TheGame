import Deck
import Player
import GameBoard

if __name__ == '__main__':
    # testDeck = Deck.Deck()
    # testPlayer = Player.Player()
    # testPlayer.hand = [18,27,28,26]
    # testGameBoard = GameBoard.GameBoard([testPlayer], testDeck)
    # testGameBoard.piles = [1,17,0,100]
    # testGameBoard.playTurn()
    # print(testGameBoard.playerList[0].hand)

    sum = 0
    for i in range(10000):
        testGameBoard = GameBoard.GameBoard()
        sum += testGameBoard.runGame()
    print(sum)

