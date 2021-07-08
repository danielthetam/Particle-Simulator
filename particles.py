import pygame, os, sys, random
from pygame import math

"""
PROJECT DETAILS
Particle Simulator

Created by Daniel Tam
7/8/2021, 5:41 PM

DESCRIPTION
A particle simulator made to test out a particle mechanic for my first offical game, Toast My Bread.

USES
You may use this to draw sketches made of particles. Or just enjoy the simulation.
You may also fork this to modify the code anyway you want in order to create
a satisfying rain simulator 
"""


# Centering Screen
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

clock = pygame.time.Clock()

# Creating Window
WINDOW_SIZE = (800, 800)
display = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Particle Simulator")
pygame.display.set_icon(pygame.image.load('particleSimulatorIcon.png'))


# Particles
PARTICLE_SIZE = math.Vector2(5, 5)
PARTICLE_GRAVITY_RANGE = (0, 5)
particles = []


while True:


    # Fill Background
    display.fill((69, 76, 115))


    # Input Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_q:
                particles.clear()
        elif pygame.mouse.get_pressed()[0]:
            particles.append(pygame.Rect(pygame.mouse.get_pos(), PARTICLE_SIZE))
            for i in range(3):
                particles.append(pygame.Rect(math.Vector2(pygame.mouse.get_pos()[0] + 5, pygame.mouse.get_pos()[1]), math.Vector2(PARTICLE_SIZE.elementwise() + random.randint(-1, 1))))
   
    # Rendering

    # Rendering Particles
    for particle in particles:
        # Randomizing Particle Velocity
        particle_velocity = math.Vector2(random.randint(-1, 1)/2, random.randint(PARTICLE_GRAVITY_RANGE[0], PARTICLE_GRAVITY_RANGE[1]))

        # Particle Movement
        particle[0] += particle_velocity.x
        particle[1] += particle_velocity.y

        pygame.draw.rect(display, (147, 118, 166), particle)
        
        # Removing Particles
        if particle[1] < 0 or particle[1] > WINDOW_SIZE[1]:
            particles.remove(particle)
  

    print(len(particles))
    print(clock.get_fps())
    clock.tick(60)
    pygame.display.update()
