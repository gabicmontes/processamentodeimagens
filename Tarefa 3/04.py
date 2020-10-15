import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("sonic.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        if((img.item(i,j,2) - img.item(i,j,0) > 30) and (img.item(i,j,2) - img.item(i,j,1) > 30)):
            img.itemset((i,j,1),(img.item(i,j,1) + 60))
            img.itemset((i,j,0),0)
            img.itemset((i,j,2),0)

for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        if((img.item(i,j,0) - img.item(i,j,1) > 75) and (img.item(i,j,0) - img.item(i,j,2) > 75)):
            img.itemset((i,j,0),(img.item(i,j,0) + 60))
            img.itemset((i,j,1),(img.item(i,j,1) + 140))
            img.itemset((i,j,2),0)


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imwrite("Brasonic.jpg",img)
