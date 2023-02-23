import pygame, sys
import pygame.gfxdraw

#general variables
screenWidth = 1280
screenHeight = 720
fps = 60

boxBorder = 16
outerBoxSize = 450
innerBoxSize = outerBoxSize - boxBorder

#physics variables
gravity = 9.81
kineticEfficiency = .9
frictionEfficiency = .95
thresholdY = .25
thresholdX = .2

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
ball = Ball(ballPos, 20, ballV0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), outerBox)
    pygame.draw.rect(screen, (0, 0, 0), innerBox)

    #gravitational acceleration
    ball.velocity.y += gravity/60

    #boundaries
    #bottom
    if ball.pos.y + ball.radius + ball.velocity.y >= ((screenHeight - innerBoxSize) / 2) + innerBoxSize - 1:
        ball.pos.y = ((screenHeight - innerBoxSize) / 2 + innerBoxSize) - ball.radius - 1 
        ball.velocity.y *= -1
        ball.velocity.y *= kineticEfficiency
        ball.velocity.x *= frictionEfficiency

        if abs(ball.velocity.x) < thresholdX:
            ball.velocity.x = 0
    
        if abs(ball.velocity.y) < thresholdY:
            ball.velocity.y = 0
            ball.pos += ball.velocity
    #top
    elif ball.pos.y - ball.radius + ball.velocity.y <= ((screenHeight - innerBoxSize) / 2) + 1:
        ball.pos.y = ((screenHeight - innerBoxSize) / 2) + ball.radius + 1
        ball.velocity.y *= -1
        ball.velocity.y *= kineticEfficiency
        ball.velocity.x *= frictionEfficiency
    #left
    elif ball.pos.x - ball.radius + ball.velocity.x <= ((screenWidth - innerBoxSize) / 2) + 1:
        ball.pos.x = ((screenWidth - innerBoxSize) / 2) + ball.radius + 1
        ball.velocity.x *= -1
        ball.velocity.y *= frictionEfficiency
        ball.velocity.x *= kineticEfficiency
    #right
    elif ball.pos.x + ball.radius + ball.velocity.x >= ((screenWidth - innerBoxSize) / 2) + innerBoxSize - 1:
        ball.pos.x = ((screenWidth - innerBoxSize) / 2) + innerBoxSize - ball.radius - 1
        ball.velocity.x *= -1
        ball.velocity.y *= frictionEfficiency
        ball.velocity.x *= kineticEfficiency
    else:
        ball.pos += ball.velocity

    pygame.gfxdraw.aacircle(screen, int(ball.pos.x), int(ball.pos.y), ball.radius, (255, 0, 0))
    pygame.gfxdraw.filled_circle(screen, int(ball.pos.x), int(ball.pos.y), ball.radius, (255, 0, 0))
    pygame.display.update()
    clock.tick(fps)