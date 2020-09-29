import cv2

img = cv2.imread("galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

img_rez = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy",img_rez)
cv2.imwrite("new galaxy.jpg",img_rez)
cv2.waitKey(00)
cv2.destroyAllWindows()
