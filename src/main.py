import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from earth_renderer import render_earth
from sphere import create_sphere

def init_window():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Visualizador da Terra')
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glTranslatef(0.0, 0.0, -5)

def main():
    init_window()
    sphere_data = create_sphere()
    texture_id = render_earth.load_texture("textures/Earth_Diffuse.jpg")


    clock = pygame.time.Clock()
    rot = 0
    running = True

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(rot, 0, 1, 0)
        render_earth.draw_textured_sphere(sphere_data, texture_id)
        glPopMatrix()

        rot += 0.2
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
