import cv2
import numpy

picture1=cv2.imread("1.png")
picture2=cv2.imread("2.png")
bitwiseAnd=cv2.bitwise_and(picture1,picture2) #bitwise_and operatörü siyahları 0 beyazları 1 olarak düşünürsek
#bunları and komutunun yaptığı işleme tabi tutuyor ve beyaz üstüne beyaz gelmediği takdirde orayı beyaza boyamıyor
bitwiseOr=cv2.bitwise_or(picture1,picture2) #siyahları 0 beyazları 1 olarak düşünürsek or (ya da) işlevi görür
bitwiseXOR=cv2.bitwise_xor(picture1,picture2) #xor operatörü inputların ikisi de 0 ya da ikisi de 1 se
#0 değerini döner inputlar farklı ise 1 değerini döner
bitwiseNot=cv2.bitwise_not(picture2) #burada tek giriş yapıyoruz bu operatör 1 leri 0 a 0 ları 1 e çeviriyor

cv2.imshow("first picture",picture1)
cv2.imshow("second picture",picture2)
cv2.imshow("bitwise and picture",bitwiseAnd)
cv2.imshow("bitwise or picture",bitwiseOr)
cv2.imshow("bitwise XOR picture",bitwiseXOR)
cv2.imshow("bitwise not picture",bitwiseNot)



cv2.waitKey(0)
cv2.destroyAllWindows()