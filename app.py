import cv2

file = "frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(file)

webcam = cv2.VideoCapture(0)

while True:
    (_, imagen ) = webcam.read()
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(imagen, (x,y), (x+w, y+h), (0,255,0), 2)
    
    cv2.imshow('Reconocimiento', imagen)

    key = cv2.waitKey(10)
    if key == 27:
        break