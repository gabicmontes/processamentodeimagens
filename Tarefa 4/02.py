import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
    
    __, frame = cap.read()
    
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerYellow = np.array([25, 50, 0])
    upperYellow = np.array([50, 220, 255])
    
    mask = cv2.inRange(hsvFrame, lowerYellow, upperYellow)
    
    #cv2.imshow('mask', mask)
    #pega o contorno
    __, contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if(contours.all()):
        i = 0
        maiorArea = cv2.contourArea(contours[0])
        idContourMaiorArea = 0
        for cnt in contours:
            if maiorArea < cv2.contourAreaArea(cnt):
                maiorArea = cv2.contourArea(cnt)
                idContourMaiorArea = 1
            i += 1
        x,y,w,h = cv2.boundingRect(contours[idContourMaiorArea])
        if(maiorArea > 100):
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255) , 3)       
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    
    
    
    
    