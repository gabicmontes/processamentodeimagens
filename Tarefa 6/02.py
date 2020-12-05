import cv2
from matplotlib import pyplot as plt

img = cv2.imread("img.png")

src = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = cv2.equalizeHist(src)
plt.subplot(2,1,1),plt.imshow(src, cmap='gray')
plt.subplot(2,1,2),plt.imshow(dst, cmap='gray')
cv2.waitKey()