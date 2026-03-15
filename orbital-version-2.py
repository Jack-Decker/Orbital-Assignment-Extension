import pygame
from pygame.locals import *
from pygame.math import Vector2
import random
import math
from physics_objects import Circle

# INITIALIZE PYGAME
pygame.init()

# CREATE WINDOW
screen_width, screen_height = pygame.display.get_desktop_sizes()[0]
SIZE = 0.7*min(screen_height, screen_width)
window = pygame.display.set_mode(flags=RESIZABLE)
center = Vector2(window.get_width(), window.get_height()) / 2
screen_center = (screen_width/2, screen_height/2)

# CONSTANTS
# G is the gravitational constant
G = (SIZE**3)/15

# FONT
pygame.font.init()

# TIMING
clock = pygame.time.Clock()
FPS = 60
dt = 1/FPS
clock.tick()
playing = True
clearing = False

# SETUP
# Sun
sun = Circle(radius = SIZE/10, color = pygame.Color("yellow"),
width = 0, pos = (center.x - 250, center.y), mass = 1)
sun2 = Circle(radius = SIZE/10, color = pygame.Color("yellow"),
width = 0, pos = (center.x + 250, center.y), mass = 1)
centerG = Circle(radius = SIZE/30, color = pygame.Color("darkgrey"),
width = 0, pos = center, mass = 1)

# Ship
ship = Circle(radius = SIZE/30, color = pygame.Color("skyblue"), width = 0, mass = 1)
shipThrust = Circle(radius = SIZE/45, color = pygame.Color("yellow"), width = 0, pos = ship.pos)

# Dots
# Dots array
if playing:
    dots = [
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    ]
else:
    dots = []
if playing:
    dots2 = [
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1),
    ]
else:
    dots2 = []
#An array for storing the radius of each dots orbit from the sun
# An array for storing the radius of each dots orbit from the sun
dotRanges = []
radii_allowed_area = (window.get_width() * 1/4) - sun.radius
j = 1
for dot in dots:
    orbital_radius = radii_allowed_area * j/len(dots) + sun.radius + 10
    dotRanges.append(orbital_radius)
    j += 1

dotRanges2 = []
radii_allowed_area = (window.get_width() * 1/4) - sun2.radius
j = 1
for dot in dots2:
    orbital_radius = radii_allowed_area * j/len(dots2) + sun2.radius + 10
    dotRanges2.append(orbital_radius)
    j += 1

# function for randomizing initial positions
def randomize_dots():
    i = 0
    j = 0
    if dots:
        for dot in dots:
            # Choose a random angle theta
            theta = random.uniform(0, math.pi * 2)
            # x = sun.pos.x + radius * cos(theta)
            dot.pos.x = sun.pos.x + dotRanges[i] * math.cos(theta)
            # y = sun.pos.y + radius * sin(theta)
            dot.pos.y = sun.pos.y + dotRanges[i] * math.sin(theta)
            i += 1
    if dots2:
        for dot in dots2:
            # Choose a random angle theta
            theta = random.uniform(0, math.pi * 2)
            # x = sun.pos.x + radius * cos(theta)
            dot.pos.x = sun2.pos.x + dotRanges2[j] * math.cos(theta)
            # y = sun.pos.y + radius * sin(theta)
            dot.pos.y = sun2.pos.y + dotRanges2[j] * math.sin(theta)
            j += 1

# Function for getting initial velocities (in = initial)
def initial_vels():
    # SHIP
    #ship.vel.x = math.sqrt(2 * G * sun.mass / sun.pos.distance_to(ship.pos))
    ship.vel = (160, 200)

    # DOTS
    if dots:
        for dot in dots:
            in_dot_speed = math.sqrt(G/sun.pos.distance_to(dot.pos))
            in_dot_dir = (dot.pos - sun.pos).normalize().rotate(90)
            dot.vel = in_dot_speed * in_dot_dir
    if dots2:
        for dot in dots2:
            in_dot_speed2 = math.sqrt(G/sun2.pos.distance_to(dot.pos))
            in_dot_dir2 = (dot.pos - sun2.pos).normalize().rotate(90)
            dot.vel = -1 * (in_dot_speed2 * in_dot_dir2)

