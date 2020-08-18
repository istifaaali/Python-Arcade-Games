import pygame
import random
import time

pygame.init()

screenwidth = 500
screenheight = 700
window = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Galaga")
clock = pygame.time.Clock()

#ball_posX = int(screenwidth/2)
#ball_posY = screenheight - 100
#speed = 50

# Spirtes
ship = pygame.image.load("ship.png")
ship = pygame.transform.scale(ship, (50, 50))
bg = pygame.image.load("bg.jpg")
bulletpng = pygame.image.load("bullet.png")
bulletpng = pygame.transform.scale(bulletpng, (6,16))

fire_asteroid_images = [pygame.image.load("nruhh.png"),pygame.image.load("asteroid2.png"),pygame.image.load("asteroid3.png")]
asteroid1 = fire_asteroid_images[0]
explosionsprites = [pygame.image.load("explosion1.png"),pygame.image.load("explosion2.png"),pygame.image.load("explosion3.png"),pygame.image.load("explosion4.png"), pygame.image.load("explosion5.png")]
explosionsprite1 = pygame.transform.scale(explosionsprites[0], (50,50))
explosionsprite2 = pygame.transform.scale(explosionsprites[1], (50,50))
explosionsprite3 = pygame.transform.scale(explosionsprites[2], (50,50))
explosionsprite4 = pygame.transform.scale(explosionsprites[3], (50,50))
explosionsprite5 = pygame.transform.scale(explosionsprites[4], (50,50))

explosionsprites1 = [pygame.image.load("shipexplosion1.png"),pygame.image.load("shipexplosion2.png"),pygame.image.load("shipexplosion3.png"),pygame.image.load("shipexplosion4.png")]
shipexplosionsprite1 = pygame.transform.scale(explosionsprites1[0], (100, 100))
shipexplosionsprite2 = pygame.transform.scale(explosionsprites1[1], (100, 100))
shipexplosionsprite3 = pygame.transform.scale(explosionsprites1[2], (100, 100))
shipexplosionsprite4 = pygame.transform.scale(explosionsprites1[3], (100, 100))
explosions = [shipexplosionsprite1,shipexplosionsprite2,shipexplosionsprite3,shipexplosionsprite4]

meteorsprites = [pygame.image.load("asteroid1.png"),pygame.image.load("asteroid2.png"),pygame.image.load("asteroid3.png")]



meteor_width = 71
meteor_height = 150



meteorspeed = 5
moremeteors = 0
playeralive = True

class entity(object):
	def __init__(self, posX, posY, speed, sprite):
		self.posX = posX
		self.posY = posY
		self.speed = speed
		self.sprite = sprite

	def draw(self, window, sprite, playeralive):
		if playeralive:
			window.blit(self.sprite, (self.posX ,self.posY))
		elif not playeralive:
			#DEATH ANIMATION
			playeralive = True

mainplayer = entity(int(screenwidth/2), screenheight-100, 30, ship)

class bullet(object):
	def __init__(self,posX,posY, speed, radius, sprite):
		self.posX = posX
		self.posY = posY
		self.speed = speed
		self.radius = radius
		self.sprite = sprite

	def draw(self, window):
		#window.blit(sprite, (self.posX, self.posY))
		#pygame.draw.circle(window,(252, 3, 23), (self.posX, self.posY), self.radius)

		window.blit(self.sprite, (self.posX,self.posY))
		self.posY -= self.speed 
		#pygame.display.update()

asteroid_animation_loop = 0

class meteor(object):
	def __init__(self, posX, posY, speed, sprite):
		self.posX = posX
		self.posY = posY
		self.speed = speed
		self.sprite = sprite

	def draw(self, window, frame):
		
		window.blit(self.sprite[0], (self.posX,self.posY)) 
		boxlist.append(collisionbox(self.posX,self.posY,self.sprite, meteorspeed))
		self.posY += self.speed


	def draw_fire_asteroid(self, window):
		global asteroid_animation_loop
		boxlist.append(collisionbox(self.posX,self.posY,self.sprite, fireasteroidspeed))
		self.posY += self.speed
		window.blit(self.sprite, (self.posX, self.posY))

class collisionbox(object):
	def __init__(self, posX, posY, sprite, speed):
		self.posX = posX
		self.posY = posY
		self.sprite = sprite
		self.speed = speed

	def drawbox(self, window):
		#pygame.draw.rect(window, (0,0,0), (self.posX,self.posY,self.sprite.get_width(),self.sprite.get_height()),1)
		pass

boxlist = []
bullets = []
meteors = []
fireasteroid = []
lives = 0
frame = 0

differencelist = []
ship_differencelist = []
obheight = None
bullposYpop = None
bullposXpop = None
explosionindex = 0
framestored = None

