import pygame
import random
pygame.init()
pygame.font.init()
#VARIABLES
mainfont = pygame.font.SysFont('Comic Sans MS', 30)
screenwidth = 700
screenheight = 600
window = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Space Game")
clock = pygame.time.Clock()
run = True
mainmenubool = True
gamebool = False
storebool = False
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
player_x = screenwidth/2-20
player_y = screenheight/2+200
player_speed = 10
bullets = []
bulletspeed = 5
meteorspeed = 2
meteors = []
meteors_destroyed = []
points = 0
lives = 10


#Loading Images
ship = pygame.image.load("sprites/ship.png")
ship = pygame.transform.scale(ship, (65,65))
ship2 = pygame.image.load("sprites/ship2.png")
ship2 = pygame.transform.scale(ship2,(65,65))
bullet2 = pygame.image.load("sprites/bullet2.png")
#bullet2 = pygame.transform.scale(bullet2,())
startmenu_image = pygame.image.load("sprites/planet.png")
bullet_image = pygame.image.load("sprites/bullet.png")
bullet_image = pygame.transform.scale(bullet_image, (10, 15))
alien_image = pygame.image.load("sprites/alien.png")
alien_image = pygame.transform.scale(alien_image, (10,10))
meteor_image = pygame.image.load("sprites/asteroid.png")
background = pygame.image.load("sprites/background.png")


class meteor(object):
    def __init__(self, x, y, speed, sprite):
        self.x = x
        self.y = y
        self.speed= speed
        self.sprite = sprite

    def draw(self):
        global lives
        window.blit(self.sprite, (self.x,self.y))
        self.y += self.speed
        if self.y >= screenheight:
            meteors.pop()
            lives -= 1


class bullet(object):
    def __init__(self, x, y, speed, sprite):
        self.x = x
        self.y = y
        self.speed = speed
        self.sprite = sprite

    def draw(self):
        window.blit(self.sprite, (self.x, self.y))
        self.y -= self.speed

    def drawenemybullet(self):
        pass


class player(object):
    def __init__(self, x, y, speed, sprite):
        self.x = x
        self.y = y
        self.speed = speed
        self.sprite = sprite

    def draw(self):
        if key[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= self.speed
            elif self.x <= 0:
                self.x = screenwidth
        if key[pygame.K_RIGHT]:
            if self.x < screenwidth:
                self.x += self.speed
            elif self.x >= screenwidth:
                self.x = 0

        window.blit(self.sprite,(self.x,self.y))

mainplayer = player(player_x,player_y,player_speed, ship)

def mainmenu():
    global mainmenubool
    global gamebool
    global storebool
    global screenheight
    global screenwidth
    global startmenu_image
    window.blit(startmenu_image,(0,0))
    if key[pygame.K_RETURN]:
        mainmenubool = False
        gamebool = True
        storebool = False
    if key[pygame.K_TAB]:
        storebool = True
        mainmenubool = False
        gamebool = False

def gameover():
    window.fill((0,0,0))
    print("TEST")

def game():
    global mainmenubool
    global gamebool
    global storebool
    global player_x
    global player_y
    global player_speed
    global bullets
    global meteors
    global meteor_image
    global meteorspeed
    global meteors_destroyed
    global lives
    global points
    if lives <= 0:
        gameover()
    window.fill(BLACK)
    window.blit(background,(0,0))
    score_text = mainfont.render(f"Score: {points}", False, (255,255,255))
    lives_text = mainfont.render(f"Lives: {lives}", False, (255,255,255))
    window.blit(score_text,(10,10))
    window.blit(lives_text,(555,10))
    mainplayer.draw()
    meteorspawn_posX = random.randint(50,650)
    if len(meteors) < 1:
        meteors.append(meteor(meteorspawn_posX, -100-meteor_image.get_height(),  meteorspeed, meteor_image))
    for item in meteors:
        item.draw()

    if key[pygame.K_SPACE]:
        if len(bullets) <= 20:
            bullets.append(bullet(mainplayer.x+27, mainplayer.y-6, bulletspeed, bullet_image))
    for item in bullets:
        if item.y <= 0:
            bullets.pop(bullets.index(item))
        item.draw()
    print(meteorspeed)
    if len(meteors_destroyed) > 2:
        meteors_destroyed = []
        meteorspeed += 1
    #Collision
    shiphitbox1 = mainplayer.x
    shiphitbox2 = mainplayer.x + mainplayer.sprite.get_width()//2
    shiphitbox3 = mainplayer.x + mainplayer.sprite.get_width()
    print(shiphitbox3)
    for meteoritem in meteors:
        meteor_hitbox = list(range(meteoritem.x,meteoritem.x+meteoritem.sprite.get_width()))
        #IF BULLET HITS METEOR
        for bulletitem in bullets:
            if (bulletitem.x in meteor_hitbox) and (bulletitem.y <= meteoritem.y+meteoritem.sprite.get_height()):
                try:
                    meteors.pop(meteors.index(meteoritem))
                except:
                    print("Meteor not in list")
                meteors_destroyed.append(meteoritem)
                bullets.pop(bullets.index(bulletitem))
                points += 100

        #IF METEOR HITS SHIP
        if (shiphitbox1 in meteor_hitbox or shiphitbox2 in meteor_hitbox or shiphitbox3 in meteor_hitbox) and (meteoritem.y+meteoritem.sprite.get_height() >= mainplayer.y):
            try:
                meteors.pop(meteors.index(meteoritem))
            except:
                print("Error: Meteor not in list")
            meteors_destroyed.append(meteoritem)
            lives -= 1


    if key[pygame.K_ESCAPE]:
        gamebool = False
        mainmenubool = True
        storebool =False

def store():
    global mainmenubool
    global gamebool
    global storebool
    window.fill(RED)



    if key[pygame.K_ESCAPE]:
        mainmenubool = True
        gamebool = False
        storebool = False
while run:
    window.fill((0,0,0))
    clock.tick(60)
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if mainmenubool:
        mainmenu()
    elif gamebool:
        game()
    elif storebool:
        store()


    pygame.display.update()
