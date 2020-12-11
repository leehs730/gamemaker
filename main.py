import pygame as pg
import sys
from os import path
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # repeat으로 간격 설정
        pg.key.set_repeat(150, 100)
        self.load_data()    # 함수 load_data를 불러옴(함수 순서는 상관이 없는가?)

    def load_data(self):
        game_folder = path.dirname(__file__)    # 파일의 경로를 변수에 저장
        self.map_data = []      # map_data 리스트 생성
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:    # 텍스트 파일 텍스트 모드로 읽기오며 열기
            for line in f:      # 반복문
                self.map_data.append(line)

    def new(self):
        # initialize all variables and do all the setup for a new game / 모든 변수를 초기화하고 새 게임을 위한 모든 설정을 수행
        self.all_sprites = pg.sprite.Group()    # sprite 모듈(pygame 내장) 사용
        self.walls = pg.sprite.Group()
        self.blocks = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):    # enumerate-반복문 사용시 몇번이 사용되었는지 확인
            for col, tile in enumerate(tiles):
                if tile == '1':     # 1이면 벽
                    Wall(self, col, row)
                if tile == 'P':     # P이면 플레이어
                    self.player = Player(self, col, row)
                if tile == 'b':     # b이면 블록
                    Block(self, col, row)

    def run(self):
        # game loop - set self.playing = False to end the game / 게임 루프, self.playing 변수가 false면 게임 종료
        self.playing = True
        while self.playing:     # True 이기에 계속 돌리게됨
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):     # 게임 종료
        pg.quit()
        sys.exit()

    def update(self):   # 게임 업데이트
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):        # 격자무늬 그리기기
       for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
       for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):     #그리기
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):       # 이벤트 방향키 메커니즘 함수
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def show_start_screen(self):        # 시작 화면을 보여주는 함수
        pass

    def show_go_screen(self):       # 다음 화면으로 넘겨주는 함수
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()