import cv2


camera=cv2.VideoCapture(0)

width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))#bu satırda kameramızın çerçevesinin genişliğini int biçimde aldık
height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))#bu satırda kameramın çerçevesinin yüksekliğini int biçimde aldık

print(width,height)

fourcc=cv2.VideoWriter_fourcc(*"MPV4")#bu satırda cv2.VideoWriter_fourcckomutuyla videomuzun hangi formatta kayıt
#edileceğini belirleyip fourcc değişkenine atadık

writer=cv2.VideoWriter("kayit.mp4",fourcc,17,(width,height))#1. değişkende kayıt dosyamızın ismini 2. değişkende
#kayıt formatımızı (üstte kayıt formatını cv2.VideoWriter_fourcc komtuyla fourcc değişkenine atadık) 3. değişkende
#bir saniyede kaç frame kaydedeceğini (FPS) 4. değişkende kayıt dosyamızın genişlik ve yüksekliğini belirleyip bir değişkene
#atıyoruz. Videomuz şu an kaydedilmiyor sadece kayıt işleminin nasıl yapılacağı bilgilerini bir değişkene atadık

while True:
    ret,image=camera.read()
    image=cv2.flip(image,1)#kameradan alınan görüntünün yatay veya dikey çevirilmesini sağlar
    #0-> x ekseninde yani dikey 1-> y ekseninde yani yatay -1-> ise hem dikey hem de yatay eksene görünntüyü çevirir
    writer.write(image)#kayıt işlei bu satırda .write komutuyla yapılıyor kayıt özelliklerini writer değişkeninden
    #alıyor
    cv2.imshow("camera",image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
writer.release()#kamerarla işimiz bittiğinde onu nasıl serbest bırakıyorsak kayıt işlemini de aynı şekilde serbest
#bırakmamız gerk
cv2.destroyAllWindows()