import cv2
import numpy
 
picture=cv2.imread("kids.jpg")

picturePart=picture[50:150,300:400]

picture[0:100,0:100]=picturePart

picture[400:450,300:350]=(0,150,255)
cv2.imshow("23 Nisan", picture)
cv2.imshow("23 Nisan pitcure part", picturePart)


cv2.waitKey(0)
cv2.destroyAllWindows()