import numpy as np

def create_sphere(stacks=40, slices=40, radius=1.0):
    vertices = []
    texcoords = []
    indices = []

    for i in range(stacks + 1):
        lat = np.pi / 2 - i * np.pi / stacks
        xy = radius * np.cos(lat)
        z = radius * np.sin(lat)

        for j in range(slices + 1):
            lon = j * 2 * np.pi / slices
            x = xy * np.cos(lon)
            y = xy * np.sin(lon)
            vertices.append((x, y, z))
            texcoords.append((j / slices, i / stacks))

    for i in range(stacks):
        for j in range(slices):
            first = i * (slices + 1) + j
            second = first + slices + 1
            indices.extend([first, second, first + 1])
            indices.extend([second, second + 1, first + 1])

    return vertices, texcoords, indices
