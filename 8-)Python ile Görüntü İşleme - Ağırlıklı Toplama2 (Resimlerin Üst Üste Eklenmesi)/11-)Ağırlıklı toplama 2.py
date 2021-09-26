import cv2
import numpy

picture1=cv2.imread("cem yilmaz.jpg")
picture2=cv2.imread("ozan guven.jpg")


cv2.imshow("Ozan Guven",picture2)
cv2.imshow("Cem Yilmaz",picture1)


total=cv2.add(picture1,picture2)#cv.add komutuyla resimleri üst üste koyup tüm bgr değerlerini topladık
#dikkat etmemiz gereken husus resimlerin en ve boy oranlarının aynı olmsı gerek

agirlikliToplama=cv2.addWeighted(picture1,0.7,picture2,0.3,0)#bu komutla hangi resimden yüzde kaç ağırlıkta
#kullanacağımızı belirliyoruz

cv2.imshow("new pitcure",total)
cv2.imshow("agirlikli toplam",agirlikliToplama)

cv2.waitKey(0)
cv2.destroyAllWindows()