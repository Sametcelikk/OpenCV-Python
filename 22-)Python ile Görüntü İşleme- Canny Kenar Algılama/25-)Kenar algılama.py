import cv2
import numpy

#kenar algışama işlemleri gri resim üzreinde yapılır

picture=cv2.imread("groot2.jpg")
grayPicture=cv2.cvtColor(picture,cv2.COLOR_BGR2GRAY)
blur=cv2.medianBlur(grayPicture,7)
#yukarıda resmi kenar algılama yapmak için en uygun hale getirdim. gri hale çevirip blur işlemi yaparak kenar hatları
#daha belirgin hale getirdim


#canny algoritması:
def AutoCanny(blur,sigma=0.33):
    median=numpy.median(blur) #bu satır görüntüdeki piksel yoğunluklarının medyanını hesaplamamızı sağlıyor
    lower=int(max(0,(1.0-sigma)*median)) #bu ve alt satırda al ve üst eşik değerlerini resme göre otomatik
    upper=int(min(255,(1+sigma)*median)) #belirliyoruz
    canny=cv2.Canny(blur,lower,upper) #1. değişkende hangi resmin kenarlarını bulacağımızı 2. değişkende alt
    #3. değişkende ise üst eşik değeri belirliyoruz

    return canny

cv2.imshow("original picture",picture)
cv2.imshow("grey picture",grayPicture)
cv2.imshow("blurred picture",blur)
cv2.imshow("canny picture",AutoCanny(blur))

cv2.waitKey(0)
cv2.destroyAllWindows()


#yukarıdaki sigma ve blur ayarları groot2.jpg resmine göre yapılmıştır başka bir resimde bu ayarları o resme göre
#yapılmalıdır yoksa bu kadar verimli bir sonuç elde edemeyebiliriz