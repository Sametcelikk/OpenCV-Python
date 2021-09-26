import cv2
import numpy

picture=cv2.imread("sametcelik.png")


kernel=numpy.ones((5,5),numpy.uint8)

opening=cv2.morphologyEx(picture,cv2.MORPH_OPEN,kernel)#opening komutu resme erosion ardından dilation işlemi uygular
#Opening olayını cv2.morphologyEx komutuyla yaparız gürültülü resimlerde kullanmak mantıklı olanıdır
#1. değişken kaynağımızı 2. değişken hangi morfolojik işlemi uyguluyacağımzıı (cv2.MORPH_OPEN yazarak opening
#işlemi uygulamak istediğimizi belirttik) 3. değişken ise kernelimizi belirliyor

closing=cv2.morphologyEx(picture,cv2.MORPH_CLOSE,kernel)#closing komutu openingin tam tersidir yani önce dilation işlemi
#ardından erosion işlemi uygular bu komutu gürültülü resimlerde kullanmak mantıksızdır. Bu komutu kesikli eksikli
#resimlerde kullanmak en mantıklısıdır
#1. değişken kaynağımızı 2. değişken hangi morfolojik işlemi uygulayacağımızı (cv2.MORPH_CLOSE yazarak closing
#işlemi uygulamak istediğimizi belirttik) 3. değişken ise kernelimizi belirlememizi sağlar
#bu işlem gürültülü resimlerde bir işe yaramıyacaktır

gradient=cv2.morphologyEx(picture,cv2.MORPH_GRADIENT,kernel) #gradient komutu dilation işlemi uygulanmış resimden
#aynı görselin erosion işlemi uygalınmış halini çıkartır
#1. değişken kaynağımızı 2. değişken hangi morfolojik işlemi uygulayacağımızı (cv2.MORPH_GRADIENT yazarak gradyant
#işlemi uygulamak istediğimizi belirttik) 3. değişken ise kernelimizi belirlememizi sağlar

tophat=cv2.morphologyEx(picture,cv2.MORPH_TOPHAT,kernel)#tophat komutu orijinal resmimizden opening işlemi uygulanmış
#resmimizi çıkartmamızı sağlar.Yani ön plandaki nesneyi kaldırıp arka plandaki nesnelerin kalmasını sağlar
#1. değişken kaynağımızı 2. değişken hangi morfolojik işlemi uygulayacağımızı (cv2.MORPH_TOPHAT yazarak tophat
#işlemi uygulamak istediğimizi belirttik) 3. değişken ise kernelimizi belirlememizi sağlar



cv2.imshow("original picture",picture)
cv2.imshow("opening picture",opening)
cv2.imshow("closing picture",closing)
cv2.imshow("gradient picture",gradient)
cv2.imshow("tophat picture",tophat)




cv2.waitKey(0)
cv2.destroyAllWindows()