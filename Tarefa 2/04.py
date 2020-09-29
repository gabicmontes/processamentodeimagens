import numpy as np
import cv2
import os

obj_img = cv2.imread("novos.png")

x = 550
y = 100

altura = 130
largura = 110

for i in range(y, y+altura):
    for j in range(x, x+largura):
        obj_img.itemset((i,j,0), 0)
        obj_img.itemset((i,j,1), 0)
        obj_img.itemset((i,j,2), 0)

cv2.imwrite("novos_sem_moreira.png", obj_img)