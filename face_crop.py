# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:59:02 2019

@author: vp999274
"""

'''  
facechop.py

-Takes an image and detects a face in it.  
-For each face, an image file is generated
    -the images are strictly of the faces
'''

import cv2

def facechop(image):  
    facedata = "haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(facedata)

    img = cv2.imread(image)

    minisize = (img.shape[1],img.shape[0])
    miniframe = cv2.resize(img, minisize)

    faces = cascade.detectMultiScale(miniframe)

    for f in faces:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))

        sub_face = img[y:y+h, x:x+w]
        #face_file_name = "faces/face_" + str(y) + ".jpg"
        cv2.imwrite('face.jpg', sub_face)
        
        cv2.imshow("face", sub_face)
        cv2.waitKey(0)

    #cv2.imshow(image, img)

    return
  
facechop("18.jpg")
#cv2.waitKey(0)

"""
    while(True):
        key = cv2.waitKey(20)
        if key in [27, ord('Q'), ord('q')]: 
            break
"""            