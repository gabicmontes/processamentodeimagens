import cv2
import numpy as np
from matplotlib import pyplot as plt

imgPB = cv2.imread("03.jpg", 0)
imgColor = cv2.imread("01.jpg")

color = ('b', 'g', 'r')

for i, col in enumerate(color):
    print(i, col)
    histr = cv2. calcHist([imgColor], [i], None, [256], [0,256])
    plt.subplot(2,2,1),plt.plot(histr, color = col)
    plt.xlim([0, 256])

imgColorRGB = cv2.cvtColor(imgColor, cv2.COLOR_BGR2RGB)

plt.subplot(2,2,2),plt.hist(imgPB.ravel(), 256, [0, 256])
plt.subplot(2,2,4),plt.imshow(imgPB, cmap='gray')
plt.subplot(2,2,3),plt.imshow(imgColorRGB, cmap='gray')
#cv2.imshow("Imagem", imgColor)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()