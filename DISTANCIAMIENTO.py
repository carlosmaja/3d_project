"""
3D-COMPUTER VISION.ipynb

## import all libraries & Load Images
"""

# Commented out IPython magic to ensure Python compatibility.
import os
import cv2
import numpy as np
from PIL import Image
import glob
import pyvista as pv
from pyvista import set_plot_theme
set_plot_theme("dark")
import vtk
from matplotlib import pyplot as plt
from scipy import ndimage as ndi
from skimage import (exposure, feature, filters, io, measure,
                      morphology, restoration, segmentation, transform,
                      util)

from skimage import img_as_ubyte
from matplotlib import pyplot as plt
from PIL import Image
import imageio
# Leer todas las imágenes JPG en un directorio específico
import numpy as np
import pyvista as pv
from PIL import Image
import os
from vtk import VTK_VERTEX

# Ruta al directorio donde están las imágenes TIFF
ruta_imagenes = 'C:\\Users\\CHIPY\\Desktop\\DEBERES MASTER\\3D\\IMG_DREAM_Morph_3'  # Cambia a tu ruta

# Filtrar solo los archivos TIFF
imagenes = [os.path.join(ruta_imagenes, img) for img in os.listdir(ruta_imagenes) if img.endswith(('tif', 'tiff'))]

# Listas para almacenar todos los puntos y celdas
todos_los_puntos = []
todas_las_celdas = []
indice_punto = 0
print(imagenes[0])
# Recorrer todas las imágenes
for idx, ruta in enumerate(imagenes):
    # Cargar la imagen TIFF y convertirla a escala de grises
    imagen = Image.open(ruta)
    imagen_array = np.array(imagen)
    height, width = imagen_array.shape

    # Crear puntos para la imagen actual
    puntos = []
    for y in range(height):
        for x in range(width):
            z = imagen_array[y, x]  # Usa el valor de intensidad como coordenada Z
            # Separar por 2 y desplazar cada imagen en el eje Z para que no se solapen
            puntos.append([x *2, y*2 , idx * 50 + z])  # idx*50 desplaza cada imagen hacia "arriba"

    # Convertir la lista de puntos a un array y agregarla a la lista global
    puntos = np.array(puntos)
    todos_los_puntos.append(puntos)

    # Crear celdas para cada punto de la imagen actual
    num_puntos = len(puntos)
    celdas = np.hstack([[1, i + indice_punto] for i in range(num_puntos)])  # Formato [1, index] para cada punto
    todas_las_celdas.append(celdas)

    # Actualizar el índice de puntos para la siguiente imagen
    indice_punto += num_puntos
print("ya salio del bucle")
# Convertir todas las listas a arrays de PyVista
todos_los_puntos = np.vstack(todos_los_puntos)
todas_las_celdas = np.hstack(todas_las_celdas)
tipos_celdas = np.full(todos_los_puntos.shape[0], VTK_VERTEX)
print("aqui")
# Crear el UnstructuredGrid con todos los puntos y celdas
grid = pv.UnstructuredGrid(todas_las_celdas, tipos_celdas, todos_los_puntos)

# Visualizar el UnstructuredGrid en PyVista
plotter = pv.Plotter()
plotter.add_mesh(grid, color='blue', point_size=5, render_points_as_spheres=True)
plotter.show()

"""


imagenes = [os.path.join(ruta_imagenes, img) for img in os.listdir(ruta_imagenes) if img.endswith(('tif', 'tiff'))]

# Listas para almacenar todos los puntos y celdas
todos_los_puntos = []
todas_las_celdas = []
indice_punto = 0
print(imagenes[0])
# Recorrer todas las imágenes
for idx, ruta in enumerate(imagenes):
    # Cargar la imagen TIFF (se asume que ya está en blanco y negro)
    imagen = Image.open(ruta)
    imagen_array = np.array(imagen)
    height, width = imagen_array.shape

    # Crear puntos para la imagen actual, filtrando solo los negros
    puntos = []
    for y in range(height):
        for x in range(width):
            z = imagen_array[y, x]
            if z == 0:  # Solo agregar puntos que son negros (intensidad 0)
                puntos.append([x * 2, y * 2, idx * 50])  # idx*50 desplaza cada imagen hacia "arriba"

    # Convertir la lista de puntos a un array y agregarla a la lista global
    puntos = np.array(puntos)
    todos_los_puntos.append(puntos)

    # Crear celdas para cada punto de la imagen actual
    num_puntos = len(puntos)
    if num_puntos > 0:
        celdas = np.hstack([[1, i + indice_punto] for i in range(num_puntos)])  # Formato [1, index] para cada punto
        todas_las_celdas.append(celdas)

    # Actualizar el índice de puntos para la siguiente imagen
    indice_punto += num_puntos

# Convertir todas las listas a arrays de PyVista
todos_los_puntos = np.vstack(todos_los_puntos)
todas_las_celdas = np.hstack(todas_las_celdas)
tipos_celdas = np.full(todos_los_puntos.shape[0], VTK_VERTEX)

# Verificar si hay puntos antes de crear la malla para evitar errores
if todos_los_puntos.size > 0:
    # Crear el UnstructuredGrid con todos los puntos y celdas
    grid = pv.UnstructuredGrid(todas_las_celdas, tipos_celdas, todos_los_puntos)

    # Visualizar el UnstructuredGrid en PyVista
    plotter = pv.Plotter()
    plotter.add_mesh(grid, color='black', point_size=5, render_points_as_spheres=True)
    plotter.show()
else:
    print("No se encontraron puntos negros en las imágenes.")
    """