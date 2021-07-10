
import sys
import pygame
from settings import Settings

from ship import Ship
from bullet import Bullet
from bullet2 import Bullet2


class AlienInvasion:
    
    def __init__(self):
        pygame.init()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("エイリアン侵略")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bullets2 = pygame.sprite.Group()

    
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_bullets2()
            self._update_screen()


 

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            #キーボードとマウスのイベントに対応する
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            #右移動
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            #左移動
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_a:
            self._fire_bullet2()


    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            #右移動
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            #左移動
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)

    def _fire_bullet2(self):
        if len(self.bullets2) < self.settings.bullets_allowed2:
            new_bullet2 = Bullet2(self)
            self.bullets2.add(new_bullet2)

    def _update_bullets2(self):
        self.bullets2.update()
        for bullet2 in self.bullets2.copy():
            if bullet2.rect.bottom >= 1000:
                self.bullets2.remove(bullet2)



    def _update_screen(self):
        #ループを通過するたびに画面を再描画する
        self.screen.fill(self.settings.bg_color)
        
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for bullet2 in self.bullets2.sprites():
            bullet2.draw_bullet2()
        
        pygame.display.flip()
        


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

