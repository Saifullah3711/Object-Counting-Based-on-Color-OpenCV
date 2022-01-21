import cv2 
import numpy as np
import imutils




#=========================================================================
lower_yellow = np.array([18, 100, 52])  # yellow done 2000 area
upper_yellow = np.array([40, 255, 255])

lower_green = np.array([50, 59, 27])
upper_green = np.array([86, 255, 255])

lower_red = np.array([0, 89, 0])   # Red Done
upper_red = np.array([9, 255, 255])

lower_blue = np.array([86, 109, 14])
upper_blue = np.array([157, 255, 255])
#-------------------------------------------------------------------------------


def ContourCalculate(image):
    hsvImg = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsvImg, lower_yellow, upper_yellow)
    mask2 = cv2.inRange(hsvImg, lower_green, upper_green)
    mask3 = cv2.inRange(hsvImg, lower_red, upper_red)
    mask4 = cv2.inRange(hsvImg, lower_blue, upper_blue)

    cntr1 = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cntr1 = imutils.grab_contours(cntr1)

    cntr2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cntr2 = imutils.grab_contours(cntr2)

    cntr3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cntr3 = imutils.grab_contours(cntr3)

    cntr4 = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cntr4 = imutils.grab_contours(cntr4)

    lengthYellow = 0
    for y in cntr1:
        area1 = cv2.contourArea(y)
        if area1>1600:
            cv2.drawContours(image,[y], -1, (255,255,0),3)
            lengthYellow +=1
    

    lengthGreen = 0
    for g in cntr2:
        area1 = cv2.contourArea(g)
        if area1>1600:
            cv2.drawContours(image,[g], -1, (255,255,0),3)
            lengthGreen +=1
    

    lengthRed = 0
    for r in cntr3:
        area1 = cv2.contourArea(r)
        if area1>1600:
            cv2.drawContours(image,[r], -1, (255,255,0),3)
            lengthRed +=1

    lengthBlue = 0
    for b in cntr4:
        area1 = cv2.contourArea(b)
        if area1>1600:
            cv2.drawContours(image,[b], -1, (255,255,0),3)
            lengthBlue +=1
    cv2.putText(image,f'Yellow: {lengthYellow}', (20, 100),cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 0),3 )
    cv2.putText(image,f'Green: {lengthGreen}', (20, 160),cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 0),3 )
    cv2.putText(image,f'Red: {lengthRed}', (20, 220),cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 0),3 )
    cv2.putText(image,f'Blue: {lengthBlue}', (20, 280),cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 0),3 )





cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgS = img
    ContourCalculate(imgS)

    cv2.imshow("image", img)
    cv2.waitKey(1)


