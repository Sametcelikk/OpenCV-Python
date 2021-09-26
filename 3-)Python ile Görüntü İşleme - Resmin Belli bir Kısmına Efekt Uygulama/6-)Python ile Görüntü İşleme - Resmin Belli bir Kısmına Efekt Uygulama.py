import cv2
import numpy

picture=cv2.imread("people.jpg")
picture[150:200, 340:500, 0]=255 #o yazıp maviye erişim sağladık ve değerini 255 yaptık yeşil için 1 kırmızı için 2
picture[150:200, 340:500, 1]=255 #ilk parametre dikey ikinci parametre yatay sınırları belirliyor
picture[150:200, 340:500, 2]=20

cv2.imshow("Kemal Sunal Photo", picture)





cv2.waitKey(0)
cv2.destroyAllWindows()