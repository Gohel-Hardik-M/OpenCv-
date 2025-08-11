import cv2 as cv
import os
import numpy as np 

people = []
for i in os.listdir(r'Training Photos'):
  people.append(i)

DIR = 'Training Photos/'

# Cascader Classifier TO detect Face in the image 
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# TO train the model we need the features and labels of the person -->and the face_roi of the image as feature
features = []
lables = []

def create_train():
  for person in people:
    path = os.path.join(DIR, person)
    label = people.index(person)
    for img in os.listdir(path):
      img_path = ps.path.join(path,img)
      img_array= cv.imread(img_path)
      gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
      faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbora = 4)
      for (x,y,w,h) in faces_rect :
        faces_roi = gray[y:y+h,x:x+w]
        features.append(faces_roi)          # appending each faces_roi for each image in features list 
        labels.append(label)

create_train()
print(f"length of features = {len(features)}")
print(f"length of labels = {len(labels)}")

# Training Model with the labels and the features we got
features = np.array(features,dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)

# Saving OUr Trained Model in yml format to use in recognizing image of the person 
face_recognizer.save('face_trained.yml')

# ALso saving our features and labels in the form of numpy array (npy) if we wanna use it later on then we can easily so 
np.save('features.npy',features)
np.save('labels.npy',labels)
