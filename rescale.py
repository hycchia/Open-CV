import cv2 as cv



def rescaleFrame(frame,scale = 0.1):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

img = cv.imread('Resources/Photos/cat_large.jpg')
cv.imshow('Cat',rescaleFrame(img))
cv.waitKey(0)

capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video',frame)
    cv.imshow('AnotherVideo',rescaleFrame(frame))

    if cv.waitKey(20) & 0xFF==ord('d'): #if letter d is press, break the loop
        break

capture.release()
cv.destroyAllWindows()