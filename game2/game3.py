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


p = 0



class Game:
	pygame.init()


	def __init__(self):
		self.settings =Settings()


	def run_game(self):
		running = True
		while running:
			screen.fill((0,0,0))
			screen.blit(message,(20,50))

			eventGame()

			player(playerX,playerY)
			

			


			pygame.display.update()













def eventGame():
	for event in pygame.event.get():
		global p
		if event.type == pygame.QUIT:
			global running
			running = False
		
		elif event.type == pygame.KEYDOWN:

			p = _event_key_down(event)

			#elif event.key == pygame.K_SPACE:
				# if bullet_state is 'ready':
				# 	bulletX = playerX
				# 	fire_bullet(bulletX,bulletY)

		elif event.type == pygame.KEYUP:
			
			p = _event_key_up(event)

	moveIwo(p)

def _event_key_down(event):
	p_change = 0
	if event.key == pygame.K_LEFT:
		p_change -= 1
	elif event.key == pygame.K_RIGHT:
		p_change += 1
	return p_change


def _event_key_up(event):
	p_change = 0
	if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
		p_change = 0
	return p_change



def moveIwo(p):
	global playerX
	playerX += p
	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736





p_change=0






if __name__ == '__main__':
    ga = Game()
    ga.run_game()
