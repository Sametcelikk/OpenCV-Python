import cv2
import numpy

picture = cv2.imread("wolf.jpg")
cv2.imshow("samet's pitcure", picture)

print(picture[(230, 80)])  # konumu belirtilen pikselin BGR değerlerini gösterir

cv2.waitKey(0)
cv2.destroyAllWindows()
