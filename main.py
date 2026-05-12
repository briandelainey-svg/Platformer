import pygame, sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Platformer')
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0))
        self.img_pos = [160, 260]
        self.movey = [False, False]
        
        self.collison_area = pygame.Rect(50, 50, 300, 50)
    
    
    def refresh(self):
        pygame.display.update()
        self.clock.tick(60)
        self.screen.fill((14, 219, 248))
        
    def objects(self):
        img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
        if img_r.colliderect(self.collison_area):
            pygame.draw.rect(self.screen, (0, 100, 255), self.collison_area)
        else:
            pygame.draw.rect(self.screen, (0, 50, 155), self.collison_area)
        self.img_pos[1] += (self.movey[1] - self.movey[0]) * 5
        self.screen.blit(self.img, (self.img_pos))
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movey[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movey[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movey[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movey[1] = False
                        
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
            
            self.refresh()
            self.objects()
if __name__ == '__main__':
    Game().run()