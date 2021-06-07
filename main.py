import Deck

if __name__ == '__main__':
    testing = Deck.Deck()
    for i in range(98):
        testing.draw([])
    print(testing.draw([]))
