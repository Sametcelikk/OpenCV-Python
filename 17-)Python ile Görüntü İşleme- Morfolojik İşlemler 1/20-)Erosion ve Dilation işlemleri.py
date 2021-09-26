import cv2
import numpy

picture=cv2.imread("sametcelik.png")

kernel=numpy.ones((5,5),numpy.uint8) #burada deliation işlemi için kernel oluşturuyoruz


erosion=cv2.erode(picture,kernel,iterations=1)#erode komutuyla resmin ön planını ve gürültüleri daralttık.
#1. parametrede hangi resimde işlem yapacağımızı 2. parametrede kernelimi 3. parametrede ise daraltmanın boyutunu
#ayarladık. Gürültülü resme bu işlemi uyguladıktan sonra dilate komutuyla resmimizi tekrar genişletip gürültüden
#giderilmiş bir resim oluşturmak en mantıklısıdır.

dilation=cv2.dilate(picture,kernel,iterations=1) #deliate komutuyla ggürültüleri ve öm plandaki görüntüleri genişlettik
#1. parametrede hangi resimde işlem yapacağımızı 2. paremetrede kerneli 3. parametrede ise genişletmenin
#boyutunu belirledik
#gürültülü resme dilation işlemi yapmak mantıklı olmaz. Bu işlem gürültüyü giderdikten sonra yapılmalıdır
#resmimiz kesikliyse ve eksik kısımları varsa ona direkt dilation işlemi uygulamak mantıklıdır

erodeAndDilate=cv2.dilate(erosion,kernel,iterations=1) #burada erode işlemi uygulanmış resme dilate komutunu uygulayarak
#tekrar genişlettik ve gürültüden arındırılmış bir resim elde ettik
#yukarıda da yazdığım gibi gürültülü resimlerde erosion üstüne dilation işlemi yapmak en mantıklı olanıdır

cv2.imshow("Original picture",picture)
cv2.imshow("Dilation picture",dilation)
cv2.imshow("erosion picture",erosion)
cv2.imshow("erode and dilate pitcure",erodeAndDilate)

cv2.waitKey(0)
cv2.destroyAllWindows()