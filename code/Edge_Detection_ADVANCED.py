import cv2 as cv
import numpy as np 

img = cv.imread('Photos/war.jpg')
cv.imshow('Original Image',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image',gray)


#Laplacian 
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)


# Sobel 
sobelx = cv.Sobel(gray, cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)

combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('SObel X',sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('Combined Sobel',combined_sobel)


canny = cv.Canny(gray,150,175)
cv.imshow('Canny Image',canny)

cv.waitKey(0)
