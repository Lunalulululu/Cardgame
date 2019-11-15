"""
#import pygame
import pygame

#initialize game engine
pygame.init()

window_width=500
window_height=500

animation_increment=10
clock_tick_rate=20

#Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

#Set title to the window
pygame.display.set_caption("Hello World")


dead=False

#Initialize values for color (RGB format)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
BROWN=(165,42,42)

clock = pygame.time.Clock()
screen.fill(WHITE)

def draw_tree():
    pygame.draw.rect(screen, BROWN, [260, 400, 30, 100])
    pygame.draw.polygon(screen, GREEN, [[350, 400], [275, 250], [200, 400]])
    pygame.draw.polygon(screen, GREEN, [[340, 350], [275, 230], [210, 350]])

while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
    draw_tree()
    pygame.display.flip()
    clock.tick(clock_tick_rate)

"""

from Players.AIPlayer import AIPlayer

"""pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('carimage.png')
gameDisplay.fill(white)
"""
player0 = AIPlayer([[]], 0, ['AH', '3S', '4S', '6H', '6S', '7S', '8D', '9C', '9S', 'JH'])
player1 = AIPlayer([[]], 0, ['AH', '3S', '4S', '6H', '6S', '7S', '8D', '9C', '9S', 'JH'])
player2 = AIPlayer([[]], 0, ['AH', '3S', '4S', '6H', '6S', '7S', '8D', '9C', '9S', 'JH'])
player3 = AIPlayer([[]], 0, ['AH', '3S', '4S', '6H', '6S', '7S', '8D', '9C', '9S', 'JH'])

player.do_discard()
print(player.hand)

player.do_grouping()
print(player.final_group)


"""
def car(x,y):
    gameDisplay.blit(carImg, (x, y))

x = display_width * 0.3
y = display_height * 0.5
x_change = 0

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    x += x_change
    gameDisplay.fill(black)
    car(x,y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
"""
