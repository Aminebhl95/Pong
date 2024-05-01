import pygame

pygame.init()

# Game Variables

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen_rect = screen.get_rect()

BLACK = (0,0,0)
WHITE = (255,255,255)

clock = pygame.time.Clock()

speed = [3, 3]

running = True

# Sounds
pygame.mixer.init()
bounce_sound = pygame.mixer.Sound("sound/bounce.wav")

# Score 
player1Score = 0
player2Score = 0

# font 
font = pygame.font.Font(None, 100)
player1Text = font.render(str(player1Score), True, WHITE, None)
player2Text = font.render(str(player2Score), True, WHITE, None)

# paddles and ball rect objects
ball = pygame.Rect(screen_rect.centerx, screen_rect.centery, 20, 20)
paddleLeft = pygame.Rect(10, SCREEN_HEIGHT //2 - 50, 20, 100)
paddleRight = pygame.Rect(SCREEN_WIDTH - 30, SCREEN_HEIGHT //2 - 50, 20, 100)


# Functions 

def ctrlBallBoundary(ball):
    global player1Score, player2Score,player1Text, player2Text
    

    if ball.bottom >= screen_rect.bottom or ball.top <= screen_rect.top:
        speed[1] = -speed[1]
        
    if ball.right >= screen_rect.right:
        ball.center = (screen_rect.centerx, screen_rect.centery)
        player1Score += 1
        player1Text = font.render(str(player1Score), True, WHITE, None)
        speed[0] += 1
        speed[1] += 1
        
    if ball.left <= screen_rect.left:
        ball.center = (screen_rect.centerx, screen_rect.centery)
        player2Score += 1
        player2Text = font.render(str(player2Score), True, WHITE, None)
        speed[0] += 1
        speed[1] += 1

    


while running:

    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # draw ball
    pygame.draw.rect(screen, WHITE, ball, 0, 20)

    # move ball and control it's boundaries
    ctrlBallBoundary(ball)
    ball.move_ip(speed)

    # draw paddles
    pygame.draw.rect(screen, WHITE, paddleLeft)
    pygame.draw.rect(screen, WHITE, paddleRight)

    # Move paddles and control their movemnet 

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_q] and not paddleLeft.bottom >= screen_rect.bottom:
        paddleLeft.bottom += 4
    elif keys[pygame.K_a] and not paddleLeft.top <= screen_rect.top:
        paddleLeft.top -= 4
    elif keys[pygame.K_UP] and not paddleRight.top <= screen_rect.top:
        paddleRight.top -= 4
    elif keys[pygame.K_DOWN] and not paddleRight.bottom >= screen_rect.bottom:
        paddleRight.bottom += 4


    if ball.colliderect(paddleRight):
        speed[0] = -speed[0]
        bounce_sound.play(0)
    if ball.colliderect(paddleLeft):
        speed[0] = -speed[0]
        bounce_sound.play(0)      

    # draw score
    screen.blit(player1Text, (320, 20))
    screen.blit(player2Text, (450, 20))

    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH//2, 0), (SCREEN_WIDTH//2, SCREEN_HEIGHT))

    pygame.display.update()
    clock.tick(60)

pygame.quit()