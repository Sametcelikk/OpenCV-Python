import cv2
import numpy

picture=cv2.imread("joker.jpg")

picture[50, 30]=[255, 255, 255] #belirlediğimiz pikselin BGR değerlerini değiştirdik

for i in range(200):
    picture[i, i]=[255, 255, 255]
    for a in range(i):
        picture[i, a]=[255, 255, 255]

cv2.imshow("joker", picture)

cv2.waitKey(0)
cv2.destroyAllWindows()