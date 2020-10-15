import numpy as np
import cv2
from matplotlib import pyplot as plt

img_orig = cv2.imread("kiss.jpg")
img_red = cv2.imread("kiss.jpg")
img_blue = cv2.imread("kiss.jpg")
img_green = cv2.imread("kiss.jpg")

img_orig = cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)
img_red = cv2.cvtColor(img_red, cv2.COLOR_BGR2RGB)
img_green = cv2.cvtColor(img_green, cv2.COLOR_BGR2RGB)
img_blue = cv2.cvtColor(img_blue, cv2.COLOR_BGR2RGB)

img_red[:,:,2] = 0
img_red[:,:,1] = 0

img_blue[:,:,0] = 0
img_blue[:,:,1] = 0

img_green[:,:,0] = 0
img_green[:,:,2] = 0

vermelho = 0; verde = 0; azul = 0
        
for i in range(0, img_green.shape[0]):
    for j in range(0, img_green.shape[1]):
        verde = verde + img_green.item(i,j,1)
        
for i in range(0, img_red.shape[0]):
    for j in range(0, img_red.shape[1]):
        vermelho = vermelho + img_red.item(i,j,0)

for i in range(0, img_blue.shape[0]):
    for j in range(0, img_blue.shape[1]):
        azul = azul + img_blue.item(i,j,2)

total_pixel = img_orig.shape[0]*img_orig.shape[1]

vermelho = vermelho/total_pixel
verde = verde/total_pixel
azul = azul/total_pixel

print("Média de vermelho: ", vermelho)
print("Média de azul: ", azul)
print("Média de verde: ", verde)

if((vermelho > verde) and (vermelho > azul)):
    print("A imagem é mais vermelha")

if((azul > verde) and (azul > vermelho)):
    print("A imagem é mais azul")

if((verde > vermelho) and (verde > azul)):
    print("A imagem é mais verde")

plt.imshow(img_orig)
plt.show()