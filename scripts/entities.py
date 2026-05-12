import pygame

#Variables
vel = [0, 0]


class PhysicsEntity:
    def __init__(self, Game, e_type, pos, size, vel):
        self.Game = Game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.vel = vel
    def update(self, move=(0, 0)):
        frame_move = (move[0] + self.vel[0] move[1] + self.vel[1])