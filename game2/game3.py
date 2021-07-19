import pygame
from pygame import mixer














class Game:
	pygame.init()


	def __init__(self):

		#Player
		self.playerImg = pygame.image.load('ewo_pixel.bmp')
		self.playerI = pygame.transform.scale(self.playerImg,(80,100))
		self.playerX,self.playerY = 400,500
		self.playerX_change = 0

		#Text
		self.font = pygame.font.SysFont(None,20)
		self.message = self.font.render('Hello World',False,(255,255,255))



		self.screen = pygame.display.set_mode((800,600))
		# screen.fill((80,80,150))
		pygame.display.set_caption('invader game')

		self.running = True





	def run_game(self):
		while self.running:
			self.screen.fill((0,0,0))
			self.screen.blit(self.message,(20,50))
			self.eventGame()
			self.player()
			pygame.display.update()



	def player(self):
		self.screen.blit(self.playerI,(self.playerX,self.playerY))


	def eventGame(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			
			elif event.type == pygame.KEYDOWN:
				self._event_key_down(event)

				#elif event.key == pygame.K_SPACE:
					# if bullet_state is 'ready':
					# 	bulletX = playerX
					# 	fire_bullet(bulletX,bulletY)

			elif event.type == pygame.KEYUP:				
				self._event_key_up(event)

		self.moveIwo()

	def _event_key_down(self,event):
		if event.key == pygame.K_LEFT:
			self.playerX_change -= 1
		elif event.key == pygame.K_RIGHT:
			self.playerX_change += 1


	def _event_key_up(self,event):
		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
			self.playerX_change = 0

	def moveIwo(self):
		self.playerX += self.playerX_change
		if self.playerX <= 0:
			self.playerX = 0
		elif self.playerX >= 720:
			self.playerX = 720





if __name__ == '__main__':
    ga = Game()
    ga.run_game()
