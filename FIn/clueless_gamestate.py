import clue
import Deck
import uuid

"""
This class controls the games state of the clueless game

"""


class clueless_gamestate(object):

    def __init__(self, players, messages=None, turn_list=None,
                 current_player=None, turn_status=None, current_suggestion=None,
                 suggestion_response_player=None, game_winner=None, true_suspect_cards=None,
                 player_input = None):
        deck = Deck()
        self.game_winning_cards = deck.draw_winning_cards()
        self.players = players
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.position = [None, None]
        self.win = False
        self.player_input = player_input


        if messages:
            self.messages = messages
        else:
            self.messages = list()

        if turn_list:
            self.turn_list = turn_list
        else:
            self.turn_list = list(players)

        if current_player:
            self.current_player = current_player
        else:
            self.current_player = self.turn_list[0]

        if turn_status:
            self.turn_status = turn_status
        else:
            self.turn_status = clue.AWAITING_MOVE

        self.current_suggestion = current_suggestion
        self.suggestion_response_player = suggestion_response_player

        # the true suspect cards
        if true_suspect_cards:
            self.true_suspect_cards = true_suspect_cards
        else:
            self.true_suspect_cards = list()

        # holds the Player that is the final winner of the game
        self.game_winner = game_winner

    def get_player_input(self, p):
        return self.player_input[p]

    def start_game(self, player, input):
        self.player_input[player] = input
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def nextTurn(self):
        if self.p1Went:
            return self.p1Went
        else:
            return self.p2Went

    def handle_accusation(self, player, suspect, weapon, room):
        player_accusation = [suspect, weapon, room]
        winning_cards = [card for card in self.game_winning_cards]
        if set(player_accusation) == set(winning_cards):
            print ("winner!")
        else:
            print ("wrong accusation!")


        #p1 = self.player_input