def redraw():
	global bg
	global bullets
	global boxlist
	global differencelist
	global obheight
	global bullposYpop
	global bullposXpop
	global explosionsprites
	global explosionindex
	global meteordestroyed
	global ship_differencelist
	global lives
	global score
	global mainplayer
	global frame
	global framestored

	mainplayerbox = collisionbox(mainplayer.posX,mainplayer.posY,mainplayer.sprite, 50)

	window.fill((0,0,0))
	window.blit(bg, (0,0))

	for meteor in meteors:
		meteor.draw(window, frame)
		if meteor.posY > screenheight:
			meteors.pop(meteors.index(meteor))
			lives += 1


	for asteroid in fireasteroid:
		#if fire_asteroid_chance:
		asteroid.draw_fire_asteroid(window)
		if asteroid.posY > screenheight:
			fireasteroid.pop(fireasteroid.index(asteroid))

	for bullet in bullets:
		bullet.draw(window)
		bullposYpop = bullet.posY
		bullposXpop = bullposXpop
		if bullet.posY < 0:
			bullets.pop(bullets.index(bullet))



	for ob in boxlist:
		obheight = ob.posX+ meteor_height
		boxlist.pop(boxlist.index(ob))
		ob.drawbox(window)
		line = (ob.posX, ob.posX+meteor_width)
		
		for element in differencelist:
			if len(differencelist) == meteor_width:
				differencelist = []

		range1 = ob.posX
		range2 = ob.posX + meteor_width

		for num in list(range(range1, range2)):
			differencelist.append(num)

		if len(ship_differencelist) == mainplayerbox.sprite.get_width():
			ship_differencelist = []

		shiprange1 = mainplayerbox.posX
		shiprange2 = mainplayerbox.posX + mainplayerbox.sprite.get_width()

		for num in list(range(shiprange1, shiprange2)):
			ship_differencelist.append(num)

		for bullet in bullets:
			for meteor in meteors:
				if bullet.posX in differencelist and bullet.posY <= ob.posY+meteor_height:
					meteors.pop(meteors.index(meteor))
					meteordestroyed += 1
					bullets.pop(bullets.index(bullet))
					score += 100



		for meteor in meteors:
			if (ob.posX+meteor_width//2 in ship_differencelist) or (ob.posX+meteor_width in ship_differencelist) or (ob.posX in ship_differencelist):
				if (ob.posY+meteor_height) >= mainplayerbox.posY:
					meteors.pop(meteors.index(meteor))
					while True:
						if frame in list(range(0,50)):
							window.blit(explosions[0], (mainplayer.posX,mainplayer.posY))
							frame += 1
						elif frame in list(range(50,100)):
							window.blit(explosions[1], (mainplayer.posX,mainplayer.posY))
							frame += 1
						elif frame in list(range(100, 150)):
							window.blit(explosions[2], (mainplayer.posX,mainplayer.posY))

							frame += 1
						elif frame in list(range(150,200)):
							window.blit(explosions[3], (mainplayer.posX,mainplayer.posY))

							frame += 1
						elif frame == 200:
							frame = 0
							break

					mainplayer.posX = int(screenwidth/2)
					mainplayer.posY = screenheight - 100
					meteordestroyed += 1
					lives += 1


	window.blit(scoretext, (10, 10))
	window.blit(textsurface,(380,10))
	mainplayer.draw(window, ship, playeralive)
	mainplayerbox.drawbox(window)
	pygame.display.update()




run = True

meteorindex = 1
meteordestroyed = 0

pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)
score = 0

def addscore(score):
	score += 50

while run:
	clock.tick(20)
	#print(pygame.time.get_ticks()//1000)
	if lives != 10:
		textsurface = myfont.render(f'Lives:{10-lives}', False, (255, 255, 255))
		scoretext = myfont.render(f"Score:{score}", False, (255, 255, 255))
		meteor_spawn_chance = [False,False,True,False,False,True]
		meteor_spawn_chance = random.choice(meteor_spawn_chance)
		fire_asteroid_chance = [True, True,True,False,False,False,False,False] #This makes it a 3/8 (38%) chance for a faster asteroid to spawn 
		fire_asteroid_chance = random.choice(fire_asteroid_chance)
		meteor_posX = random.randint(0, screenwidth - 100)
		meteor_posY = -150
		#meteorsprite = pygame.transform.sale(meteorsprite,(50,50))
		fireasteroid_posX = random.randint(0, screenwidth - 50)
		fireasteroid_posY = 0
		fireasteroidspeed = meteorspeed + 10

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("Program Terminated")
				run = False

		key = pygame.key.get_pressed()

		if key[pygame.K_RIGHT]:
			if mainplayer.posX != 450:
				mainplayer.posX += mainplayer.speed
				print(f"Right Key Pressed. PositionX: {mainplayer.posX}")
			elif mainplayer.posX >= 450:
				mainplayer.posX = 0

		if key[pygame.K_LEFT]:
			if mainplayer.posX > 0:
				mainplayer.posX -= mainplayer.speed
				print(f"Left Key Pressed. PostionX: {mainplayer.posX}")
			elif mainplayer.posX <= 0:
				mainplayer.posX = screenwidth-50

		if key[pygame.K_SPACE]:
			print("Space Bar Pressed")
			if len(bullets) < 15:
				bullets.append(bullet(mainplayer.posX+23, mainplayer.posY+-10, 8, 4, bulletpng))

		
		if len(meteors) < 1:
			if meteorspeed < 40:
				meteorspeed += 1
				meteors.append(meteor(meteor_posX, meteor_posY,meteorspeed,meteorsprites))
			elif meteorspeed == 40:
				#meteors.append(meteor(meteor_posX, meteor_posY,meteorspeed,meteorsprites))
				pass

		if len(fireasteroid) < 0:
			fireasteroid.append(meteor(fireasteroid_posX,fireasteroid_posY,fireasteroidspeed, asteroid1))

		redraw()

	elif lives == 10:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("Program Terminated")
				run = False
		window.fill((0,0,0))
		print("Out of lives\nGame Over!")
		gameover = myfont.render("Game Over!", False, (255, 255, 255))
		scoreboard = myfont.render(f"Score:{score}", False,(255,255,255))
		window.blit(scoreboard,(screenwidth/2-50,screenheight/2+100))
		window.blit(gameover,(screenwidth/2-50,screenheight/2))
		pygame.display.update()
		pygame.time.delay(10000)
		run = False
		

pygame.quit()
