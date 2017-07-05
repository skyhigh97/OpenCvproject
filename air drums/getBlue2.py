# to do list
# get image
# sub background
# get Colors        - done
# get contour
# divide screen
# make sounds and trigger events
##lower_blue = np.array([110,50,50])
##upper_blue = np.array([130,255,255])

import cv2
import numpy as np
import math

def nothing(x):
    pass

cv2.namedWindow('image')
# create trackbars for color change
cv2.createTrackbar('hl','image',0,255,nothing)
cv2.createTrackbar('sl','image',0,255,nothing)
cv2.createTrackbar('vl','image',0,255,nothing)
cv2.createTrackbar('hu','image',0,255,nothing)
cv2.createTrackbar('su','image',0,255,nothing)
cv2.createTrackbar('vu','image',0,255,nothing)

cap = cv2.VideoCapture(0)

kernel_square = np.ones((11,11),np.uint8)
kernel_ellipse= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

while(True):
    
    _, frame = cap.read()
    blur = cv2.blur(frame,(3,3))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hl = cv2.getTrackbarPos('hl','image')
    sl = cv2.getTrackbarPos('sl','image')
    vl = cv2.getTrackbarPos('vl','image')
    hu = cv2.getTrackbarPos('hu','image')
    su = cv2.getTrackbarPos('su','image')
    vu = cv2.getTrackbarPos('vu','image')

    

    lower_blue = np.array([hl,sl,vl])
    upper_blue = np.array([hu,su,vu])    

    # Threshold the HSV image to get only blue colors
    mask2 = cv2.inRange(hsv, lower_blue, upper_blue)
    dilation = cv2.dilate(mask2,kernel_ellipse,iterations = 1)
    erosion = cv2.erode(dilation,kernel_square,iterations = 1)    
    dilation2 = cv2.dilate(erosion,kernel_ellipse,iterations = 1)    
    filtered = cv2.medianBlur(dilation2,5)
    kernel_ellipse= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(8,8))
    dilation2 = cv2.dilate(filtered,kernel_ellipse,iterations = 1)
    kernel_ellipse= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    dilation3 = cv2.dilate(filtered,kernel_ellipse,iterations = 1)
    median = cv2.medianBlur(dilation2,5)
    ret,thresh = cv2.threshold(median,127,255,0)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask2)

    _,contours, hierarchy =  cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)   
    max_area=0
    ci=0
    print len(contours)
    if len(contours)!=0: # draw a circle about the blob
        for c in contours:
            # get the bounding rect
            x, y, w, h = cv2.boundingRect(c)
            # draw a green rectangle to visualize the bounding rect
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
            # get the min area rect
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            # convert all coordinates floating point values to int
            box = np.int0(box)
            # draw a red 'nghien' rectangle
            cv2.drawContours(frame, [box], 0, (0, 0, 255))
 
            # finally, get the min enclosing circle
            (x, y), radius = cv2.minEnclosingCircle(c)
        # convert all values to int
            center = (int(x), int(y))
            radius = int(radius)
            # and draw the circle in blue
            img = cv2.circle(frame, center, radius, (255, 0, 0), 2)
        cv2.imshow("contours", img)
        cv2.drawContours(img, contours, -1, (255, 255, 0), 1)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
