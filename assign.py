import cv2
import glob

imgs = glob.glob("*.jpg")

for image in imgs:
    img=cv2.imread(image,0)
    print(img.shape)
    re = cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(10)
    cv2.destroyAllWindows()
    cv2.imwrite("img_rezz"+image,re)
