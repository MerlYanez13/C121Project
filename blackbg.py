import cv2
import time
import numpy as np
image=cv2.imread("me.jpg")
cap=cv2.VideoCapture(0)
time.sleep(2)
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    image=cv2.resize(image,(640,480))
    upperBlack=np.array([104,153,70])
    lowerBlack=np.array([30,30,0])
    mask=cv2.inRange(frame,lowerBlack,upperBlack)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    f=frame-result
    f=np.where(f==0,image,f)
    cv2.imshow("video",frame)
    cv2.imshow("mask",f)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()