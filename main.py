import pygame, sys, time, math, random, array
import moderngl as mgl

pygame.mixer.init()

WIDTH, HEIGHT = 640, 480
width, height = 320, 240
TILE_SIZE = 8
OFFSETS = [(-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1), (-1, -1), (0, -1), (1, -1)]
AUTO_TILE_MAP = {'0011': 1, '1011': 2, '1001': 3, '0001': 4, '0111': 5, '1111': 6, '1101': 7, '0101': 8, 
                '0110': 9, '1110': 10, '1100': 11, '0100': 12, '0010': 13, '1010': 14, '1000': 15, '0000': 16}
AUTO_TILE_TYPES = {1}

levels = [
    [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
        [1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    [
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2, 2, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
]

class Portal:
    def __init__(self, pos, app):
        self.pos = pos
        self.anim = self.load_anim(app.assets['portal'])
        self.frame = 0
        self.started = False
        self.step = 0
        self.finished = False

    def reset(self):
        self.frame = 0
        self.started = False
        self.step = 0
        self.finished = False

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], 8, 8)
    
    def load_anim(self, tex):
        anim = []
        for i in range(8):
            tile = pygame.Surface((8, 8))
            tile.blit(tex, (-8 * i, 0))
            tile.set_colorkey((0, 0, 0))
            anim.append(tile.copy())
        return anim
    
    def draw(self, screen, scroll = [0, 0]):
        if self.started:
            self.frame += 0.1
            self.step = min(int(self.frame), 7)
            if self.frame > 7:
                self.finished = True
        image = self.anim[self.step]
        screen.blit(image, (self.pos[0] - scroll[0], self.pos[1] - scroll[1]))

class Level:
    def __init__(self, app):
        self.portal = Portal([0, 0], app)
        self.level = 0
        self.tiles = self.load_level(self.level)
        self.autotile()
        self.tile_set = self.load_tileset(app.assets['tiles'])
        self.spike = app.assets['spike']
    
    def load_tileset(self, tileset):
        tiles = []
        for y in range(4):
            for x in range(4):
                tile = pygame.Surface((8, 8))
                tile.blit(tileset, (-x * TILE_SIZE, -y * TILE_SIZE))
                tile.set_colorkey((0, 0, 0))
                tiles.append(tile.copy())
        return tiles

    def next_level(self):
        self.level += 1
        self.tiles = self.load_level(self.level)
        self.autotile()
    
    def load_level(self, l):
        tiles = levels[l]
        level = {}
        for y, row in enumerate(tiles):
            for x, tile in enumerate(row):
                if tile:
                    if tile == 3:
                        self.portal.pos = [x * TILE_SIZE, y * TILE_SIZE]
                    level[f'{x};{y}'] = {'type': tile, 'variant': 0, 'pos': [x * TILE_SIZE, y * TILE_SIZE]}
                    
        return level
    
    def autotile(self):
        for loc in self.tiles:
            print(loc)
        for loc in self.tiles:
            tile = self.tiles[loc]
            aloc = ''
            for shift in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                check_loc = str(math.floor(tile['pos'][0] / TILE_SIZE) + shift[0]) + ';' + str(math.floor(tile['pos'][1] / TILE_SIZE) + shift[1])
                print(check_loc)
                if check_loc in self.tiles:
                    if self.tiles[check_loc]['type'] == tile['type']:
                        aloc += '1'
                    else:
                        aloc += '0'
                    print('yo')
                else:
                    aloc += '0'
            if tile['type'] in AUTO_TILE_TYPES:
                tile['variant'] = AUTO_TILE_MAP[aloc] - 1
                print(tile['variant'])

    def collidepos(self, pos):
        loc = f'{math.floor(pos[0] / TILE_SIZE)};{math.floor(pos[1] / TILE_SIZE)}'
        if loc in self.tiles:
            if self.tiles[loc]['type'] == 1:
                return True
        return False
    
    def get_tiles_around_pos(self, pos):
        tiles = []
        tpos = [math.floor(pos[0] / TILE_SIZE), math.floor(pos[1] / TILE_SIZE)]
        for offset in OFFSETS:
            t = f'{tpos[0] + offset[0]};{tpos[1] + offset[1]}'
            if t in self.tiles:
                if self.tiles[t]['type'] == 1:
                    tiles.append(pygame.Rect((tpos[0] + offset[0]) * TILE_SIZE, (tpos[1] + offset[1]) * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        return tiles
    
    def get_spikes(self, pos):
        tiles = []
        tpos = [math.floor(pos[0] / TILE_SIZE), math.floor(pos[1] / TILE_SIZE)]
        for offset in OFFSETS:
            t = f'{tpos[0] + offset[0]};{tpos[1] + offset[1]}'
            if t in self.tiles:
                if self.tiles[t]['type'] == 2:
                    tiles.append(pygame.Rect((tpos[0] + offset[0]) * TILE_SIZE, (tpos[1] + offset[1]) * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        return tiles

    def draw(self, screen, scroll = [0, 0]):
        for x in range(math.floor(scroll[0] / TILE_SIZE), math.floor((scroll[0] + screen.get_width()) / TILE_SIZE + 1)):
            for y in range(math.floor(scroll[1] / TILE_SIZE), math.floor((scroll[1] + screen.get_height()) / TILE_SIZE + 1)):
                loc = f'{x};{y}'
                if loc in self.tiles:
                    ty = self.tiles[loc]['type']
                    if ty == 1:
                        screen.blit(self.tile_set[self.tiles[loc]['variant']], (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                    elif ty == 2:
                        screen.blit(self.spike, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                    elif ty == 3:
                        self.portal.draw(screen, scroll)
                    #pygame.draw.rect(screen, (0, 0, 255), (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1], TILE_SIZE, TILE_SIZE))

class Player:
    def __init__(self, pos, dimensions, app):
        """
        pos: [x, y]
        dimensions: [x, y]
        vel: [x, y]
        friction: friction_x
        """
        self.frame = 0
        self.step = 0
        self.frame_speed = 0.1
        self.pos = pos
        self.dimensions = dimensions
        self.vel = [0, 0]
        self.gravity = 0.3
        self.friction = 0.8
        self.falling = 99
        self.jumping = 99

        self.flipped = False

        self.ad = 121
        self.spawn_pos = pos
        self.should_die = False
        self.spawn_ghost = False

        self.anim = self.load_anim(app.assets['player'])
        self.controls = {'up': False, 'down': False, 'left': False, 'right': False}

    def load_anim(self, a):
        anim = []
        for x in range(4):
            tile = pygame.Surface(self.dimensions)
            tile.blit(a, (-self.dimensions[0] * x, 0))
            tile.set_colorkey((0, 0, 0))
            anim.append(tile.copy())
        return anim

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[1])
    
    def update(self, dt, level, app):
        self.falling += 1 * dt
        self.jumping += 1 * dt
        if (self.controls['left']):
            self.vel[0] -= 0.6
            self.flipped = True
        if (self.controls['right']):
            self.vel[0] += 0.6
            self.flipped = False
        if (self.jumping < 20 and self.falling < 10):
            self.vel[1] = -3
            self.falling = 3
            self.jumping = 30
        self.vel[0] *= self.friction
        self.pos[0] += self.vel[0] * dt
        player_rect = self.rect()
        rects = level.get_tiles_around_pos(self.pos)
        for rect in rects:
            if rect.colliderect(player_rect):
                if self.vel[0] > 0:
                    # going right
                    player_rect.right = rect.left
                else:
                    # going left
                    player_rect.left = rect.right
                self.pos[0] = player_rect.left
        self.pos[1] += self.vel[1] * dt
        if self.vel[1] < 0:
            self.vel[1] += 0.2 * dt
        else:
            self.vel[1] += 0.25 * dt
        #self.vel[1] += self.gravity * dt
        player_rect = self.rect()
        rects = level.get_tiles_around_pos(self.pos)
        for rect in rects:
            if rect.colliderect(player_rect):
                if self.vel[1] > 0:
                    # going down
                    player_rect.bottom = rect.top
                    self.falling = 0
                else:
                    # going up
                    player_rect.top = rect.bottom
                self.vel[1] = 0
                self.pos[1] = player_rect.top
        if self.falling < 3:
            self.frame += self.frame_speed * dt
        else:
            self.frame = 0
        player_rect = self.rect()
        rects = level.get_spikes(self.pos)
        for rect in rects:
            if rect.colliderect(player_rect):
                self.should_die = True
                self.spawn_ghost = True
    
    def draw(self, screen, scroll = [0, 0]):
        self.step = int(self.frame) % 4
        image = pygame.transform.flip(self.anim[self.step], self.flipped, False)
        screen.blit(image, (self.pos[0] - scroll[0], self.pos[1] - scroll[1]))
        #pygame.draw.rect(screen, (255, 0, 0), (self.pos[0] - scroll[0], self.pos[1] - scroll[1], self.dimensions[0], self.dimensions[1]))

class Ghost:
    def __init__(self, pos, app, vel):
        self.pos = pos
        self.vel = vel
        self.offset = 0
        self.timer = 0
        self.flipped = random.choice([False, True])
        self.image = self.load_sprite(app.assets['stuff'])

    def rect(self):
        return pygame.Rect(self.pos[0] + 1, self.pos[1] + 1, 6, 7)
    
    def load_sprite(self, tex):
        t = pygame.Surface((8, 8))
        t.blit(tex, (0, 0))
        t.set_colorkey((0, 0, 0))
        return t

    def update(self, dt, player_pos, ad):
        self.timer += 1 * dt
        self.vel[0] *= 0.9
        self.vel[1] *= 0.9
        self.pos[0] += self.vel[0] * dt
        self.pos[1] += self.vel[1] * dt
        self.pos[1] += math.sin(self.timer * 0.1) * 0.5
        speed = 0.05
        if ad > 120:
            self.vel[0] = min(speed, max(-speed, (player_pos[0] - self.pos[0]) * speed))
            self.vel[1] = min(speed, max(-speed, (player_pos[1] - self.pos[1]) * speed))
        self.flipped = player_pos[0] < self.pos[0]
        self.pos[0] = max(32, self.pos[0])
    
    def draw(self, screen, scroll = [0, 0]):
        screen.blit(pygame.transform.flip(self.image, self.flipped, False), (self.pos[0] - scroll[0], self.pos[1] - scroll[1]))

class App:
    def __init__(self):
        self.render_display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
        self.display = pygame.Surface((WIDTH, HEIGHT))
        self.screen = pygame.Surface((width, height))
        self.ctx = mgl.create_context()
        self.quad_buffer = self.ctx.buffer(data=array.array('f', [
            -1.0, 1.0, 0.0, 0.0,
            1.0, 1.0, 1.0, 0.0,
            -1.0, -1.0, 0.0, 1.0,
            1.0, -1.0, 1.0, 1.0
        ]))
        self.vert_shader = '''
        #version 330 core

        in vec2 vert;
        in vec2 texcoord;
        out vec2 uvs;
        

        void main() {
            uvs = texcoord;
            gl_Position = vec4(vert.x, vert.y, 0.0, 1.0);
        }
        '''
        self.frag_shader = '''
#version 330 core
        uniform sampler2D tex;
        uniform sampler2D noise;
        uniform float time;
        uniform float fadin;

        uniform float timeScale = 0.001;
        uniform float angleConst = 1.5;
uniform float stripeImpact = 0.01;
uniform float stripeWidth = 70;
uniform float threshold = 0.23; // size of hole

        in vec2 uvs;
        out vec4 f_color;

        void main() {
            vec2 texCoords = vec2(uvs.x, uvs.y);  // can be used to warp screen
    vec2 noise_offset = vec2(texture(noise, vec2(texCoords.x, texCoords.y - time * timeScale)).r) * 0.5; 
            vec3 mult = texture(noise, uvs + (time * 0.001)).rgb;
            vec4 baseColor;
            vec2 shiftTexcoords = vec2(texCoords.x + sin(time * 0.2 * timeScale), texCoords.y * 2.0 - sin(time * 0.02 * timeScale));
            vec3 color1 = texture(noise, shiftTexcoords).rgb;
            shiftTexcoords = vec2(texCoords.x * 2.7 - sin(time * 0.05 * timeScale), texCoords.y * 1.7 - sin(time * 0.5 * timeScale)); // and here
            vec3 color2 = texture(noise, shiftTexcoords).rgb;
             shiftTexcoords = vec2(texCoords.x * 0.35 - sin(time * 0.4 * timeScale), texCoords.y * 0.35 - sin(time * 0.4 * timeScale)); // here as well
    vec3 color3 = texture(noise, shiftTexcoords).rgb;
    vec4 combinedColor = vec4(vec3((color1 + color2 * 0.5 + color3 * 0.5) * 0.5), 1.0);
    combinedColor = combinedColor * (distance(vec2(0.5, 0.5), texCoords) * 0.5 + 0.5) + sin((texCoords.x - texCoords.y * angleConst) * stripeWidth) * stripeImpact;
             if (combinedColor.r < threshold + 0.01) {
        baseColor = vec4(0.27450980392156865, 0.3568627450980392, 0.9058823529411765, 1.0);  // different colors
    } else if (combinedColor.r < threshold + 0.02) {
        baseColor = vec4(0.27450980392156865, 0.3568627450980392, 0.9058823529411765, 1.0);
    } else if (combinedColor.r < threshold + 0.05) {
        baseColor = vec4(0.13333333333333333, 0.17647058823529413, 0.5058823529411764, 1.0);
    } else if (combinedColor.r < threshold + 0.1) {
        baseColor = vec4(0.10588235294117647, 0.09411764705882353, 0.3254901960784314, 1.0);
    } else {
        baseColor = vec4(0.054901960784313725, 0.03529411764705882, 0.1843137254901961, 1.0);
    }
    
            f_color = vec4((texture(tex, uvs).rgb + baseColor.rgb * 0.4 + mult * 0.3) * (255.0 - fadin) / 255.0, 1.0);
        }
        '''
        self.program = self.ctx.program(vertex_shader=self.vert_shader, fragment_shader=self.frag_shader)  # still can't spell :)
        self.render_objects = self.ctx.vertex_array(self.program, [(self.quad_buffer, '2f 2f', 'vert', 'texcoord')])
        self.fade = self.screen.copy()
        self.fade.fill((0, 0, 0))
        self.fade.set_alpha(0)
        self.dt = 1
        self.last_time = time.time() - 1 / 60
        self.clock = pygame.time.Clock()
        self.running = True

        self.assets = {'tiles': pygame.image.load('data/images/tiles.png').convert(),
                       'spike': pygame.image.load('data/images/spike.png').convert(),
                       'player': pygame.image.load('data/images/player.png').convert(),
                       'stuff': pygame.image.load('data/images/stuff.png').convert(),
                       'portal': pygame.image.load('data/images/portal.png').convert(),
                       'you_win': pygame.image.load('data/images/you_win.png').convert(),
                       'noise': pygame.image.load('data/images/pic.png').convert(),
                       'dead': pygame.image.load('data/images/dead_logo.png').convert(),
                       'gameover': pygame.transform.scale2x(pygame.image.load('data/images/gameover.png').convert())}
        self.music = {'ghost': self.loadsound('ghost.wav'),
                      'hurt': self.loadsound('hurt.wav'),
                      'gameover': self.loadsound('gameover.wav'),
                      'jump': self.loadsound('jump.wav'),
                      'level1': self.loadsound('level1.wav'),
                      'level2': self.loadsound('level2.wav'),
                      'level3': self.loadsound('level3.wav'),
                      'menu': self.loadsound('menu.wav'),
                      'victory': self.loadsound('victory.wav'),
                      'powerup': self.loadsound('pickupCoin.wav')}
        for key in self.assets:
            self.assets[key].set_colorkey((0, 0, 0))

        self.level = Level(self)
        self.player = Player([20, 50], [4, 8], self)
        self.dust = []
        self.scroll = [0, 0]
        self.ghosts = []
        self.fadin = 0
        self.finished = False
        self.timer = 0
        self.screen_shake = 0
        self.menu = True
        self.music['menu'].play(-1)
        self.lives = 1

    def loadsound(self, path):
        return pygame.mixer.Sound('data/audio/' + path)
    
    def surf_to_texture(self, surf):
        tex = self.ctx.texture(surf.get_size(), 4)
        tex.filter = (mgl.NEAREST, mgl.NEAREST)
        tex.swizzle = 'BGRA'
        tex.write(surf.get_view('1'))
        return tex
    
    def next_level(self):
        self.level.next_level()
    
    def close(self):
        self.running = False
        pygame.quit()
        sys.exit()

    def kill_player(self):
        self.screen_shake = max(self.screen_shake, 16)
        self.player.ad = 0
        self.player.should_die = False
        self.player.vel = [0, 0]
        if self.player.spawn_ghost:
            print('yo')
            self.music['hurt'].play()
            self.music['ghost'].play()
            self.player.spawn_ghost = False
            for i in range(1):
                self.ghosts.append(Ghost(self.player.pos.copy(), self, [random.random() * 10 - 5, random.random() * -10 - 5]))
        else:
            self.music['hurt'].play()
            self.lives -= 1
            if self.lives < 1:
                for key in self.music:
                    self.music[key].stop()
                self.music['gameover'].play()

        for i in range(random.randint(50, 60)):
            self.dust.append([self.player.pos.copy(), [random.random() * 2 - 1, random.random() * -5], random.randint(5, 40), (255, random.randint(0, 255), random.randint(0, 255)), 50])
        for i in range(random.randint(50, 60)):
            self.dust.append([self.player.pos.copy(), [random.random() * 5 - 2.5, random.random() * 5 - 2.5], random.randint(5, 40), (255, random.randint(0, 255), random.randint(0, 255)), 50])
        self.player.pos = [20, 50]
    
    def update_particles(self, render_scroll):
        for i, particle in sorted(enumerate(self.dust), reverse=True):
            # [pos, vel, size, color]
            particle[0][0] += particle[1][0] * self.dt
            if self.level.collidepos(particle[0]):
                particle[0][0] -= particle[1][0] * self.dt
                particle[1][0] *= -0.7
                particle[1][1] *= 0.99
            particle[1][1] += 0.1 * self.dt
            particle[0][1] += particle[1][1] * self.dt
            if self.level.collidepos(particle[0]):
                particle[0][1] -= particle[1][1] * self.dt
                particle[1][1] *= -0.7
                particle[1][0] *= 0.99
            particle[2] -= 0.1
            if particle[2] < 0:
                self.dust.pop(i)
            else:
                color = pygame.Color(particle[3][0], particle[3][1], particle[3][2], particle[2] / particle[4] * 255)
                self.screen.set_at((particle[0][0] - render_scroll[0], particle[0][1] - render_scroll[1]), color)

    def update(self):
        if self.lives > 0:
            if not self.menu:
                self.timer += 1
                if self.fadin == 0:
                    if self.level.portal.rect().colliderect(self.player.rect()):
                        print('yo')
                        self.music['powerup'].play()
                        self.fadin = 1
                if self.fadin > 0:
                    print(self.fadin)
                    self.fadin += 1
                    if self.fadin == 255:
                        self.fadin = 0
                        self.kill_player()
                        self.ghosts = []
                        self.dust = []
                        self.player.ad = 121
                        if self.level.level == 0:
                            self.music['level1'].stop()
                            self.music['level2'].play(-1)
                        elif self.level.level == 1:
                            self.music['level2'].stop()
                            self.music['level3'].play(-1)
                        else:
                            self.music['level3'].stop()
                            self.music['victory'].play(-1)
                        try:
                            self.next_level()
                        except IndexError:
                            self.finished = True
                if self.player.ad > 120:
                    self.player.update(self.dt, self.level, self)
                    if self.player.should_die:
                        self.kill_player()
                    self.scroll[0] += (self.player.pos[0] - self.screen.get_width() / 2 - self.scroll[0]) / 10 * self.dt
                    self.scroll[1] = -50
                self.player.ad += 1

                #self.scroll[1] += (self.player.pos[1] - self.screen.get_height() / 2 - self.scroll[1]) / 12 * self.dt
                self.screen_shake = max(0, self.screen_shake - 1 * self.dt)

                screen_shake_offset = (random.random() * self.screen_shake - self.screen_shake / 2, random.random() * self.screen_shake - self.screen_shake / 2)
                render_scroll = (int(self.scroll[0] + screen_shake_offset[0]), int(self.scroll[1] + screen_shake_offset[1]))
                self.level.draw(self.screen, render_scroll)
                #self.dust.append([[50, 50], [random.random() * 4 - 2, -1], 50, (255, random.randint(0, 255), random.randint(0, 255)), 50])
                self.update_particles(render_scroll)
                for i, ghost in enumerate(self.ghosts):
                    ghost.update(self.dt, self.player.pos, self.player.ad)
                    ghost.draw(self.screen, render_scroll)
                    if len(self.ghosts) > 7:
                        print(ghost.timer)
                        if ghost.timer > 300:
                            self.ghosts.pop(i)
                        else:
                            if ghost.rect().colliderect(self.player.rect()):
                                self.player.should_die = True
                                self.ghosts.pop(i)
                    else:
                        if ghost.rect().colliderect(self.player.rect()):
                            self.player.should_die = True
                            self.ghosts.pop(i)

                if self.player.ad > 120:
                    self.player.draw(self.screen, render_scroll)
            else:
                self.screen.blit(self.assets['dead'], (0, 0))
        else:
            self.fadin = min(self.fadin + 1, 255)
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.assets['gameover'], (0, 0))
    
    def run(self):
        while self.running:
            self.dt = time.time() - self.last_time
            self.dt *= 60
            self.last_time = time.time()
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.close()
                    if event.key == pygame.K_LEFT:
                        self.player.controls['left'] = True
                    if event.key == pygame.K_RIGHT:
                        self.player.controls['right'] = True
                    if event.key == pygame.K_DOWN:
                        self.player.controls['down'] = True
                    if event.key == pygame.K_UP:
                        self.player.controls['up'] = True
                        self.player.jumping = 0
                        if self.menu:
                            self.menu = False
                            self.music['menu'].stop()
                            self.music['level1'].play(-1)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.close()
                    if event.key == pygame.K_LEFT:
                        self.player.controls['left'] = False
                    if event.key == pygame.K_RIGHT:
                        self.player.controls['right'] = False
                    if event.key == pygame.K_DOWN:
                        self.player.controls['down'] = False
                    if event.key == pygame.K_UP:
                        self.player.controls['up'] = False
            self.update()
            self.fade.set_alpha(self.fadin)
            self.screen.blit(self.fade, (0, 0))
            if self.finished:
                self.screen.blit(self.assets['you_win'], (0, 0))
            pygame.transform.scale_by(self.screen, 2.0, self.display)
            frame_tex = self.surf_to_texture(self.display)
            frame_tex.use(0)
            noise_tex = self.surf_to_texture(self.assets['noise'])
            noise_tex.use(1)
            self.program['tex'] = 0
            self.program['noise'] = 1
            self.program['time'] = self.timer
            self.program['fadin'] = self.fadin
            self.render_objects.render(mode=mgl.TRIANGLE_STRIP)
            frame_tex.release()
            noise_tex.release()
            if self.lives > 0:
                pygame.display.set_caption(f'FPS: {self.clock.get_fps() :.1f} LIVES: {self.lives}')
            else:
                pygame.display.set_caption(f'GAMEOVER')
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    App().run()
