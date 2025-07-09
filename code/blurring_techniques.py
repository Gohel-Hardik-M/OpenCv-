import cv2 as cv

img = cv.imread('Photos/war.jpg')
cv.imshow('Original Image',img)


# 1st Method --> Avaraging 
avarage = cv.blur(img,(3,3))   # (3,3) -->is the kernel size --> Higher The kerner size more the blurr effect
cv.imshow(" Avarage Blurr Image",avarage)


# 2nd Method --> Gaussian Blur
gaussian = cv.GaussianBlur(img , (7,7),0)
cv.imshow("gaussian Blur",gaussian)

# 3rd Method --> Median Blur
median = cv.medianBlur(img,3)
cv.imshow("Median Blur",median)

# 4th method -->Bilateral 
bilatera; = cv.bilateralFilter(img,5,15, 15 )

cv.waitKey(0)


