# main_ar.py - Versão com AR usando OpenCV + OpenGL + marcador ArUco

import cv2
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from sphere import create_sphere
from earth_renderer import render_earth

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters()

cap = cv2.VideoCapture(0)

# Camera calibration (usar valores reais se tiver)
camera_matrix = np.array([[800, 0, 320],
                          [0, 800, 240],
                          [0,   0,   1]], dtype=np.float32)
dist_coeffs = np.zeros((4, 1))

# Inicializa janela Pygame/OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glEnable(GL_DEPTH_TEST)
glEnable(GL_TEXTURE_2D)
gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)

texture_id = render_earth.load_texture("textures/Earth_Diffuse.jpg")
sphere_data = create_sphere()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, rejected = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)

    if ids is not None:
        for corner in corners:
            rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corner, 0.05, camera_matrix, dist_coeffs)
            rmat, _ = cv2.Rodrigues(rvec[0][0])
            mat = np.identity(4)
            mat[:3, :3] = rmat
            mat[:3, 3] = tvec[0][0]
            glLoadMatrixf(mat.T)

            glRotatef(pygame.time.get_ticks() * 0.05, 0, 1, 0)
            render_earth.draw_textured_sphere(sphere_data, texture_id)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            pygame.quit()
            exit()

cap.release()
cv2.destroyAllWindows()
