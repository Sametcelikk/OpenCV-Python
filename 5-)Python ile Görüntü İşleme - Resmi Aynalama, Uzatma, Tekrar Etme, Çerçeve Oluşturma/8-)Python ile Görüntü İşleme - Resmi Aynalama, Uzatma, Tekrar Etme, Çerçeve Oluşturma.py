import cv2
import numpy

picture=cv2.imread("adileNasit.jpg")

mirrorImage=cv2.copyMakeBorder(picture,75,75,100,100,cv2.BORDER_REFLECT) #resmi aynalama
#1. parametre kullanacağımız resim 2.,3.,4.,5. parametre ölçekler ve son parametre de yapmak istediğimiz işlem
#2. parametre üst 3. parametre alt 4. parametre sol 5. parametre sağ sınırı belirler

strechedImage=cv2.copyMakeBorder(picture,120,120,100,100,cv2.BORDER_REPLICATE) #resmi uzatma

repeatedImage=cv2.copyMakeBorder(picture, 150, 150, 150, 150, cv2.BORDER_WRAP) #resmi aynalama

borderImage=cv2.copyMakeBorder(picture,50,50,50,50,cv2.BORDER_CONSTANT,value=(0,0,255)) #resme çerçeve ekler
#value değeri çerçevemizin rengini belirlememizi sağladı

cv2.imshow("Mirror Adile Nasit's Picture",mirrorImage)
cv2.imshow("Streched Adile Nasit's Picture",strechedImage)
cv2.imshow("Repeated Adile Nasit's Picture",repeatedImage)
cv2.imshow("Bordered Adile Nasit's Picture",borderImage)


cv2.waitKey(0)
cv2.destroyAllWindows()