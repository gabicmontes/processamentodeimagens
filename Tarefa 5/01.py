import cv2
import numpy as np
import time

ESCAPE_KEY_ASCII = 27

img = cv2.imread("uni.jpg", 0)
imglimiar = img
windowTitle = "Limiarizacao"
cv2.namedWindow(windowTitle)

def onChange(value):
    #print("valor alterado", value)
    pass

cv2.createTrackbar("limiar", windowTitle, 127, 255, onChange)

before_limiar = 127
update = False
cont_time = 0

while(True):
    
    after_limiar = cv2.getTrackbarPos("limiar", windowTitle)
    
    if before_limiar != after_limiar:        
        update = True
        cont_time = time.time()
        before_limiar = after_limiar
    
    if update == True and time.time() - cont_time > 1:
        limiar, imglimiar = cv2.threshold(img, after_limiar, 255, cv2.THRESH_BINARY)
        update = False
    
    cv2.imshow(windowTitle, imglimiar)    
    k = cv2.waitKey(1) & 0xFF
    if k == ESCAPE_KEY_ASCII:
        break

cv2.destroyAllWindows()












