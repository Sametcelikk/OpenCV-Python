import cv2
import numpy

picture1=cv2.imread("emel sayin.jpg")
picture2=cv2.imread("turkan soray.jpg")

print(f"{picture1[100,200]}+{picture2[300,430]}={picture1[100,200]+picture2[300,430]}")
#yukarideki satırda verilen biksellerin (y,x) bgr değerlerini toplayıp yeni bir değer oluşturdu

cv2.imshow("Emel Sayin's picture",picture1)
cv2.imshow("Turkan Soray's picture",picture2)


cv2.waitKey(0)
cv2.destroyAllWindows()