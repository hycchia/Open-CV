import cv2 as cv

# Read Images
# img = cv.imread('Resources/Photos/cat_large.jpg')
# cv.imshow('Cat',img)
# cv.waitKey(0)


# Read Video
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue,frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #if letter d is press, break the loop
        break

capture.release()
cv.destroyAllWindows()
