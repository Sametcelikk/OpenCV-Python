import cv2

picture=cv2.imread("image 4.png",0)


#simple threshold
ret,thresh1=cv2.threshold(picture,160,255,cv2.THRESH_BINARY)

#adaptive thresholding
thresh2=cv2.adaptiveThreshold(picture,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#adaptive thresholding tüm resme aynı anda etki etmekten ziyade bizim belirlediğimiz alana o alandaki yoğunluğa göre
#etki uygular 1. değişkende kaynağı 2. değişkende maks değeri 3. değişkende adaptive thresholding çeşidini
#4. değişkende thresholding yöntemini 5. ve 6. değişkende ise meaning yönteminde kullandığımız yöntemi kullandığımız
#için kaça kaçlık alanların yoğunluğunu alacağımızı belirliyoruz

thresh3=cv2.adaptiveThreshold(picture,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#burda ise yoğunluğu mean yöntemi ile değil de gauss yöntemiyle aldık değişkenlerin işlevleri aynı



cv2.imshow("original picture ",picture)
cv2.imshow("simple threshold ",thresh1)
cv2.imshow("adaptive thresholding mean",thresh2)
cv2.imshow("adaptive threholding gaussian",thresh3)


cv2.waitKey(0)
cv2.destroyAllWindows()