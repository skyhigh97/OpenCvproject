import numpy as np
import cv2

# Create a black image
screen = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(screen,(0,0),(511,511),(255,0,0),5)
# Draw a cyan rectangle with thickness of 3 px at  top-right corner
cv2.rectangle(screen,(384,0),(510,128),(255,255,0),-1)

#draw red circle inside rectangle (-1 thickness = filled)
# center co.ord = (447,63) Radius = 63 color = white (255,255,255)
cv2.circle(screen,(447,63), 63, (255,255,255), -1)

#draw a green  ellipse : center ,(axes lengths), angle of rotn.,start angle, end angle 
cv2.ellipse(screen,(256,256),(100,50),0,0,300,(0,255,0),-1)

#draw red polygon of 5  sides. Make coordinates of vertices
#into an array of shape ROWSx1x2 where ROWS are number of
#vertices and it should be of type int32. 
pts = np.array([[300,200],[100,300],[100,500],[500,500], [500,300]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(screen,[pts],True,(0,0,255),3)

#text view
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(screen,'AKASH ',(100,500), font, 4,(255,255,255),2,cv2.LINE_AA)

while(1):
    cv2.imshow('SCREEN',screen)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()
    
