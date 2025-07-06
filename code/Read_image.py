import cv2 as cv

# Readifng Image
img = cv.imread('photos/war.jpg')
cv.imshow('war',img)
cv.waitKey(0)


# TO read video 
capture = cv.VideoCapture('vd/EXAMPLES.mp4')
while True :
    isTrue , frame = capture.read()
    cv.imshow('vedio',frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
