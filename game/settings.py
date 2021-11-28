class Settings:
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #宇宙船の速度
        self.ship_speed = 1.5
        self.ship_limit = 3
        #弾の設定
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        #self.bullet_color2 = (90,60,60)
        self.bullets_allowed = 3
        #self.bullets_allowed2 = 2

        #エイリアン用
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1



        #star用
        self.star_speed = 0.2
        self.star_width = 8
        self.star_height = 8
        self.star_color = (255,210,0)
        self.star_colors = ('#ffacfc','#f148fb','#7122fa','#560a86','#3b27ba','#e847ae','#13ca91','#ff9472','#ff8c00','#daa520')
        self.star_direction = 1
        self.stars_num = 500
