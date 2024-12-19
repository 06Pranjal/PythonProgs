#htis is for resizing and rescaling the videos images andlive video

import cv2 as cv

# img=cv.imread('Pics/images (1).jpeg')
# cv.imshow('Cat',img)

def rescaleFrame(frame,scale=0.75):
    # this method is for images,videos,live Videos
    width=int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    dimensions =(width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

#this works for live videos only
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)
#read videos

capture= cv.VideoCapture('Videos/855029-hd_1920_1080_30fps.mp4')

while True:
    isTrue, frame =capture.read()

    frame_resized= rescaleFrame(frame,scale=0.2)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()