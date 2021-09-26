import cv2
import numpy

camera=cv2.VideoCapture(0)

while True:
    ret,image=camera.read()

    cv2.line(image,(0,0),(100,100),(0,0,255),2) #bu satırla videoma çizgi ekledim

    cv2.rectangle(image,(150,150),(250,250),(255,0,0),3) #bu satırla videoma dikdörtgen ekledim

    cv2.putText(image,("Samet's Video"),(300,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)#bu satırla videoma yazı ekledim

    cv2.circle(image, (150, 150), 25, (0, 255, 0), 2) #bu satırla videoma daire ekledim

    cv2.imshow("Camera",image)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()