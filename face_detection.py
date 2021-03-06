import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread('prac-1.jpg') # uncomment this to use face detection on image
cap = cv2.VideoCapture(0)
while True:
    _,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for(x, y, w, h) in faces:
        cv2.rectangle(img,(x,y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('image', img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        #ESC key to stop
        break
cap.release()
