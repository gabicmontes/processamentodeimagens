import cv2
import math
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

def showGrid(imgArray, titleArray):
    
    tamanho = len(imgArray)
    
    if(tamanho == 0):
        print("ERRO: Array vazio")
        return 
    
    elif (tamanho == 1):  
        plt.subplot(1,1,1),plt.imshow(imgArray[0], cmap='gray')
        plt.title(titleArray[0]), plt.xticks([]), plt.yticks([])
           
    elif (tamanho == 2):        
        plt.subplot(2,2,1),plt.imshow(imgArray[0],cmap = 'gray')
        plt.title(titleArray[0]), plt.xticks([]), plt.yticks([])
        
        plt.subplot(2,2,2),plt.imshow(imgArray[1],cmap = 'gray')
        plt.title(titleArray[1]), plt.xticks([]), plt.yticks([])
            
    else:          
        c = math.ceil(tamanho/3)
        i, titleId = 1,0 
        
        for img in imgArray: 
            plt.subplot(c,3,i),plt.imshow(img, cmap='gray')
            plt.title(titleArray[titleId]), plt.xticks([]), plt.yticks([])
            i += 1
            titleId += 1
                
    plt.show()   

def applyFilter(img, filterName):
    
    if(filterName == "media"):
        media = cv2.blur(img,(51,51))
        return media
    
    if(filterName == "gaussiano"):
        gauss = cv2.GaussianBlur(img,(51,51),0)
        return gauss
    
    if(filterName == "mediana"):
        mediana = cv2.medianBlur(img,51)
        return mediana
    
    if(filterName == "laplaciano"):
        laplaciano = cv2.Laplacian(img,cv2.CV_64F)
        return laplaciano
    
    if(filterName == "sobelx"):
        sobelX = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
        return sobelX
    
    if(filterName == "sobely"):
        sobelY = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
        return sobelY

    
def main():
    
    img = cv2.imread("dog.jpg", 0)
    imgArray = [img]
    titleArray = ["Original"]
    
    imgArray.append(applyFilter(img, "media"))
    titleArray.append("media")
    imgArray.append(applyFilter(img, "gaussiano"))
    titleArray.append("gaussiano")
    imgArray.append(applyFilter(img, "mediana"))
    titleArray.append("mediana")
    imgArray.append(applyFilter(img, "sobely"))
    titleArray.append("sobely") 
    imgArray.append(applyFilter(img, "sobelx"))
    titleArray.append("sobelx")                      
    imgArray.append(applyFilter(img, "laplaciano"))
    titleArray.append("laplaciano")
    
    
    showGrid(imgArray, titleArray)
    
main()
