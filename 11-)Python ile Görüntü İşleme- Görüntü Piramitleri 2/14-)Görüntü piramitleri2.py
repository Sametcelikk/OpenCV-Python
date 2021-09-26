import cv2
import numpy

picture=numpy.zeros((300,300,3),dtype="uint8")#zeros fonksiyonunu kullanarak bir resim oluşturduk
#ilk değişkende resmin yükseklik genişlik ve kanal sayısını belirledik ikinci değişkende ise data tipini belirledik
cv2.imshow("a",picture)

print(picture)

cv2.waitKey(0)
cv2.destroyAllWindows()