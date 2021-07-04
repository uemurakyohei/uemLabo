import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,600))
# screen.fill((80,80,150))
pygame.display.set_caption('invader game')

#Player
playerImg = pygame.image.load('ewo_pixel.bmp')
playerImg = pygame.transform.scale(playerImg,(80,100))
playerX,playerY = 400,500
playerX_change = 0

def player(x,y):
	screen.blit(playerImg,(x,y))


#Text
font = pygame.font.SysFont(None,20)
message = font.render('Hello World',False,(255,255,255))


def eventGame():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			global running
			running = False
		
		if event.type == pygame.KEYDOWN:
			_event_key_down(event)		
			#elif event.key == pygame.K_SPACE:
				# if bullet_state is 'ready':
				# 	bulletX = playerX
				# 	fire_bullet(bulletX,bulletY)

		if event.type == pygame.KEYUP:
			_event_key_up(event)



def _event_key_down(event):
	p_change = 0
	if event.key == pygame.K_LEFT:
		p_change = -0.1
	elif event.key == pygame.K_RIGHT:
		p_change = 0.1
	moveIwo(p_change)


def _event_key_up(event):
	p_change = 0
	if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
		p_change = 0
	moveIwo(p_change)


def moveIwo(_change):
	global playerX
	global playerX_change
	playerX_change = _change
	playerX += playerX_change

	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736
	print(playerX)






running = True
while running:
	screen.fill((0,0,0))
	screen.blit(message,(20,50))

	eventGame()

	player(playerX,playerY)


	


	pygame.display.update()