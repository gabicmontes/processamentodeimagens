import cv2
import time
import numpy as np

ESCAPE_KEY_ASCII = 27

def onChange(value):
    pass

def dilatacao(img, shape):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,shape)   
    dilatacao_dst = cv2.dilate(img, kernel)
    return dilatacao_dst

def erosao(img, shape):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,shape)   
    erosao_dst = cv2.erode(img, kernel)
    return erosao_dst

def main():
    
    ESCAPE_KEY_ASCII = 27
    
    img = cv2.imread("j.png", 0)
    imgMorfologica = img
    windowTitle = "Operações Morfológicas"
    cv2.namedWindow(windowTitle)
        
    cv2.createTrackbar("intensidade", windowTitle, 0, 50, onChange)
    
    before = 0
    update = False
    cont_time = 0
    
    largura = img.shape[1]
    altura =  img.shape[0]
    dimensoes = (largura,altura)
    
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    out = cv2.VideoWriter('video.avi',fourcc, 20.0, dimensoes)
        
    
    while(True):
        
        after = cv2.getTrackbarPos("intensidade", windowTitle)
        
        if before != after:        
            update = True
            cont_time = time.time()
            before = after
        
        if update == True and time.time() - cont_time > 1:
            #imgMorfologica = erosao(img, (after,after))
            imgMorfologica = dilatacao(img, (after,after))
            update = False
        
        cv2.imshow(windowTitle, imgMorfologica)    
        k = cv2.waitKey(1) & 0xFF
        if k == ESCAPE_KEY_ASCII:
            break
        
       
        frame = np.array(imgMorfologica)
        out.write(frame)
        
    out.release()
    cv2.destroyAllWindows()

main()











