import cv2
import numpy

picture=cv2.imread("Natalie Portman.jpg")

enlargedPicture=cv2.pyrUp(picture)#pyrUp fonksiyonu resmin yüksekliğini ve genişliğini iki katına yükseltir

scaledDownPicture=cv2.pyrDown(picture)#pyrDown fonksiyonu resmin yüksekliğini ve genişliğini yarısına düşürür

cv2.imshow("Original Picture",picture)
cv2.imshow("New Picture",enlargedPicture)
cv2.imshow("Scaled Down Picture",scaledDownPicture)

cv2.waitKey(0)
cv2.destroyAllWindows()