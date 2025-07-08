import cv2 as cv

img = cv.imread('Photos/war.jpg')
cv.imshow('Original Image',img)


# 1st Method --> Avaraging 
avarage = cv.blur(img,(3,3))   # (3,3) -->is the kernel size --> Higher The kerner size more the blurr effect
cv.imshow(" Avarage Blurr Image",avarage)


# 2nd Method --> Gaussian Blur


cv.waitKey(0)


