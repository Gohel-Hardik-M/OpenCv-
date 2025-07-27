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

 

cv.waitKey(0)
