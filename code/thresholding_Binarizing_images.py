import cv2 as cv

#Reafing Original Image
img = cv.imread('Photos/war.jpg')
cv.imshow('Original Image',img)


#Conevrting Original IMage into Gray IMage
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY IMAGE',gray) 

  
#Simple THresholding 
threshold, thresh = cv.threshold(gray,150,255, cv.THRESH_BINARY)
cv.imshow('simple thresholded',thresh)

# Inverse THresholding 
threshold , thresh_inv = cv.threshold(gray,150,255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse THresholded IMAGE',thresh_inc)

#Adaptive THresholding 
adaptive_thresh = cv.adaptiveThreshold(gray , 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV , 11,9)
cv.imshow('Adaptive Thresh Image',adaptive_thresh)

 

cv.waitKey(0)
