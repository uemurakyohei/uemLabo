import pygame
from pygame.sprite import Sprite
from bullet import Bullet

class Bullet2(Bullet):
	def __init__(self,ai_game):
		super().__init__(ai_game)

		self.color = self.settings.bullet_color2


		#弾のrectを(0,0)の位置に作成してから、正しい位置を設定する
		self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop
		self.rect.midbottom = ai_game.ship.rect.midbottom

		self.y = float(self.rect.y)



	def update(self):
		if self.y <0:
			self.y -=self.settings.bullet_speed
			self.rect.y = self.y
		elif self.y == 0:
			self.y +=self.settings.bullet_speed
			self.rect.y = self.y

	def draw_bullet2(self):
		pygame.draw.rect(self.screen,self.color,self.rect)