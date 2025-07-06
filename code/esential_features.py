import cv2 as cv
img = cv.imread('photos/war.jpg')
cv.imshow('oRIGINAL IMAG',img)

croped = img[0:250,250:260]
cv.imshow('Croped',croped)

cv.waitKey(0)
