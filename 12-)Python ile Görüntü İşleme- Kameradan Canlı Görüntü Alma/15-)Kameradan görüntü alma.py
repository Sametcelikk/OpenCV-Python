import cv2
import numpy


camera=cv2.VideoCapture(0)#bu parametreye 0 yazarsak kendi bilgisayarımın kamerasını 1 yazarsak usb ile taktığımız
#kamerayı 2 yazarsak belirlediğimiz videoyu almasını sağlar

while True:
    ret,image=camera.read() #ret komutuyla kameranın çelışıp çalışmadığını kontrol ettik read komutuyla kameradaki
    #görüntüyü alıp image değişkenine atadık(kameradan aslında video deiğl resim alıyoruz bu döngü sayesinde o resimleri
    #birleştirip video haline getitiriyoruz)
    cv2.imshow("Camera",image)

    if cv2.waitKey(30) & 0xFF == ord("q"):#waitkey komutu ile kaç milisaniyede bir fotoğraf çekileceğini belirliyoruz
    #0xFF ise girdi almamzı sağlıyor ve o değer q ya eşitse döngüyü kırıyor ve görüntü alma işlemi sonlanıyor
        break

camera.release()#relase komutu ile döngüden çıktıktan sonra kameradan görüntü alma işlemini sonlandırıyoruz

cv2.destroyAllWindows()

