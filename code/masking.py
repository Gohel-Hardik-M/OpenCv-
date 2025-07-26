import cv2 as cv
import numpy as np 
img = cv.imread('Photos/war.png')
cv.imshow('Img',img)


blank =  np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank Image',blank)

masked = cv.bitwise_and(img,img,mask = mask)
cv.imshow('Masked Image', masked)

cv.waitkey(0)
