import cv2 as cv
import numpy as np 

blank = np.zeros((400,400),dtype='uint8)
#Rectangle
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
#Circle 
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)   

# Bitwise AND  :-->placing two images on top of each other and adds them with each other
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise AND', bitwise_and)

# Bitwise OR  :-->founds non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("Bitwise OR", bitwise_or)


# Bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("Bitwise XOR",bitwise_xor)

# Bitwise NOT -->  Swaps the colors 
bitwise_not = cv.bitwise_not(rectnagle)
cv.imshow("BItwise NOT --> Recatnagle",bitwise_not)

bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow("BItwise NOT --> Circle",bitwise_not_circle)




cv.waitKey(0)

