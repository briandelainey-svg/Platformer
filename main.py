import pygame, sys
from scripts.utils import load_img
from scripts.entities import PhysicsEntity

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320 , 240))
        pygame.display.set_caption('Platformer')
        
        self.clock = pygame.time.Clock()
        
        self.movex = [False, False]
        
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        self.assets = {
            'player': load_img('entities/player.png')
            }
        
    def refresh(self):
        pygame.display.update()
        self.clock.tick(60)
        self.display.fill((14, 219, 248))
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
    def objects(self):
        self.player.update((self.movex[1] - self.movex[0], 0))
        self.player.render(self.display)
    
    def run(self):
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movex[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movex[1] = True
                if event.type == pygame.KEYUP:
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