def start_game():
    ship.clear_force()
    ship.set_velocity(0)
    ship.pos = ((window.get_width()/2), window.get_height()/2)
    global state, alive, win, dot, dots, start_time, seconds, minutes, active, pause_seconds, time_when_paused
    alive = True
    win = False
    active = True
    if dots:
        if len(dots) < len(dotRanges):
            for j in range(len(dotRanges) - len(dots)):
                dots.append(Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1))
                j += 1
        randomize_dots()
    if dots2:
        if len(dots2) < len(dotRanges2):
            for k in range(len(dotRanges2) - len(dots2)):
                dots2.append(Circle(radius = SIZE/60, color = pygame.Color("white"), width = 0, mass = 1))
                k += 1
        randomize_dots()
    initial_vels()
    start_time = pygame.time.get_ticks() - game_loop_start_time
    seconds = 0
    minutes = 0
    state = "play"
    pause_seconds = 0
    time_when_paused = 0

def pause_game():
    global active, time_when_paused, seconds, pause_seconds
    # PAUSE GAME
    if active: 
        active = False
        text = pygame.font.SysFont("arial", 150).render("PAUSED", True, Color("white"))
        window.blit(text, (center.x - text.get_width()/2, center.y - text.get_height()/2))
        pygame.display.update()
        time_when_paused = (pygame.time.get_ticks() - game_loop_start_time)
    # RESUME GAME
    elif not active:
        active = True
        # The pause seconds variable accounts for the CUMULATIVE TIME that the game has been paused.
        # This is cumulative because the game runs on the programs total runtime,
        # so it needs to account for every time the game is paused.
        pause_seconds += (pygame.time.get_ticks() - game_loop_start_time) - time_when_paused
        time_when_paused = 0
        

# GAME LOOP
if dots:
    playing = True
    clearing = True
