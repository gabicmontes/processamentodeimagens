import cv2
from matplotlib import pyplot as plt


dog = cv2.imread("dog.jpg")
marca = cv2.imread("marca.png")

dogmarca = cv2.addWeighted(dog, 0.7, marca, 0.3, 0)
dogmarca = cv2.cvtColor(dogmarca, cv2.COLOR_BGR2RGB)

plt.imshow(dogmarca)
plt.show()










