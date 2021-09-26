import cv2

picture=cv2.imread("d.png")


meanFilter1=cv2.blur(picture,(3,3)) #blur komutu ile hangi fotoğrfa kaça kaçlık bir işlem yapacağımızı belirliyoruz
#blur komutu kaça kaçlık piksel alanı belirlersek o piksellerin renk değerlerinin ortalamasını alıp merkezdeki
#piksele o değeri atıyor buna mean filter işlemi deniyor
meanFilter2=cv2.blur(picture,(5,5))
meanFilter3=cv2.blur(picture,(7,7))

medianFilter1=cv2.medianBlur(picture,3) #median komutu hangi fotoğrafa kaça kaçlık işlem yapacağımızı belirliyoruz
#median blur komutu belirlediğimiz alandaki piksellerin medyanını yani ortasındaki değeri alıp piksellerin merkezine
#o değeri atar
medianFilter2=cv2.medianBlur(picture,5)
medianFilter3=cv2.medianBlur(picture,7)

gaussFilter1=cv2.GaussianBlur(picture,(3,3),0)
gaussFilter2=cv2.GaussianBlur(picture,(5,5),0)
gaussFilter3=cv2.GaussianBlur(picture,(7,7),0)

cv2.imshow("original picture",picture)
cv2.imshow("mean filter 3*3",meanFilter1)
cv2.imshow("mean filter 5*5",meanFilter2)
cv2.imshow("mean filter 7*7",meanFilter3)

cv2.imshow("median filter 3*3",medianFilter1)
cv2.imshow("median filter 5*5",medianFilter2)
cv2.imshow("median filter 7*7",medianFilter3)

cv2.imshow("gauss filter 3*3",gaussFilter1)
cv2.imshow("gauss filter 5*5",gaussFilter2)
cv2.imshow("gauss filter 7*7",gaussFilter3)



cv2.waitKey(0)
cv2.destroyAllWindows()