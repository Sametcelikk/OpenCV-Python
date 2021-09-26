import cv2

#otsu bir değer seçme zorunluluğunu ortadan kaldırır değeri kendisi belirler

picture=cv2.imread("image 1.jpg",0)

#simple thresholding
ret1,thresh1=cv2.threshold(picture,127,255,cv2.THRESH_BINARY)

#otsu thresholding
ret2,thresh2=cv2.threshold(picture,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#1. değişkende kaynağımızı
#2. ve 3. değişkenlerde sadece kullanılmasını istedğimiz bgr aralığını girdik eşik değerlerini girmdik
#4. parametrede cv2.THRESH_BINARY komutuna cv2.THRESH_OTSU ekleyerek otsu thresholding e çevirdik
#bu sayede eşik değerleri otomatik ayarlanacak

#Not:Simple ve otsu da iki çıktı döndürdüğümüz için iki tane değişken belirliyoruz (ret,thresh1)
#Adaptive thresholdingde ise tek değişken belirliyoruz

cv2.imshow("original picture",picture)
cv2.imshow("simple thresholding picture",thresh1)
cv2.imshow("otsu thresholding picture",thresh2)

#Not2:Bu threshold yöntemleri arassında en iyi diyebileceğimiz bir yöntem yok her bir threshold yöntemi kullanım alanına
#göre diğerinden daha iyi olabilir bu yüzden thresholding yöntemlerinin işlevlerini iyi bilmek lazım


cv2.waitKey(0)
cv2.destroyAllWindows()