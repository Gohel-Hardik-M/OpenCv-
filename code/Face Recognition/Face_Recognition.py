# Importing Required Models/Libraries
import os 
import numpy as np 
import cv2 as cv


# Classifier 
haar_cascade cv.CascadeClassifier('haar_face.xml')

# Features 
p = []
for i in os.listdir("Training Photos"):
  p.append(i)

# Reading our trained model to recognise the faces 
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

#Concerting Original Image to Gray scale to detect the face 
img = cv.imread('Testing Photos/1.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

face_rect = haar_cascade.detectMultiScale(gray,1.1,4)

# Drawing Rectangle Around the detected face and displaying text label of the person whose image it is
for (x,y,w,h) in face_rect:
  face_roi = gray[y:y+h,x:x+w]
  # Tesing Now 
  label, confidence  = face_recognizer.predict(face_roi)
  cv.putText(gray,str(p[label]),(x,y-20),cv.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),thickness=2)
  cv.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Image',gray)
cv.waitKey(0)


   
