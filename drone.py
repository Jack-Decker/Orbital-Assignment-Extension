import pygame
from pygame.locals import *
from pygame.math import Vector2, Vector3
import random
import math
from physics_objects import Circle

# CONSTANTS

# INITIALIZE PYGAME
pygame.init()

# CREATE WINDOW
window = pygame.display.set_mode([1000,700])

# TIMING
clock = pygame.time.Clock()
FPS = 60
dt = 1/FPS
clock.tick()

# SETUP
# drone
drone = Circle(radius = 50, color=Color("red"), pos=(100, 100), mass=1, vel = (0, 0))
# checkpoints
checkpoints : list[Circle] = []
def spawn_checkpoints():
    global checkpoints
    checkpoints.clear()
    for i in range(5):
        checkpoints.append(Circle(radius = 100, color = pygame.Color("green"), width = 5, pos = 
        (random.uniform(100, window.get_width() - 100), random.uniform(100, window.get_height() - 100))))

spawn_checkpoints()

# GAME LOOP
state = "play"
while state != "quit":
     # DISPLAY AND TIMING
    pygame.display.update()
    clock.tick(FPS) / 1000
    
    # BACKGROUND GRAPHICS
    window.fill((0,0,0))

    # PHYSICS
    ## Clear force from all objects
    drone.clear_force()

    ## Add forces
    ### Gravity downward
    drone.add_acc((0, 200))
    
    ### Thrust force
    # force when the key is down
    key = pygame.key.get_pressed()
    if key[K_LEFT]:
        drone.add_acc((-400, 0))
    if key[K_RIGHT]:
        drone.add_acc((400, 0))
    if key[K_UP]:
        drone.add_acc((0, -300))

    ### Air resistance (if time permits)

    ## Update objects
    if state == "play":
        drone.update(dt)
    print(drone.pos)

    # GAME ELEMENTS
    ## Checkpoints
    # check if drone is inside checkpoint
    for x in checkpoints:
        if x.pos.distance_to(drone.pos) < x.radius - drone.radius:
            x.width = 0
    
    if all(x.width == 0 for x in checkpoints):
        spawn_checkpoints()
    
    # GRAPHICS
    for i in checkpoints:
        i.draw(window)
    drone.draw(window)
    for i in checkpoints:
        if x.width > 0:
            x.draw(window)

    # EVENTS
    while event := pygame.event.poll():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            state = "quit"
        elif event.type == KEYDOWN and state == "ready":
            state = "play"
        # add more events, such as for pause or restarting from game over
        