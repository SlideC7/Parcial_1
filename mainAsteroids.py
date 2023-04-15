import math
import random

import arcade
from game_object import Player

# definicion de constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Asteroids"
SCALING = 0.5
SPEED = 5
BULLET_SPEED = 15


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.sprites = arcade.SpriteList()
        self.player = Player("img/spaceRocket.png", SCALING, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.sprites.append(self.player)
        self.bullets = arcade.SpriteList()
        self.enemies = arcade.SpriteList()
        self.score = 0
        self.attempts = 3    
        self.enemy_cooldown = 0    
        self.enemy_bullet_list = arcade.SpriteList()
        arcade.schedule(self.add_enemy, 0.5)

    def on_key_press(self, symbol: int, modifiers: int):
        """Metodo para detectar teclas que han sido presionada
        El punto se movera con las teclas de direccion.
        Argumentos:
            symbol: tecla presionada
            modifiers: modificadores presionados
        """
        if symbol == arcade.key.UP:
            self.player.speed = SPEED
        if symbol == arcade.key.DOWN:
            self.player.speed = -SPEED

        if symbol == arcade.key.LEFT:
            self.player.change_angle = 5
        if symbol == arcade.key.RIGHT:
            self.player.change_angle = -5

        if symbol == arcade.key.SPACE:
            bullet = arcade.Sprite(
                "img/star.png",
                0.1,
                angle=self.player.angle + 90,
                center_x=self.player.center_x,
                center_y=self.player.center_y,
            )
            bullet.velocity = (
                BULLET_SPEED * math.cos(math.radians(self.player.angle + 90)),
                BULLET_SPEED * math.sin(math.radians(self.player.angle + 90))
            )
            self.bullets.append(bullet)
            self.sprites.append(bullet)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP, arcade.key.DOWN):
            self.player.speed = 0
        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_angle = 0

    def on_update(self, delta_time: float):
        """Metodo para actualizar objetos de la app"""
        self.update_bullets()
        self.update_enemies()
        self.update_enemies_attack()  # Agregar esta línea
        self.sprites.update()

    def on_draw(self):
        """Metodo para dibujar en la pantalla"""
        arcade.start_render()
        self.sprites.draw()
        arcade.draw_text(
            f"Score: {self.score}",
            700,
            35,
            arcade.color.YELLOW,
            15,
            width=SCREEN_WIDTH,
            align="left"
        )

    def update_bullets(self):
        for b in self.bullets:
            if b.top > SCREEN_HEIGHT or b.bottom < 0 or b.left < 0 or b.right > SCREEN_WIDTH:
                b.remove_from_sprite_lists()

    def update_enemies(self):
        for e in self.enemies:
            if e.collides_with_list(self.bullets):
                e.remove_from_sprite_lists()
                self.score += 1

    def update_enemies_attack(self):
        for e in self.enemies:
            e.center_x += math.cos(math.radians(e.angle + 90)) * 4
            e.center_y += math.sin(math.radians(e.angle + 90)) * 4
            
        for e in self.enemy_bullet_list:
            if e.collides_with_sprite(self.player):
                self.attempts -= 1
                if self.attempts == 0:
                    arcade.draw_text(
                        "Game Over",
                        SCREEN_WIDTH / 2,
                        SCREEN_HEIGHT / 2,
                        arcade.color.WHITE,
                        font_size=50,
                        anchor_x="center",
                    )
                    arcade.draw_text(
                        f"Puntuación: {self.score}",
                        SCREEN_WIDTH / 2,
                        SCREEN_HEIGHT / 2 - 50,
                        arcade.color.WHITE,
                        font_size=30,
                        anchor_x="center",
                    )
                    arcade.finish_render()  # se muestra el resultado en la ventana
                    arcade.pause(3) 
                    arcade.close_window()
                self.player.center_x = SCREEN_WIDTH / 2
                self.player.center_y = SCREEN_HEIGHT / 2
                self.player.angle = 0
                e.remove_from_sprite_lists()


    def add_enemy(self, delta_time: float):
        if self.enemy_cooldown > 0:
            self.enemy_cooldown -= delta_time
            return

        # crea una nave enemiga
        enemy = arcade.Sprite("img/alienShip.png", SCALING)
        enemy.left = random.randint(10, SCREEN_WIDTH - 10)
        enemy.top = SCREEN_HEIGHT - 10
        enemy.angle = 180  # mirando hacia abajo
        self.enemies.append(enemy)
        self.sprites.append(enemy)

        # crea una bala enemiga
        bullet = arcade.Sprite("img/star.png", 0.2)
        bullet.center_x = enemy.center_x
        bullet.bottom = enemy.bottom - 5
        bullet.change_y = -10  # movimiento hacia abajo
        self.enemy_bullet_list.append(bullet)
        self.sprites.append(bullet)

        self.enemy_cooldown = 1.0




        enemy = arcade.Sprite("img/asteroid50.png", SCALING)
        enemy.left = random.randint(10, SCREEN_WIDTH - 10)
        enemy.top = random.randint(10, SCREEN_HEIGHT - 10)
        self.enemies.append(enemy)
        self.sprites.append(enemy)
        self.enemy_cooldown = 0.5
        dx = self.player.center_x - enemy.center_x
        dy = self.player.center_y - enemy.center_y
        enemy.angle = math.degrees(math.atan2(dy, dx))

    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()
        # aquí se muestra el número de intentos restantes
        arcade.draw_text(
            f"Intentos: {self.attempts}",
            50,
            35,
            arcade.color.WHITE,
            15,
            width=SCREEN_WIDTH,
            align="left"
        )

if __name__ == "__main__":
    app = App()
    arcade.run()
