from OpenGL.GL import *
import pygame

class render_earth:
    @staticmethod
    def load_texture(path):
        texture_surface = pygame.image.load(path)
        texture_data = pygame.image.tostring(texture_surface, 'RGB', 1)
        width, height = texture_surface.get_rect().size

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        return texture_id

    @staticmethod
    def draw_textured_sphere(sphere_data, texture_id):
        vertices, texcoords, indices = sphere_data
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glBegin(GL_TRIANGLES)
        for idx in indices:
            glTexCoord2fv(texcoords[idx])
            glVertex3fv(vertices[idx])
        glEnd()
