import cv2

cam = cv2.VideoCapture(0)  #kamerayı çalıştır
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 400) #kameranın boyunu ayarla
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320) #kameranın genişliğini ayarla


ret,goruntu = cam.read() #kamerayı oku(kamerada görünün fotoğraf) ret: kameranın çalışıp çalışmadığını kontrol etme

cv2.imshow("Goruntu", goruntu) #görüntüyü göster




