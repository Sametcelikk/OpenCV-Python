import cv2
import numpy as np

picture = cv2.imread("logo.jpg", 0)  # imread komutu ile resmimi pitcure değişkenine atatdım
# eğer ikince parametreyi 0 yaparsam renkleri kullanmayıp sadece siyah beyaz alıcak

cv2.imshow("samet's pitcure", picture)  # imshow komutu resmi okumamızı açmamızı ve o resime ilk parametredeki gibi
# isim vermemizi sağlar


cv2.imwrite("logo2.jpg", picture)  # değişkenimdeki resmi hangi dizindeyse oraya kaydetmesini sağlar


cv2.waitKey(0)  # kapanışta kullanmamız gereken temel iskeletlerden birisi
cv2.destroyAllWindows()  # temel iskeletin bir diğer parçasıdır. Çarpıya bastığımızda opencv ile
# alakalı tüm pencerelerin kapanmasını sağlar
