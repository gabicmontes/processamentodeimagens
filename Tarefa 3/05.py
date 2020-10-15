import cv2
import numpy as np
from matplotlib import pyplot as plt

caetano = cv2.imread("caetano.jpg")
chico = cv2.imread("chico.jpg")

caetachico = cv2.addWeighted(chico, 0.5, caetano, 0.5, 0)

caetachico = cv2.cvtColor(caetachico, cv2.COLOR_BGR2RGB)
plt.imshow(caetachico)
plt.show()