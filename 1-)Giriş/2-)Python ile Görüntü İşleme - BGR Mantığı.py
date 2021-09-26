import cv2
import numpy as np

picture = cv2.imread("birdPitcure.jpg")

cv2.imshow("samet's pitcure", picture)

print(picture)

cv2.waitKey(0)

cv2.destroyAllWindows()
