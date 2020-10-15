import numpy as np
import cv2
from matplotlib import pyplot as plt

def crop(img,y1,y2,x1,x2):
    crop_img = img[ y1:y2 , x1:x2 ]
    return crop_img

def paste(img, crop_img, y,x):
    img[y:y+crop_img.shape[0], x:x+crop_img.shape[1]] = crop_img
    return img

#chamando e convertendo a imagem 
img = cv2.imread("kiss.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#crop: definindo a região de interesse e chamando a função
y1=70; y2=160; x1=395; x2=465
img_crop = crop(img,y1,y2,x1,x2)

#paste: definindo inicio do x e y de onde começa a colagem / chamando a função
y=60; x=490
paste_img = paste(img,img_crop,y,x)

plt.imshow(paste_img)
plt.show()