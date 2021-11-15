import cv2
import numpy as np
import matplotlib
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt

# 1. leer la imagen (RGB)
img = cv2.imread('Imagenes/Elprofe.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
###

###
# 2. convertir a escala de grises
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
plt.imshow(img_gray, cmap='gray')

# 3. plotear histograma de la imagen en escala de grises

# plotear su histograma
img_Hist = img_gray.flatten()
"""
plt.figure( figsize=(10,5) )
plt.title( 'Hue Values' )
plt.xlabel( 'Valor Hue' ); plt.ylabel( 'Frecuencia' )
Hist = plt.hist( img_Hist, 70)
plt.show()
# 4. crear máscara binaria a partir del umbral del histograma
"""
BN = cv2.inRange(img_gray, 0, 150)

fig = plt.figure(figsize=(10, 10))
plt.imshow(BN, cmap='gray')
plt.axis('off')
plt.show()

canny= cv2.Canny(BN,0,100)
canny= cv2.dilate(canny,None, iterations=1)

plt.imshow(canny, cmap='gray')
plt.show()
