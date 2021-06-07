import Deck
import Player

if __name__ == '__main__':
    testDeck = Deck.Deck()
    testPlayer = Player.Player()
    testDeck.dealHands([testPlayer])
    print(testPlayer.hand)
    testPlayer.firstBid()
    print(testPlayer.startBid)