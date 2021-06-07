from random import shuffle
class Deck:
    __DECK_LENGTH  = 98
    __HAND_SIZE = [8,7,6]
    isEmpty = False

    def __init__(self):
        '''
        Constructor for the deck object, creates a shuffled deck of cards from 2 - 98
        '''
        self.deck = [i for i in range(2,100)]
        shuffle(self.deck)
        self.index = 0

    def dealHands(self,playerList):
        '''
        Deals hands to each player.
        :param playerList: A list of player objects
        :return: None
        '''
        if len(playerList) == 1:
            self.dealHand(playerList,self.__HAND_SIZE[0])
        elif len(playerList) == 2:
            self.dealHand(playerList,self.__HAND_SIZE[1])
        else:
            self.dealHand(playerList,self.__HAND_SIZE[2])

    def dealHand(self,playerList,cardAmount):
        '''
        Deals a starting hand to each individual player
        :param playerList: A list of player objects
        :param cardAmount: The amount to deal to each player
        :return: None
        '''
        for player in playerList:
            for i in range(cardAmount):
                self.draw(player.hand)

    def draw(self,hand):
        '''
        The list to draw a card from a deck
        :param hand: a list to put the drawn card into
        :return: the new hand
        '''
        if self.index < self.__DECK_LENGTH:
            hand.append(self.deck[self.index])
            self.index += 1
            if self.index >= self.__DECK_LENGTH:
                self.isEmpty = True
            return hand
        else:
            return hand



