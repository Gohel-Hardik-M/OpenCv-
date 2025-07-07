# In this block of code we are gonna split the image into BGR formate like we will get the Red scale , Blue Scale , And Green Scale Images


import cv2 as cv


img = cv.imread('Photos/war.jpg')
cv.imshow('Original Image',img)

b,g,r= cv.split(img)

cv.imshow('Blue',b)   #Blue Scale image
cv.imshow('Green',g)  #Green scale image
cv.imshow('Red',r)    #Red scale image

# shapes of every images
print(img.shape)   
print(b.shape)
print(g.shape)
print(r.shape)

# Merging blue , green and red scale images to get the original one 
merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)


cv.waitkey(0)
