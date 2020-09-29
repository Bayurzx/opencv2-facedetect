import cv2

face_cascade = cv2.CascadeClassifier("front_face.xml")

img = cv2.imread("news.jpg") #Greyscale has higher accuracy with fac detection
gray_pic= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_pic,
scaleFactor=(1.15),
minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),3)

print(type(faces))
print(faces)

resized = cv2.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("Gray",resized)
cv2.waitKey(7000)
cv2.destroyAllWindows()
