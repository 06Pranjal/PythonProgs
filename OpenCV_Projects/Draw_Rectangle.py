#program for creation of green rectangle on black colour
import cv2 as cv
import numpy as np

#create a blank image
blank=np.zeros((500,500,3), dtype='uint8')


#Recatngle in Green
cv.rectangle(blank,(100,100),(300,300),(0,255,0),thickness=3)
cv.imshow('Green Rectangle',blank)


#in thickness option to fill the complete rectangle in a color we can use -1 or cv.Filled also
cv.waitKey(0)