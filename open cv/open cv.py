import cv2 as cv
import numpy as np
video = cv.VideoCapture("./Video/ball.mp4")
while True:
    isTrue,frame = video.read()
    if int(isTrue)==0:
        break    
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([75, 255, 255])
    mask = cv.inRange(hsv,lower_green,upper_green)
    contours,_ = cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for contour in contours:
     approx = cv.approxPolyDP(contour,0.01*cv.arcLength(contour,True),True)
     if(len(approx)>12):
        x, y, w, h = cv.boundingRect(contour)
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv.imshow("Video",frame)
    if cv.waitKey(20) & 0XFF==ord("k"):
        break
video.release()
cv.destroyAllWindows()