import cv2
import numpy

picture=numpy.zeros((300,300,3),dtype="uint8")

cv2.line(picture,(50,50),(100,100),(0,0,255),3)#line komutu ile çizgi çekiyoruz. 1. parametrede hangi esme çizgi
#çekeceğimizi 2. parametrede çizginin hangi pikselden başlıyacağını 3. parametrede çizginin hangi piksele kadar
#gideceğini 4. parametrede çizginin BGR değerlerini 5. parametrede ise çizginin kalınlığını belirliyoruz

cv2.circle(picture,(150,150),25,(0,255,0),2)#circle komutu ile daire çiziyoruz. 1. parametrede hangi resime daire
#cizeceğimzi 2. parametrede dairenin merkezinin hangi pikselde olacağını 3. parametrede dairenin yarıçapını
#4. parametrede dairenin BGR değerlerini 5. parametrede ise dairenin kalınlıpını belirliyoruz

cv2.putText(picture,"SAMET CELIK",(10,250),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)#putText komutu ile yazı yazıyoruz
#1. parametrede hangi resime yazı yazacağımızı 2. parametrede yazının hangi pikselden başlıyacağını
#3. parametrede yazının fontunu 4. parametrede yazının büyüklüğünü 5. parametrede yazının BGR değerlerini
#6. parametrede yazının kalınlığını belirliyoruz

cv2.imshow("example1",picture)

cv2.waitKey(0)
cv2.destroyAllWindows()