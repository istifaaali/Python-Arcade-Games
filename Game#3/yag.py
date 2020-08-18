import pygame
import random

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comfortaa', 50)
screenwidth = 1080
screenheight = 608
window = pygame.display.set_mode((screenwidth,screenheight))
clock = pygame.time.Clock()


y1 = 0
x1 = 0
y2 = 100
x2 = screenwidth-10
vel = 20
ball_posX = screenwidth//2
ball_posY = screenheight//2
ball_speed = [-5,0]
points1 = 0
points2 = 0

white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]
yellow = [255, 255, 0]

mainmenubool = True
gamebool = False
gameoverbool = False

def gameover():
    global winner

    window.fill((127,194,236))
    if points1 == 10 or points2 == 10:
        if points1 == 10:
            winner = 1
        elif points2 == 10:
            winner = 2

    gameovertext1 = myfont.render(f"      Game Over!",False, (255,255,255))
    gameovertext2 = myfont.render(f"     Player {winner} Wins!",False, (255,255,255))
    gameovertext3 = myfont.render(f" Press ESC to Continue",False, (255,255,255))

    window.blit(gameovertext1, (screenwidth//2-150, screenheight//2-150))
    window.blit(gameovertext2, (screenwidth//2-150, screenheight//2-100))
    window.blit(gameovertext3, (screenwidth//2-150, screenheight//2-50))

def mainmenu():
    window.fill((black))
    starttext = myfont.render("Press SPACE to play and press ESC to Pause",False, (255,255,255))
    window.blit(starttext,(screenwidth//2-350,screenheight//2))

def game():
    window.fill((58,131,86))
    global ball_posX
    global ball_posY
    global y2
    global vel
    global y1
    global points1
    global points2
    global gameoverbool
    global gamebool

    if points1 == 10 or points2 == 10:
        gamebool = False
        gameoverbool = True

    pygame.draw.circle(window, white, (ball_posX,ball_posY), 10, 10)

    if keys[pygame.K_UP] and y2 - vel > -1:
        y2 -= vel
    if keys[pygame.K_DOWN] and y2 + 250 < 800:
        y2 += vel
    if keys[pygame.K_q] and y1 - vel > -1:
            y1 -= vel
    if keys[pygame.K_a] and y1 + 250 < 800:
            y1 += vel

    points_text1 = myfont.render(f"{points1}", False, (255,255,255))
    points_text2 = myfont.render(f"{points2}", False, (255,255,255))

    differencelist1 = list(range(y1,y1+100))
    differencelist2 = list(range(y2,y2+100))

    ball_dir = random.choice([1,2])
    ball_dir2 = random.choice([1,2])

    if ball_posX >= x2 and ball_posY in differencelist2:
        if ball_dir == 1:
            ball_speed[0] = -5
            ball_speed[1] = -2
        elif ball_dir == 2:
            ball_speed[0] = -5
            ball_speed[1] = 2

    if ball_posX == x1 and ball_posY in differencelist1:
        if ball_dir2 == 1:
            ball_speed[0] = 5
            ball_speed[1] = -2
        if ball_dir2 == 2:
            ball_speed[0] = 5
            ball_speed[1] = 2

    if ball_posY <= 0:
        if (ball_speed[0] == 5) and (ball_speed[1] == -2):
            ball_speed[1] = 2
        elif (ball_speed[0] == -5) and (ball_speed[1] == -2):
            ball_speed[1] = 2

    elif ball_posY >= screenheight:
        if (ball_speed[0] == -5) and (ball_speed[1] == 2):
            ball_speed[1] = -2
        elif (ball_speed[0] == 5) and (ball_speed[1] == 2):
            ball_speed[1] = -2

    elif ball_posX > screenwidth:
        ball_posX = screenwidth//2
        points1 += 1

    elif ball_posX < 0:
        ball_posX = screenwidth//2
        ball_speed[0] = 5
        ball_speed[1] = 0
        points2 += 1

    ball_posX += ball_speed[0]
    ball_posY += ball_speed[1]

    window.blit(points_text1,(20,screenwidth//2))
    window.blit(points_text2,(screenwidth-50,screenwidth//2))
    pygame.draw.rect(window, red, (x1, y1, 10, 100))
    pygame.draw.rect(window, blue, (x2, y2, 10, 100))
    pygame.draw.rect(window, white, [540, 0, 0, 608])

quit = False
while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
    keys = pygame.key.get_pressed()

    if mainmenubool:
        mainmenu()
        if keys[pygame.K_SPACE]:
            mainmenubool = False
            gamebool = True
    elif gamebool:
        if keys[pygame.K_ESCAPE]:
            mainmenubool = True
            gamebool = False
        game()

    elif gameoverbool:
        if keys[pygame.K_ESCAPE]:
            mainmenubool = True
            gamebool = False
            gameoverbool = False
            points1 = 0
            points2 = 0
        gameover()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
