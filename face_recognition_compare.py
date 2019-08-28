# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:29:46 2019

@author: vp999274
"""

import face_recognition
import cv2
known_image = face_recognition.load_image_file("18.jpg")
unknown_image = face_recognition.load_image_file("18.jpg")
cv2.imshow("result", known_image)
cv2.waitKey(0)
 
biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
 
results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
print(results)