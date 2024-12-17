#this is just for how to import any image from folder to new windows to read
import cv2 as cv

img=cv.imread('Pics/images.jpeg')#to read image

cv.imshow('Cat',img)#to show up the image

cv.waitKey(0)#to give infinte delay to the window until any button is pressed