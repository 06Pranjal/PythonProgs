#read videos from a file to a new window
import cv2 as cv
#we can provide a argument 0 for webcam, 1 for first camera , 2 for second camera
#you can also provide path for the video

capture= cv.VideoCapture('Videos/855029-hd_1920_1080_30fps.mp4')

while True:
    isTrue, frame =capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()