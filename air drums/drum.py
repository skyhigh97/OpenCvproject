

import numpy as np
import cv2
import pygame
import math
import pygame.mixer
pygame.mixer.init()

snare = pygame.mixer.Sound("SnareDrum.wav")
hithat = pygame.mixer.Sound("rimshot.wav")
tom1 = pygame.mixer.Sound("midtom.wav")
tom2 = pygame.mixer.Sound("dry.wav")
pygame.mixer.Sound.play



kernel_square = np.ones((11,11),np.uint8)
kernel_ellipse= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
threshDone = False
def nothing(x):
    pass

#get the circle

def drawCircle(contours,frame):
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
    return img,center

#set thresh @starting
def setThresh():
    global threshDone
    threshDone=True
    hl = cv2.getTrackbarPos('hl','image')
    sl = cv2.getTrackbarPos('sl','image')
    vl = cv2.getTrackbarPos('vl','image')
    hu = cv2.getTrackbarPos('hu','image')
    su = cv2.getTrackbarPos('su','image')
    vu = cv2.getTrackbarPos('vu','image')
    return hl,sl,vl,hu,su,vu

#do the actual thresh
def doThresh(hsv,lower_blue,upper_blue):
    global kernel_ellipse
    global kernel_square
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
    return thresh,mask2

cv2.namedWindow('image')
# create trackbars for color change
cv2.createTrackbar('hl','image',0,255,nothing)
cv2.createTrackbar('sl','image',0,255,nothing)
cv2.createTrackbar('vl','image',0,255,nothing)
cv2.createTrackbar('hu','image',0,255,nothing)
cv2.createTrackbar('su','image',0,255,nothing)
cv2.createTrackbar('vu','image',0,255,nothing)

cap = cv2.VideoCapture(0)


#set the initial conditions

wasInTom1 = False
wasInTom2 = False 
wasInSnare = False
wasInHitHat = False

#coords
tom2Coords = (150,250,300,400)
tom1Coords = (330, 250,480, 400 )
snareCoords = (450, 50,600, 200)
hihatCoords = (50, 50,200, 200)

def tom1Hit(center):
    global wasInTom1
    center = center
    if inDrumZone(center, "tom1"):
        if wasInTom1 == False:
            wasInTom1 = True
            return True
        else:
            return False
    else:
        wasInTom1 = False
        return False

def tom2Hit(center):
    global wasInTom2
    center =center
    if inDrumZone(center, "tom2"):
        if wasInTom2 == False:
            wasInTom2 = True
            return True
        else:
            return False
    else:
        wasInTom2 = False
        return False

def snareHit(center):
    global wasInSnare 
    center = center
    if inDrumZone(center, "snare"):
        if wasInSnare == False:
            wasInSnare = True
            return True
        else:
            return False
    else:
        wasInSnare = False
        return False
        
def hithatHit(center):
    global wasInHitHat
    center = center
    if inDrumZone(center, "hihat"):
        if wasInHitHat == False:
            wasInHitHat = True
            return True
        else:
            return False
    else:
        wasInHitHat = False
        return False

def inDrumZone(center,drum):
    if drum == "tom2":
        if (center[0] > tom2Coords[0] and center[1] > tom2Coords[1] and
            center[0] < tom2Coords[2] and center[1] < tom2Coords[3]):
            return True
        else:
            return False
    elif drum == "tom1":
        if (center[0] > tom1Coords[0] and center[1] > tom1Coords[1] and
            center[0] < tom1Coords[2] and center[1] < tom1Coords[3]):
            return True
        else:
            return False
    elif drum == "snare":
        if (center[0] > snareCoords[0] and center[1] > snareCoords[1] and
             center[0] < snareCoords[2] and center[1] < snareCoords[3]):
             return True
        else:
            return False
    elif drum == "hihat":
        if (center[0] > hihatCoords[0] and center[1] > hihatCoords[1] and
            center [0] < hihatCoords[2] and center[1] < hihatCoords[3]):
            return True
        else:
            return False
def playSounds(center):
    if tom1Hit(center):
        tom1.play()
    elif tom2Hit(center): 
        tom2.play()
    elif snareHit(center):
        snare.play()
    elif hithatHit(center):
        hithat.play()

while(True):
    #read frame
    _, frame = cap.read()
    blur = cv2.blur(frame,(3,3))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # threshold if not done
    if not threshDone:
        # if thresholded then proceed
        nothing(1)
    else:
        lower_blue = np.array([hl,sl,vl])
        upper_blue = np.array([hu,su,vu])    
        # Threshold the HSV image to get only blue colors
        thresh,mask2 = doThresh(hsv,lower_blue, upper_blue)
        cv2.imshow('mask',mask2)
        cv2.rectangle(frame,(150,250),(300,400),(0,255,0))
        cv2.rectangle(frame,(330, 250),(480, 400),(0,255,0))
        cv2.rectangle(frame,(450, 50),(600, 200),(0,255,0))
        cv2.rectangle(frame,(50, 50),(200, 200),(0,255,0))

        cv2.imshow('frame',frame)
        #get contours from threshed image
        _,contours, hierarchy =  cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)   
        max_area=0
        ci=0
        print len(contours)
        if len(contours)!=0: # draw a circle about the blob
            img,center = drawCircle(contours,frame)
            cv2.imshow("contours", img)
            cv2.drawContours(img, contours, -1, (255, 255, 0), 1)
            #draw the drum areas on the screen

            playSounds(center)
        
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    if k==ord('t'):
        hl,sl,vl,hu,su,vu=setThresh()

cv2.destroyAllWindows()
