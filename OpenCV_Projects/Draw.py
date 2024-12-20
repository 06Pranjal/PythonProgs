#program for creation of blank image in black colour
import cv2 as cv
import numpy as np

#create a blank image
blank=np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank',blank)

cv.waitKey(0)