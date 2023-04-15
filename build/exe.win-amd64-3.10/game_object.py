import math
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BULLET_SPEED = 5


class Player(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)
        self.speed = 0
        self.lives = 3


    def update(self):
        self.angle += self.change_angle
        angle_rad = math.radians(self.angle)
        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)


class Bullet(arcade.Sprite):
    def __init__(self, image, scale, angle, center_x, center_y, s_width, s_height):
        super().__init__(image, scale, angle=angle, center_x=center_x, center_y=center_y)
        # self.velocity = velocity
        self.s_width = s_width
        self.s_height = s_height

    def update(self):
        if self.top > self.s_height or self.bottom < 0 or self.right > self.s_width or self.left < 0:
            self.remove_from_sprite_lists()


class Enemy(arcade.Sprite):
    def __init__(self, image, scale, x, y, angle):
        super().__init__(image, scale, center_x=x, center_y=y, angle=angle)
        self.center_x = x
        self.center_y = y
        self.angle = angle


    
