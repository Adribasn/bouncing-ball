import pygame, sys
import math

#general variables
screenWidth = 1280
screenHeight = 720
fps = 60

boxBorder = 16
outerBoxSize = 450
innerBoxSize = outerBoxSize - boxBorder

#physics variables
gravity = 9.81
kineticEfficiency = .8

class Ball():
    def __init__(self, pos, radius, v0):
        self.pos = pos
        self.radius = radius
        self.velocity = v0

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight), flags=pygame.SCALED, vsync=1)
clock = pygame.time.Clock()
keysPressed = pygame.key.get_pressed()
outerBox = pygame.Rect((screenWidth - outerBoxSize) / 2, (screenHeight - outerBoxSize) / 2, outerBoxSize, outerBoxSize)
innerBox = pygame.Rect((screenWidth - innerBoxSize) / 2, (screenHeight - innerBoxSize) / 2, innerBoxSize, innerBoxSize)

ballPos = pygame.math.Vector2(screenWidth/2, screenHeight/2)
ballV0 = pygame.math.Vector2(0, 0)
ball = Ball(ballPos, 15, ballV0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), outerBox)
    pygame.draw.rect(screen, (0, 0, 0), innerBox)

    ball.velocity.y += gravity/60

    if ball.pos.y + ball.radius + ball.velocity.y >= ((screenHeight - innerBoxSize) / 2 + innerBoxSize):
        ball.pos.y = ((screenHeight - innerBoxSize) / 2 + innerBoxSize) - ball.radius
        ball.velocity.y *= -1
        ball.velocity.y *= kineticEfficiency
    else:
        ball.pos += ball.velocity
        

    pygame.draw.circle(screen, (255, 0, 0), (ball.pos), ball.radius)
    pygame.display.update()
    clock.tick(fps)