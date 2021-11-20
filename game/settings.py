class Settings:
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #宇宙船の速度
        self.ship_speed = 1.5
        #弾の設定
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        #self.bullet_color2 = (90,60,60)
        self.bullets_allowed = 3
        #self.bullets_allowed2 = 2

        #エイリアン用
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1