game_loop_start_time = pygame.time.get_ticks()
start_game()
while state != "quit":
    if active == True:
        # DISPLAY AND TIMING
        pygame.display.update()
        clock.tick(FPS) / 1000
        
        # BACKGROUND GRAPHICS
        if clearing:
            window.fill((0,0,0))

        if alive:
            seconds = (((pygame.time.get_ticks() - game_loop_start_time) - start_time) - pause_seconds) / 1000
            if seconds/60 > 1:
                minutes = int(seconds/60)
                seconds -= minutes * 60
            seconds = round(seconds, 3)
        if clearing:
            time_text = pygame.font.SysFont("arial", 50).render(f"{minutes}:{seconds}", True, Color("white"))
            window.blit(time_text, (0, 0))
        elif not clearing and (state == "win" or state == "lose"):
            time_text = pygame.font.SysFont("arial", 50).render(f"{minutes}:{seconds}", True, Color("white"))
            window.blit(time_text, (0, 0))

        # PHYSICS
        ## Clear force from all objects
        ship.clear_force()
        for dot in dots:
            dot.clear_force()
        for dot in dots2:
            dot.clear_force()

        ## Add forces
        ### Gravitational force toward sun
        # r is the vector from the sun to the ship
        r, r2 = (ship.pos - sun.pos), (ship.pos - sun2.pos)
        m, m2 = r.magnitude(), r2.magnitude()
        if r != [0, 0] and r2 != [0, 0]:
            gravForce = (-1 * G * (sun.mass/m**3)* r) - (G * (sun2.mass/m2**3)* r2)
            ship.add_acc(gravForce)
        
        for dot in dots:
            dot_r = dot.pos - sun.pos
            if dot_r != 0:
                dot_gravForce = (-1 * G * (sun.mass/dot_r.magnitude()**3) * dot_r)
                dot.add_acc(dot_gravForce)
        for dot in dots2:
            dot_r2 = dot.pos - sun2.pos
            if dot_r2 != 0:
                dot_gravForce2 = (-1 * G * (sun.mass/dot_r2.magnitude()**3) * dot_r2)
                dot.add_acc(dot_gravForce2)

        ### Thrust force
        thrust = Vector2()
        key = pygame.key.get_pressed()
        if key[K_LEFT]:
            thrust.x = -1
        if key[K_RIGHT]:
            thrust.x = 1
        if key[K_UP]:
            thrust.y = -1
        if key[K_DOWN]:
            thrust.y = 1
        if thrust != Vector2(0, 0):
            thrust.normalize()
            thrust.scale_to_length(SIZE/5)
        ship.add_acc(thrust)

        ## Update objects
        if alive:
            ship.update(dt)
            shipThrust.pos = Vector2(thrust * -1/7) + ship.pos
            shipThrust.update(dt)
        for dot in dots:
            dot.update(dt)
        for dot in dots2:
            dot.update(dt)
        # GAME ELEMENTS
        ## Dot collection
        if alive:
            for dot in dots:
                if ship.pos.distance_to(dot.pos) < (ship.radius + dot.radius):
                    dots.remove(dot)
            for dot in dots2:
                if ship.pos.distance_to(dot.pos) < (ship.radius + dot.radius):
                    dots2.remove(dot)

        # Draw the sun
        sun.draw(window)
        sun2.draw(window)

        ## Winning
        if not dots and not dots2 and playing:
            # show "You Won!" on screen
            state = "win"
            text = pygame.font.SysFont("arial", 150).render("You Won!", True, Color("green"))
            window.blit(text, (center.x - text.get_width()/2, center.y - text.get_height()/2))
            win = True

        ## Losing
        if ((ship.pos.distance_to(sun.pos) < (ship.radius + sun.radius) and win == False) or 
        (ship.pos.distance_to(sun2.pos) < (ship.radius + sun2.radius)) and win == False):
            state = "lose"
            #delete the ship
            alive = False
            # show "You Lost!" on screen
            text = pygame.font.SysFont("arial", 150).render("You Lost!", True, Color("red"))
            window.blit(text, (center.x - text.get_width()/2, center.y  -text.get_height()/2))

        # GRAPHICS
        # Draw the ship elements
        if alive:
            if thrust.x or thrust.y != 0:
                shipThrust.draw(window)
            ship.draw(window)
            #Adds lines to go from the screen center to the ship when it's off screen
            if (ship.pos.x < 0 or ship.pos.x > window.get_width() or ship.pos.y < 0 
            or ship.pos.y > window.get_height()):
                pygame.draw.line(surface = window, color = pygame.Color("red"), 
                start_pos = sun.pos, end_pos = ship.pos)
                #.rotate_rad(-1 * math.asin(ship.radius/((ship.pos - center).magnitude()))))
                #pygame.draw.line(surface = window, color = pygame.Color("green"), 
                #start_pos = sun.pos, end_pos = ship.pos.rotate_rad(math.asin(ship.radius/(ship.pos - center).magnitude())))

        # Draw the dots
        for dot in dots:
            dot.draw(window)
        for dot in dots2:
            dot.draw(window)
        # EVENTS
        while event := pygame.event.poll():
            if event.type == KEYDOWN and event.key == K_BACKSPACE:
                if clearing == True:
                    clearing = False
                elif clearing == False:
                    clearing = True
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                state = "quit"
            # add more events, such as for pause or restarting from game over
            if event.type == KEYDOWN and event.key == K_SPACE and (state == "win" or state == "lose"):
                start_game()
                window.fill((0,0,0))
            elif event.type == KEYDOWN and event.key == K_SPACE and (state != "win" and state != "lose"):
                pause_game()
                window.fill((0,0,0))
        
        if not pygame.mouse.get_focused() and not pygame.key.get_focused():
            pause_game()
    while event := pygame.event.poll():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                state = "quit"
        if event.type == KEYDOWN and event.key == K_SPACE:
            pause_game()