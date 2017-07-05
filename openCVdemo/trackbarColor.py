#Trackbar as the Color Palette

import cv2
import numpy as np

def nothing(x) :
    pass

#create a window with screen black
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

#create sliders
cv2.createTrackbar( 'RED'  ,'image' ,0,255,nothing)
cv2.createTrackbar( 'GREEN','image' ,0,255,nothing)
cv2.createTrackbar( 'BLUE' ,'image' ,0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n 1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('RED','image')
    g = cv2.getTrackbarPos('GREEN','image')
    b = cv2.getTrackbarPos('BLUE','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()
