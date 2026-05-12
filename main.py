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
        self.movex = [False, False]
        
        
    def refresh(self):
        pygame.display.update()
        self.clock.tick(60)
        self.screen.fill((14, 219, 248))
        self.screen.blit(self.img, (self.img_pos))
        
        
    def run(self):
        while True:
            #self.pygame.draw.rect(screen, (0, 0, 0), (320, 480))
            if self.img_pos[1] <= 430:
                self.img_pos[1] += 5
            elif self.img_pos[1] >= 430:
                self.img_pos[1] == 430
            self.img_pos[1] += (self.movey[1] - self.movey[0]) * 10
            self.img_pos[0] += (self.movex[1] - self.movex[0]) * 10
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movey[0] = True
                    if event.key == pygame.K_DOWN:
                        if self.img_pos[1] >= 430:
                            print('nope')
                        else:
                            self.movey[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movey[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movey[1] = False
                        
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

Game().run()