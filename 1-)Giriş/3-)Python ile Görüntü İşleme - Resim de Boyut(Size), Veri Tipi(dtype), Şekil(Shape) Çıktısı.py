import cv2
import numpy as np

picture = cv2.imread("birdPitcure.jpg")
picture2 = cv2.imread("birdPitcure.jpg", 0)

cv2.imshow("samet's pitcure", picture)


print(picture.size)#resimin boyutunu öğrenmiş oluyoruz
print(picture.dtype) #resmimizin data türünü öğrenmemizi sağlar
print(picture.shape) #resmin yüksekliğini genişliğini  ve kaç kanal kullandığını öğrenmemizi sağlar
print("--------------")
print(picture2.size)
print(picture2.dtype)
print(picture2.shape)

cv2.waitKey(0)

cv2.destroyAllWindows()
