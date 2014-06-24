from .sprite import *
from .map import *
from .bullet import *


class Tank(Sprite):
    """Sprite for enemy tanks and base class for Player"""
    is_enemy = True

    def __init__(self, position, direction, lives):
        sprite_cache = TileCache("tanks.png")
        self.frames = sprite_cache["tanks.png"]
        Sprite.__init__(self, position)
        self.direction = direction
        self.lives = lives
        self.position = position
        self.image = self.frames[DIRECTIONS.index(self.direction)][0]

    def update(self, *args):
        self.image = self.frames[DIRECTIONS.index(self.direction)][0]

    def next_position(self):
        x, y = self.position
        direction = DIRECTIONS.index(self.direction)
        next_x = x + DX[direction]
        next_y = y + DY[direction]
        return (next_x, next_y)

    def shoot(self):
        (next_x, next_y) = self.next_position()
        bullet = Bullet((next_x, next_y), self.direction)
        return bullet

class Player(Tank):
    """Display the player"""
    is_player = True

    def __init__(self, position, direction, lives):
        Tank.__init__(self, position, direction, lives)
        sprite_cache = TileCache("player.png")
        self.frames = sprite_cache["player.png"]

