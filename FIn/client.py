import pygame, sys
from network import Network
from clue import Player
from pygame.locals import *
import os, random
from Deck import Deck

pygame.init()
width = 900
height = 900
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

TILE_WIDTH = 30
TILE_HEIGHT = 30
TILE_MARGIN = 1
TILE_SIZE = TILE_WIDTH + TILE_MARGIN
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
LIGHT_GREEN = 38, 77, 0
RED = 255, 0, 0
YELLOW = 250, 230, 0
BROWN = 128, 128, 0
SAFFRON = 255, 153, 51
LIGHT_BLUE = 201, 255, 229
PINK = 241, 156, 187
AQUA = 16, 206, 200
GRAY = 160, 160, 160
GOLD = 181, 152, 73
VIOLET = 153, 51, 255
BLUE = 68, 106, 255
WHITE = 255, 255, 255
font = pygame.font.SysFont(None, 25)  # default font set at 21 points
player_font = pygame.font.SysFont(None, 50)


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)  ## defining the text object with font and color
    textrect = textobj.get_rect()  # getting size and location of this text object
    textrect.topleft = (x, y)  ## setting the location of the text object
    surface.blit(textobj, textrect)  ## displaying the textobject at the text location


# doc = pygame.Rect(10, 10, 10, 10)
# docImage = pygame.image.load("images/doc.bmp")
# docStretched = pygame.transform.scale(docImage, (40,40))

def move(win):
    # doctor
    column = 10
    row = 10
    # pygame.draw.rect(win, BLACK, [TILE_SIZE*column+TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN,TILE_WIDTH,TILE_HEIGHT])
    drawText("D", player_font, win, TILE_SIZE * column, TILE_SIZE * row)


# print(nurseImage)
# DRAW HALLWAYS
hall = WHITE


def draw(col1, col2, row1, row2):
    for column in range(col1, col2):
        for row in range(row1, row2):
            pygame.draw.rect(win, (hall),
                             [TILE_SIZE * column + TILE_MARGIN, TILE_SIZE * row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])


def drawHalls(win):
    ## Study to Library
    draw(3, 4, 6, 11)
    ## Library to Conservatory
    draw(3, 4, 16, 21)
    ## Conservatory to Ballroom
    draw(6, 10, 24, 25)
    ## Ballroom to Kitchen
    draw(18, 22, 24, 25)
    ## Kitchen to Dining
    draw(24, 25, 16, 21)
    ## Dining to Lounge
    draw(24, 25, 6, 11)
    ## Lounge to Hall
    draw(18, 22, 3, 4)
    ## Study to Hall
    draw(6, 10, 3, 4)
    ## Library to Billiard
    draw(6, 10, 13, 14)
    ## Billiard to Dining
    draw(18, 22, 13, 14)
    ## Billiard to Ballroom
    draw(13, 14, 17, 21)
    ## Billiard to Hall
    draw(13, 14, 6, 10)


def redrawWindow(win, player, player2):
    win.fill((52, 54,
              54))  ## the color of the tile margins -- for now will have a slightly lighter color so the labels themselves can pop out more

    pygame.draw.rect(win, (0, 0, 0), [0, 0, TILE_WIDTH, TILE_HEIGHT])

    ## draw out the yellow tiles
    for column in range(TILE_WIDTH):
        for row in range(TILE_HEIGHT):
            pygame.draw.rect(win, (YELLOW),
                             [TILE_SIZE * column + TILE_MARGIN, TILE_SIZE * row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    ## Top Level Rooms

    # Add Study
    for column in range(1, 6):
        for row in range(1, 6):
            pygame.draw.rect(win, (VIOLET),
                             [TILE_SIZE * column + TILE_MARGIN, TILE_SIZE * row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Study", font, win, 40, 80)

    # Add Hall
    for column in range(10, 18):
        for row in range(1, 6):
            pygame.draw.rect(win, (SAFFRON),
                             [TILE_SIZE * column + TILE_MARGIN, TILE_SIZE * row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Hall", font, win, 330, 80)

    # Add Lounge
    for column in range(22, 27):
        for row in range(1, 6):
            pygame.draw.rect(win, (GRAY),
                             [TILE_SIZE * column + TILE_MARGIN, TILE_SIZE * row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Lounge", font, win, 700, 80)

    ## Middle Level Rooms

    # Add Library
    for column in range(1, 6):
        for row in range(11, 16):
            pygame.draw.rect(win, (AQUA),
                             [TILE_SIZE * column + TILE_MARGIN, TILE_SIZE * row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Library", font, win, 40, 390)

    # Add Billiard
    for column in range(10, 18):
        for row in range(10, 17):
            pygame.draw.rect(win, (LIGHT_GREEN),
                             [TILE_SIZE * column + TILE_MARGIN, TILE_SIZE * row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Billiard Room", font, win, 330, 390)

    # Add Dining
    for column in range(22, 27):
        for row in range(11, 16):
            pygame.draw.rect(win, (BLUE),
                             [TILE_SIZE * column + TILE_MARGIN, TILE_SIZE * row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Dining Room", font, win, 700, 390)

    ## Bottom Level Rooms

    # Add Conservatory
    for column in range(1, 6):
        for row in range(21, 28):
            pygame.draw.rect(win, (RED),
                             [TILE_SIZE * column + TILE_MARGIN, TILE_SIZE * row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Conservatory", font, win, 40, 690)

    # Add Ballroom
    for column in range(10, 18):
        for row in range(21, 28):
            pygame.draw.rect(win, (PINK),
                             [TILE_SIZE * column + TILE_MARGIN, TILE_SIZE * row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Ballroom", font, win, 330, 690)

    # Add Kitchen
    for column in range(22, 27):
        for row in range(21, 28):
            pygame.draw.rect(win, (LIGHT_BLUE),
                             [TILE_SIZE * column + TILE_MARGIN, TILE_SIZE * row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Kitchen", font, win, 700, 690)

    drawHalls(win)
    player.draw(win)
    player2.draw(win)

    player.show_accusation_and_suggestion()
    player2.show_accusation_and_suggestion()

    pygame.display.update()


# move(win)

def terminate():
    pygame.quit()
    sys.exit()


def card_solution(DC, NoP):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        for i in range(NoP):
            print('Your cards: ', ', '.join(DC[i]))


def start_game(self, username):
    self.username = username
    self.state = self.client.start_new_game()
    self.game_id = self.state.game_id
    self.suspect = self.client.get_player(self.username).suspect


def main():
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    NoP = 1
    D = Deck()
    DC = D.DistributeCards(NoP)
    run = True
    counter = 0
    while run:
        clock.tick(900)
        current_game_state = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if counter == 0:
            p.player_info()

        #if game_state.
        # start_game(p, p.player_info)
        card_solution(DC, NoP)
        p.move()
        p.make_accusation_and_suggestion()
        redrawWindow(win, p, current_game_state)
        counter += 1
    # pygame.display.update()


main()