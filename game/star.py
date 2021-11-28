import pygame
from pygame.sprite import Sprite
from random import random
from math import floor

class Star(Sprite):
	def __init__(self,ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		#self.color = ai_game.settings.star_color
		self.rate = random()*random()


		self.rect = pygame.Rect(0,0,self.settings.star_width*self.rate,self.settings.star_height*self.rate)
		self.rect.x = self.rect.width
		self.rect.y = 0
		
		#座標を指定
		self.x = float(self.screen_rect.right * random())
		self.y = float(self.screen_rect.height * random())


		num = floor( 10 * random() )
		self.color = self.settings.star_colors[num]


	def check_edges(self):
		if self.rect.bottom == self.screen_rect.bottom:
			return True

	def update(self):
		self.y += (self.settings.star_speed * self.rate)
		self.rect.y = self.y


	def draw_star(self):
		pygame.draw.rect(self.screen,self.color,self.rect)





