from math import floor
class Player:
    handSize = 0

    def __init__(self):
        self.hand = []
        self.countByTens = [0 for i in range(10)]
        self.startBid = 0
        self.otherBid = 0
        self.isHandEmpty = False

    def __str__(self):
        return self.hand

    def firstBid(self,index=0):
        '''
        Calulates the bid for first based on cards close to 1 or 100.
        :param index: How close, by tens, to count close to 1 or 100
        :return:
        '''
        for card in self.hand:
            self.countByTens[floor(card / 10)] += 1
        self.startBid += self.countByTens[0 + index] + self.countByTens[9 - index]
