#Clue-Less Game - Card Class
#Panagiotis Kazantzis

from random import shuffle, randint

PlayerNames = {
    -1: '-',
    0 : 'Colonel Mustard',
    1 : 'Miss Scarlet',
    2 : 'Professor Plum',
    3 : 'Mr. Green',
    4 : 'Mrs. White',
    5 : 'Mrs. Peacock'
    }

WeaponNames = {
    -1: '-',
    0 : 'Rope',
    1 : 'Lead Pipe',
    2 : 'Knife',
    3 : 'Wrench',
    4 : 'Candlestick',
    5 : 'Revolver'
    }

RoomNames = {
    -1: '-',
    0 : 'Study Room',
    1 : 'Hall',
    2 : 'Lounge',
    3 : 'Library',
    4 : 'Billiard Room',
    5 : 'Dining Room',
    6 : 'Conservatory',
    7 : 'Ball Room',
    8 : 'Kitchen'
    }


class Deck:
    PlayerCards = None
    WeaponCards = None
    RoomCards = None
    Solution = None

    def __init__(self):
        self.PlayerCards = set([i for i in range(6)])
        self.WeaponCards = set([i for i in range(6)])
        self.RoomCards = set([i for i in range(9)])
        p, w, r = randint(0,5), randint(0,5), randint(0,8)
        self.Solution = (p, w, r)
        
        self.PlayerCards.remove(p)
        self.WeaponCards.remove(w)
        self.RoomCards.remove(r)
        self.PlayerCards = list(self.PlayerCards)
        self.WeaponCards = list(self.WeaponCards)
        self.RoomCards = list(self.RoomCards)

    def DistributeCards(self, NoP):
        #if NoP < 3 or NoP > 6: # check number of players
           # return None
        shuffle(self.PlayerCards)
        shuffle(self.WeaponCards)
        shuffle(self.RoomCards)
        C = [PlayerNames[i] for i in self.PlayerCards] + [WeaponNames[i] for i in self.WeaponCards] + [RoomNames[i] for i in self.RoomCards]
        shuffle(C)
        R = [[] for i in range(NoP)]
        for i,c in enumerate(C):
            R[i % NoP].append(c)
        return R

#Demo
NoP = 3
#D = Deck()
#DC = D.DistributeCards(NoP)
#for i in range(NoP):
#    print('Player ' + str(i) + ' cards: ', ', '.join(DC[i]))



        
    