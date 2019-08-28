import cv2
import sys

# Get user supplied values
imagePath = '18.jpg'
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    face_image=cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
face_crop = []
for f in faces:
    x, y, w, h = [ v for v in f ]
    cv2.rectangle(face_image, (x,y), (x+w, y+h), (255,0,0), 3)
    # Define the region of interest in the image  
    face_crop.append(image[y:y+h, x:x+w])

for face in face_crop:
    cv2.imshow('face',face)
    break;
    cv2.waitKey(0)
    
cv2.imshow("Faces found", image)
#cv2.imshow("Faces found", face_image)
cv2.waitKey(0)
