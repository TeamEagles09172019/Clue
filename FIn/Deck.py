# Clue-Less Game - Card Class
# Panagiotis Kazantzis

from random import shuffle, randint, random

PlayerNames = {
    -1: '-',
    0: 'Colonel Mustard',
    1: 'Miss Scarlet',
    2: 'Professor Plum',
    3: 'Mr. Green',
    4: 'Mrs. White',
    5: 'Mrs. Peacock'
}

WeaponNames = {
    -1: '-',
    0: 'Rope',
    1: 'Lead Pipe',
    2: 'Knife',
    3: 'Wrench',
    4: 'Candlestick',
    5: 'Revolver'
}

RoomNames = {
    -1: '-',
    0: 'Study Room',
    1: 'Hall',
    2: 'Lounge',
    3: 'Library',
    4: 'Billiard Room',
    5: 'Dining Room',
    6: 'Conservatory',
    7: 'Ball Room',
    8: 'Kitchen'
}


class Deck(object):
    PlayerCards = None
    WeaponCards = None
    RoomCards = None
    Solution = None

    def __init__(self):
        self.PlayerCards = set([i for i in range(6)])
        self.WeaponCards = set([i for i in range(6)])
        self.RoomCards = set([i for i in range(9)])
        p, w, r = randint(0, 5), randint(0, 5), randint(0, 8)
        self.Solution = (p, w, r)
        self._winning_cards = list()

        self.PlayerCards.remove(p)
        self.WeaponCards.remove(w)
        self.RoomCards.remove(r)
        self.PlayerCards = list(self.PlayerCards)
        self.WeaponCards = list(self.WeaponCards)
        self.RoomCards = list(self.RoomCards)
        self._game_cards = self.PlayerCards + self.WeaponCards + self.RoomCards

    def draw_winning_cards(self):
        """
        randomly select winning suspect, weapon, and room and
        return a list of the winning cards
        """
        # select the winning cards by choosing a random integer for each index
        # in the list and selecting the game card at that index
        winning_suspect = self.PlayerCards[
            random.choice(range(len(self.PlayerCards)))]
        winning_weapon = self.WeaponCards[
            random.choice(range(len(self.WeaponCards)))]
        winning_room = self.RoomCards[
            random.choice(range(len(self.RoomCards)))]

        # assign the selected winning cards to a list
        self._winning_cards = [winning_suspect, winning_weapon, winning_room]

        # remove the winning cards from the deck
        self._game_cards = [
            game_card for game_card in self._game_cards
            if game_card not in self._winning_cards
        ]
        return self._winning_cards

    def shuffle_cards(self):
        """
        shuffles the game cards
        """
        random.shuffle(self._game_cards)

    """
    deals the cards by taking the number of hands and return a list
    of lists that contain each separate hand
    """
    def DistributeCards(self, NoP):
        # if NoP < 3 or NoP > 6: # check number of players
        # return None
        shuffle(self.PlayerCards)
        shuffle(self.WeaponCards)
        shuffle(self.RoomCards)
        # C = [PlayerNames[i] for i in self.PlayerCards] + [WeaponNames[i] for i in self.WeaponCards]\
        #    + [RoomNames[i] for i in self.RoomCards]

        # shuffle(C)
        # R = [[] for i in range(NoP)]
        # for i, c in enumerate(C):
        #    R[i % NoP].append(c)
        #    print R
        # return R
        return [self._game_cards[x::NoP] for x in range(NoP)]


class GameCard(object):
    def _init__(self, item, item_type):
        self.item = item
        self.type = item_type

    def format(self):
        return {
            "item": self.item,
            "item_type": self.type

        }

# Demo
# NoP = 1
# D = Deck()
# DC = D.DistributeCards(NoP)
# for i in range(NoP):
#    print('Player ' + str(i) + ' cards: ', ', '.join(DC[i]))
