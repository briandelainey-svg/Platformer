class  Tilemap:
    def __init__(self, Game, tile_size=16):
        self.Game = Game
        self.tile_size = tile_size
        self.tile_map = {}
        self.offgrid_tiles = []
        for i in range(10):
            self.tile_map[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)} 
            self.tile_map['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)} 

    def render(self, surf):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])
            
        for loc in self.tile_map:
            tile = self.tile_map[loc]
            surf.blit(self.Game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))


if __name__ == '__main__':
    print('tilemap Is the Main')