import pygame, sys
from scripts.utils import load_img, load_imgs
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320 , 240))
        pygame.display.set_caption('Platformer')
        
        self.clock = pygame.time.Clock()
        
        self.movex = [False, False]
        self.movey = [False, False]
        
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        self.tilemap = Tilemap(self, Game,)
        self.assets = {
            'decor': load_imgs('tiles/decor'),
            'grass': load_imgs('tiles/grass'),
            'large_decor': load_imgs('tiles/large_decor'),
            'stone': load_imgs('tiles/stone'),
            'player': load_img('entities/player.png')
            }
        
    def refresh(self):
        pygame.display.update()
        self.clock.tick(60)
        self.display.fill((14, 219, 248))
        self.tilemap.render(self.display)
    def objects(self):
        self.player.update((self.movex[1] - self.movex[0], 0))
        self.player.update((self.movey[1] - self.movey[0], 0))
        self.player.render(self.display)
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

    
    def run(self):
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.movey[0] = True 
                    if event.key == pygame.K_LEFT:
                        self.movex[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movex[1] = True
                if event.type == pygame.KEYUP:
                    if event.type == pygame.K_SPACE:
                        self.movey[0] = False 
                    if event.key == pygame.K_LEFT:
                        self.movex[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movex[1] = False
                        
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
            
            self.refresh()
            self.objects()
if __name__ == '__main__':
    Game().run()