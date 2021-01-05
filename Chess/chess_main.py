###### this is our driver file
#
# responsible for user handling user input and game state object #######


import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512  # optional 400
DIMENSIONS = 8  # dimensions are 8x8
SQ_SIZE = HEIGHT // DIMENSIONS
MAX_FPS = 15  # For animation
IMAGES = {}

'''
Initialize global dictionary of images. this will be called once in the main
'''


def load_images():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR", "bp", "bR", "bN", "bB", "bQ", "bK", "bB", "bN",
              "bR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + "wp.png"), (SQ_SIZE, SQ_SIZE))


#         note: we can access an image by saying 'IMAGES['wp']

'''
main driver for our code  handles user input and updating graphics 
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    print(gs.board)
    load_images()  # only operated once
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            drawGameState((screen, gs))
            clock.tick(MAX_FPS)
            p.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen) #draw squares on board
    drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [p.Color("white", p.Color("grey"))]
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS:)



def drawPieces(screen, board):
    '''
    draws the pieces on the board using current gameState.board
    '''


if __name__ == "__main__":
    main()
