import pygame

class PhysicsEntity:
    def __init__(self, Game, e_type, pos, size):
        self.Game = Game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.vel = [0, 0]

    def update(self, move=(0, 0)):
        frame_move = (move[0] + self.vel[0], move[1] + self.vel[1])
        self.pos[0] += frame_move[0]
        self.pos[1] += frame_move[1]
        
    def render(self, surf):
        surf.blit(self.Game.assets['player'], self.pos)
        
        
if __name__ == '__main__':
    print(' "entities" Is the Main')