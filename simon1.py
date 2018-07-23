import pygame, sys, random
from pygame.locals import *

pygame.init()

SURFACEX = 160
SURFACEY = 40
LIGHTS = 4
BOXSIZE = 40
LOBLUE = ( 60, 60,180)
HIBLUE = (150,150,255)
LORED  = (180, 50, 50) 
HIRED  = (255,100,100)
LOGREEN = (50, 180, 50)
HIGREEN = (100,255,100)
LOYELLOW = (180,180,0)
HIYELLOW = (255,255,20)
GREY = (40,40,40)

HIGHS = (HIBLUE, HIRED, HIGREEN, HIYELLOW)
LOWS  = (LOBLUE, LORED, LOGREEN, LOYELLOW)

SURF = pygame.display.set_mode((SURFACEX, SURFACEY))
pygame.display.set_caption('SIMON!')

def drawHigh(lnum):
    lxpos = lnum * BOXSIZE
    colour = HIGHS[lnum]
    pygame.draw.rect(SURF, colour, (lxpos,0,BOXSIZE,BOXSIZE))
    pygame.display.update()

def drawLow(lnum):
    lxpos = lnum * BOXSIZE
    colour = LOWS[lnum]
    pygame.draw.rect(SURF, colour, (lxpos,0,BOXSIZE,BOXSIZE))
    pygame.display.update()

def drawGrey(lnum):
    lxpos = lnum * BOXSIZE
    pygame.draw.rect(SURF, GREY, (lxpos,0,BOXSIZE,BOXSIZE))
    pygame.display.update()
    
def drawBoard():
    for light in range(LIGHTS):
        drawLow(light)

def flash(light):
    drawHigh(light)
    pygame.time.wait(500)
    drawLow(light)

def grey(light):
    drawGrey(light)
    
def flashAll():
    for light in range(LIGHTS):
        flash(light)
        
def lightAll():
    for light in range(LIGHTS):
        drawHigh(light)
        
def dimAll():
    for light in range(LIGHTS):
        drawLow(light)

def flashSeq(seq):
    for light in seq:
        flash(light)

def newTurn(seq):
    light = random.randint(0,3)
    newseq = seq + [light]
    flashSeq(newseq)
    return newseq

def rightBuzz(light):
    flash(light)
    
def wrongBuzz(light):
    grey(light)

def allRightBuzz():
    lightAll()
    pygame.time.wait(2000)
    dimAll()
    
def main():
    global target # current target light
    target = 0
    flashAll()
    pygame.time.wait(2000)
    sequence = newTurn([])
    
    while True: # main game loop
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
            pygame.display.update()

            if mouseClicked:
                lightClicked = mousex // 40
                if lightClicked == sequence[target]:
                    rightBuzz(lightClicked)
                    target = target + 1
                    if target == len(sequence):
                        allRightBuzz()
                        sequence = newTurn(sequence)
                        target = 0
                        print(sequence)
                else:
                    wrongBuzz(lightClicked)
                    pygame.quit()
                    sys.exit() 

if __name__ == '__main__':
    main()
