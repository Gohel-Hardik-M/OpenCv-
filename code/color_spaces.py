import cv2 as cv

img = cv.imread('Photos/war.jpg')
cv.imshow('Orignal Image',img)

#COnverting original image in grayscale image 
gray = cv.cvtcolor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# COnverting to HSV image 
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV ',hsv)

# COnverting to L*A*B img
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

#Convering to RGB Image
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

cv.waitkey(0)


