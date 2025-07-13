import cv2 as cv
import numpy as np
video=cv.VideoCapture(0)
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])



ret,frame=video.read()
canvas=np.zeros_like(frame)

prev_center=None
while True:
    ret,frame=video.read()
    
    mirror_video=cv.flip(frame,1)
    hsv=cv.cvtColor(mirror_video,cv.COLOR_BGR2HSV) 

    b_mask=cv.inRange(hsv,lower_blue,upper_blue)
    

    blue=cv.bitwise_and(mirror_video,mirror_video,mask=b_mask)

    b_mask=cv.erode(b_mask,None,iterations=2)
    
    b_mask=cv.dilate(b_mask,None,iterations=2)
    counters,_=cv.findContours(b_mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    if counters:
        c = max(counters, key=cv.contourArea)
        M = cv.moments(c)
   
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            center = (cx, cy)
        cv.drawContours(frame, [c], -1, (0, 255, 0), 2)
        cv.circle(mirror_video, center, 5, (0, 0, 255), -1)
        if prev_center is not None:
            cv.line(canvas,prev_center,center,(255,0,0),4)
        prev_center=center    


        
    if ret==True:
        combined=cv.add(mirror_video,canvas)
        cv.imshow("video",combined)
        cv.imshow("mask",blue)
        
    key=cv.waitKey(1)
    if key==ord('q'):
        break
cv.destroyAllWindows()
