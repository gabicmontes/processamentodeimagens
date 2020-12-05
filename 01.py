import numpy as np
import cv2

def computeKmeans(image):
    Z = image.reshape((-1, 3))
    Z = np.float32(Z)
    
    #criterio de parada
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 4, 0.1)
    # quantidade de cores
    K = 256
    
    _, labels, centroides = cv2.kmeans(Z, K, None, criteria, 4, cv2.KMEANS_RANDOM_CENTERS)
    
    centroides = np.uint8(centroides)
    imagemColorida = centroides[labels.flatten()]
    imagemFinal = imagemColorida.reshape(image.shape)
    
    cv2.imshow("Original", image)
    cv2.imshow("Resultado", imagemFinal)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():

    image = cv2.imread('img.jpg')
    computeKmeans(image)    

if __name__ == "__main__":
    main()
    
    