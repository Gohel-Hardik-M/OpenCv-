import cv2 as cv
import numpy as np 

img = cv.imread('Photos/war.jpg')
cv.imshow('Original Image',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image',gray)
