import cv2
import numpy

picture=cv2.imread("Natalie Portman.jpg")

greyPicture=cv2.cvtColor(picture,cv2.COLOR_BGR2GRAY)#burada resim değişkenini alıp cv2.COLOR_BGR2RGB komutu ile
#resmi grileştirdik

cv2.imshow("Normal picture",picture)
cv2.imshow("Grey picture",greyPicture)


print("Normal picture= ",picture.shape,picture.size)
print("Grey pictur= ",greyPicture.shape,greyPicture.size)




cv2.waitKey(0)
cv2.destroyAllWindows()