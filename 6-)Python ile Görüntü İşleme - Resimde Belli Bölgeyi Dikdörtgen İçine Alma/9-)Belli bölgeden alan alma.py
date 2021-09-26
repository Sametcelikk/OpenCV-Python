import cv2
import numpy


picture=cv2.imread("hababam sinifi.png")

cv2.rectangle(picture,(470,580),(620,400),(0,255,0),2)#rectangle komutu dikdörtgen alan seçmemizi sağlıyor
#2. parametre sol alt köşeyi (x,y) 3. parametre sağ üst köşeyi (x,y) belirliyor 4. parametre çerçevenin rengini
#5. parametre çerçevenin kalınlığını belirliyor

cv2.imshow("picture",picture)




cv2.waitKey(0)
cv2.destroyAllWindows()