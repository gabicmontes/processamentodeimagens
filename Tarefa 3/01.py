import numpy as np
import cv2
from matplotlib import pyplot as plt


def crop(img,y1,y2,x1,x2):
    crop_img = img[ y1:y2 , x1:x2 ]
    return crop_img
    
img = cv2.imread("kiss.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
y1=70; y2=160; x1=395; x2=465
img_crop = crop(img,y1,y2,x1,x2)

plt.imshow(img_crop)
plt.show()


