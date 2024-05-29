#I name you bex!

import cv2
from random import randrange

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')
webcam = cv2.VideoCapture(0)

print("-------------------------!Q for quit!-------------------------")

while True:

    successful_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = face_detector.detectMultiScale(grayscaled_img)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 254), 2)
        the_face = frame[y:y+h, x:x+w ]
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)
        smile_coordinates = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.9, minNeighbors=33)
        if len(smile_coordinates) > 0:
            cv2.putText(frame, 'smiling', (x, y+h+30), fontScale=2, fontFace=cv2.FONT_HERSHEY_PLAIN, color=(0, 0, 0))

    print(face_coordinates)

    cv2.imshow('Face detection ... (emotions!)', frame)

    key = cv2.waitKey(1)
    if key==81 or key==113:
        break

webcam.release()

print("-------------------------!Code completed!-------------------------")
