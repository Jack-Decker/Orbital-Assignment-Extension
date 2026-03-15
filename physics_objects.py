import math
from pygame.math import Vector2
import pygame

class PhysicsObject:
    def __init__(self, mass = math.inf, pos = (0,0), vel = (0,0)):
        self.mass = mass
        self.set_position(pos)
        self.set_velocity(vel)
        self.acc = Vector2(0,0)
    
    def set_position(self, pos):
        self.pos = Vector2(pos)
    
    def set_velocity(self, vel):
        self.vel = Vector2(vel)

    def clear_force(self):
        self.acc *= 0

    def add_force(self, force):
        self.acc += force/self.mass
    
    def add_acc(self, acc):
        self.acc += acc

    def update(self, dt):
        # update velocity using the current force
        self.vel += self.acc*dt
        # update position using the newly updated velocity
        self.pos += self.vel*dt


class Circle(PhysicsObject):
    def __init__(self, radius = 100, color = pygame.Color("yellow"), width=0, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.color = color
        self.width = width

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.pos, self.radius, self.width)

