import numpy as np
import cv2
import os

obj_img = cv2.imread("novos.png")

obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
altura, largura, canais = obj_img.shape
print("Dimensões da Imagem: ", largura, " x ", altura)
print("Canais de cor: ", canais)

b = os.stat("novos.png").st_size
print("Bytes da imagem: ", b)