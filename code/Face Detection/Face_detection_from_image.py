import cv2 as cv
import numpy as np 

# Classifier
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# to detect the face in any image firstly we need to convert the original image into a GRAY scale image
img = cv.imread('Face Detection Images/group 1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Getting the rectangle pixels array where the face exists using harr_cascade 
face_rect = haar_cascade.detectMultiScale(gray,1.1)

# Drawing  a rectangle around the face To display where the exactly face is.
for (x,y,w,h) in face_rect:
  face_roi = gray[y:y+h,x:x+w]
  cv.putText(gray,"Detected Face is Here",(x,y-20),cv.FONT_HERHEY_SIMPLEX,1.0,(0,255,0),thickness = 2)
  cv.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Face Detected Image',gray)
cv.waitKey(0)


