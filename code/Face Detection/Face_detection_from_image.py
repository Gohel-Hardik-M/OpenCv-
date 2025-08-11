import cv2 as cv
import numpy as np 

# Classifier
haar_cascase = cv.CascadeClassifier('haar_face.xml')

# to detect the face in any image firstly we need to convert the original image into a GRAY scale image
img = cv.imread('')
