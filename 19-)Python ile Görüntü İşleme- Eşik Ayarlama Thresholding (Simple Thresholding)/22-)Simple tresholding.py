import cv2

picture=cv2.imread("image 1.jpg",0) #threshold işlemi uygulacağımız resmin gri tonunda olması lazım bu yüzden resmi okurken
#gri tonuna çeviriyoruz

ret,thresh1=cv2.threshold(picture,127,255,cv2.THRESH_BINARY)#threshold komutunda 1. değişken kaynağımızı
#2. değişkene verdiğimiz değerin altında kalan piksellerin değerini 0 a yuvarlayıp siyah olmasını sağlıyor
#3. değişkene verdiğimiz değer ise 2. değişkene verdiğimiz değerden yüksek değere sahip piksellerin değeri oluyor yani
#piksel değerleri 127 nin altında olan piksellerin yeni değeri 0 iken 127 den yüksek değere sahip piksellerin yeni değeri
#255 oluyor (resim iki kanallı olduğu için piksellerin tek değeri var) 4. değişken ise uygulamak istediğimiz threshold yöntemi

ret,thresh2=cv2.threshold(picture,127,255,cv2.THRESH_BINARY_INV)#cv2.THRESH_BINARY_INV flagi yukarıdaki flagde (cv2.THRESH_BINARY)
#oluşan değerlerin tam tersini oluşturup bize çıktı olarak veriyor

ret,thresh3=cv2.threshold(picture,127,255,cv2.THRESH_TRUNC)

ret,thresh4=cv2.threshold(picture,127,255,cv2.THRESH_TOZERO)

ret,thresh5=cv2.threshold(picture,127,255,cv2.THRESH_TOZERO_INV)

#yapacağımız işleme göre uygulayacağımız thresholdingler değişebilir açıklaması olmayan thresholdinglerde resimlere
#bakarak ne işe yaradığını anlayabilirsin

cv2.imshow("original picture",picture)
cv2.imshow("thresh1 picture",thresh1)
cv2.imshow("thresh2 picture",thresh2)
cv2.imshow("thresh3 picture",thresh3)
cv2.imshow("thresh4 picture",thresh4)
cv2.imshow("thresh5 picture",thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()