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


running = True
while running:
	screen.fill((0,0,0))
	player(playerX,playerY)
	playerX += 0.01
	screen.blit(message,(20,50))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN

	pygame.display.update()