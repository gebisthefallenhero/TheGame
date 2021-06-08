import Player
import Deck

class GameBoard:
    didLose = False
    handSize = 0
    piles = [1, 1, 100, 100]
    __MAX_GAP = 100
    __NO_PLAY = -1
    __PILE_IND = 0
    __GAP_IND = 1
    __HAND_IND = 2


    # def __init__(self, player, deck):
    #     '''
    #     A constructor for testing
    #     :param player: A player object
    #     :param deck: A deck object
    #     '''
    #     self.playerList = player
    #     self.deck = deck

    def __init__(self,numPlayers = 1):
        self.playerList = [Player.Player() for i in range(numPlayers)]
        self.deck = Deck.Deck()
        self.deck.dealHands(self.playerList)

    def runGame(self):
        '''
        Simulates a full game of The Game
        :return: None
        '''
        while self.didLose != True:
            self.playTurn()
            if self.didWin():
                return True
        if self.deck.index > 90:
            print("Happy Day")
        return False

    def playTurn(self):
        '''
        Playes one turn for each player in the game
        :return: None
        '''
        for player in self.playerList:
            numPlaced = self.checkJump(player)
            play1 = self.pickPlay(player)
            if numPlaced < 2 and play1[self.__PILE_IND] == -1:
                self.didLose = True
                return
            if play1[self.__PILE_IND] != -1:
                toRemove = self.handJumps(player,play1)
                self.piles[play1[self.__PILE_IND]] = player.hand.pop(play1[self.__HAND_IND])
                numPlaced += 1
                numPlaced += self.remCard(player,toRemove)
            numPlaced += self.checkJump(player)
            play2 = self.pickPlay(player)
            if numPlaced < 2 and play2[self.__PILE_IND] == -1:
                self.didLose = True
                return
            if play2[self.__PILE_IND] != -1:
                toRemove = self.handJumps(player, play2)
                self.piles[play2[self.__PILE_IND]] = player.hand.pop(play2[self.__HAND_IND])
                numPlaced += self.remCard(player, toRemove)
            for i in range(player.handSize - len(player.hand)):
                self.deck.draw(player.hand)


    def pickPlay(self,player):
        '''
        Goes through the players hand and picks the two cards that would result in the smallest jump.
        :param player: The player whose hand is in question
        :return: two tuples with (Index of pile to play on, Minimum distance, Index of car in hand)
        '''
        index1 = [self.__NO_PLAY, self.__MAX_GAP]
        for i in range(len(player.hand)):
            dist = [self.__NO_PLAY, self.__MAX_GAP,i]
            for up in range(2):
                gap = player.hand[i] - self.piles[up]
                if gap > 0 and gap < dist[self.__GAP_IND]:
                    dist[self.__PILE_IND] = up
                    dist[self.__GAP_IND] = gap
            for down in range(2,4):
                gap =  self.piles[down] - player.hand[i]
                if gap > 0 and gap < dist[self.__GAP_IND]:
                    dist[self.__PILE_IND] = down
                    dist[self.__GAP_IND] = gap
            if dist[self.__GAP_IND] < index1[self.__GAP_IND]:
                index1 = dist
        return index1

    def handJumps(self,player,play):
        toPlay = []
        playVal = player.hand[play[self.__HAND_IND]]
        if play[self.__PILE_IND] < 2:
            up = True
        else:
            up = False
        for card in player.hand:
            if up:
                if card == playVal + 10:
                    self.numBetween(player,card,playVal,toPlay)
                    return toPlay
            else:
                if card == playVal - 10:
                    self.numBetween(player,playVal,card,toPlay)
                    return toPlay
        return []

    def remCard(self,player,toRemove):
        '''
        Removes cards from the given list from the players hand
        :param player: The player whose hand to remove from
        :param toRemove: The cards to remove
        :return: None
        '''
        numPlays = 0
        for card in toRemove:
            if card in player.hand:
                player.hand.remove(card)
                numPlays += 1
        return numPlays

    def checkJump(self, player):
        '''
        Checks to see if the player can make a jump in the opposite direction, and checks for double and triple jumps
        :param player: The player object whose hand is in question
        :return: a integer value for the number of cards placed.
        '''
        didJump = True
        inBetween = []
        while didJump:
            didJump = False
            numPlaced = 0
            for i in range(len(player.hand)):
                if player.hand[i - numPlaced] + 10 == self.piles[0]:
                    self.numBetween(player, self.piles[0], player.hand[i - numPlaced], inBetween)#Card in players hand the low when going up
                    self.piles[0] = player.hand.pop(i - numPlaced)
                    didJump = True
                    numPlaced += 1
                elif player.hand[i - numPlaced] + 10 == self.piles[1]:
                    self.numBetween(player, self.piles[1], player.hand[i - numPlaced], inBetween)
                    self.piles[1] = player.hand.pop(i - numPlaced)
                    didJump = True
                    numPlaced += 1
                elif player.hand[i - numPlaced] - 10 == self.piles[2]:
                    self.numBetween(player, player.hand[i - numPlaced], self.piles[2], inBetween)
                    self.piles[2] = player.hand.pop(i - numPlaced)
                    didJump = True
                    numPlaced += 1
                elif player.hand[i - numPlaced] - 10 == self.piles[3]:
                    self.numBetween(player, player.hand[i - numPlaced], self.piles[3], inBetween)
                    self.piles[3] = player.hand.pop(i - numPlaced)
                    didJump = True
                    numPlaced += 1
        for card in inBetween:
            if card in player.hand:
                player.hand.remove(card)
                numPlaced += 1
        return numPlaced

    def numBetween(self,player,high,low,list):
        '''
        Method to determine the number of cards between a jump to be played by a certain player
        :param player: The player in question
        :param high: The high end of the range
        :param low: The low end of the range
        :param list: The list to be modified with the values the new value of cards to be played
        :return: the aforementioned list.
        '''
        for card in player.hand:
            if card > low and card < high:
                list.append(card)
        return list


    def didWin(self):
        if self.deck.isEmpty:
            for player in self.playerList:
                if len(player.hand) != 0:
                    return False
            return True
        else:
            return False