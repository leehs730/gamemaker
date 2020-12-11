import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.image = pg.image.load("player.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

# 1
    def move(self, dx=0, dy=0): # 플레이어 이동 설정
        if not self.collide_with_block(dx, dy) and not self.collide_with_walls(dx, dy) and not self.collide_blocks_and_walls(dx, dy):
            self.x += dx
            self.y += dy

# 3
    def collide_with_walls(self, dx=0, dy=0): # player와 wall 충돌 설정
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy: # player의 앞에 wall이 존재한다면 True 리턴
                return True
        return False

# 2
    def collide_with_block(self, dx=0, dy=0): # player와 block의 충돌 설정
        if not self.collide_blocks_and_walls(dx, dy):
            for block in self.game.blocks:
                if block.x == self.x + dx and block.y == self.y + dy: # player의 앞에 block이 존재한다면 True 리턴
                    # player와 block의 위치를 한 칸씩 밀어냄
                    self.x += dx
                    self.y += dy
                    block.x += dx
                    block.y += dy
                    return True
        elif self.collide_blocks_and_walls(dx, dy):
            return True
        return False

# 5
    def collide_blocks_and_walls(self, dx=0, dy=0):  # block과 wall의 충돌 설정
        for block in self.game.blocks:
            for wall in self.game.walls:
                if wall.x == self.x + (dx * 2) and wall.y == self.y + (dy * 2):  # 플레이어 앞의 두칸정도에 wall이 있고 바로 앞에 block이 있다면 Ture 리컨
                    if block.x == self.x + dx and block.y == self.y + dy:
                        return True
        return False

# 4
    def collide_blocks_and_blocks(self, dx=0, dy=0):  # block과 block의 충돌 설정
        for block in self.game.blocks:
            if block.x == block.x + dx and block.y == block.y + dy:  # blocks의 앞에 blocks가 존재한다면 True 리턴
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class Block(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.blocks
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.image = pg.image.load("block.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def block_chained(self, dx=0, dy=0):
        for block in self.game.blocks:
            block.x = self.x
            block.y = self.y
            if block.x + dx == block.x:
                block.x += dx
            elif block.y + dy == block.y:
                block.y += dy
            else:
                pass


    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.image = pg.image.load("wall.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE