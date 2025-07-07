 import cv2 as cv

img = cv.imread('Photos/war.jpg')
cv.imshow('Original Image',img)

b,g,r= cv.split(img)

cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


cv.waitkey(0)
