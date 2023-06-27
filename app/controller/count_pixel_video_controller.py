import cv2
import numpy as np

def count_pixels(image):
    # Mengubah gambar ke dalam mode HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Membuat mask dengan warna yang ingin dideteksi
    mask = cv2.inRange(hsv_image, greenLower, greenUpper)
    
    # Menghitung jumlah piksel yang memiliki warna yang sama dengan yang dideteksi
    pixel_count = cv2.countNonZero(mask)
    
    return pixel_count

# Mengakses kamera
cap = cv2.VideoCapture(0)

greenLower = (0, 0, 142)
greenUpper = (135, 147, 198)

while True:
    # Membaca frame dari kamera
    ret, frame = cap.read()
    
    # Mendapatkan jumlah piksel dengan warna yang ingin dideteksi
    count = count_pixels(frame)
    
    # Menampilkan jumlah piksel pada layar
    cv2.putText(frame, 'Count: ' + str(count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Menampilkan frame
    cv2.imshow('Frame', frame)
    
    # Tombol 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepaskan kamera dan menutup jendela tampilan
cap.release()
cv2.destroyAllWindows()