import cv2
from app import response, app, uploadconfig
from flask import request
import os
import uuid
from werkzeug.utils import secure_filename

def upload():
    try:
        return response.success("t","te")
    except Exception as e:
        print(e)

def testImgController():
    try:
        judul = request.form.get('judul')
        if 'file' not in request.files:
            return response.badRequest([],"file not found")
        
        file = request.files['file']

        if file.filename == '':
            return response.badRequest([],"file tidak tersedia")
        
        if file and uploadconfig.allowed_file(file.filename):
            uid = uuid.uuid4()
            filename = secure_filename(file.filename)
            renamefile = "Flask-"+str(uid)+filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))
            pixels = count_pixels('upload/'+renamefile)
            return response.success(
                {
                    'judul': judul,
                    'pathname':renamefile,
                    'pixels':pixels
                },"Success upload file"
            )
        else:
            return response.badRequest([],"file tidak di ijinkan")
        # return response.success("controller running","success")
    except Exception as e:
        print(e)
    

def count_pixels(image):
    # Mengubah gambar ke dalam mode HSV
    hsv_image = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2HSV)
    
    # Menentukan rentang warna yang ingin dideteksi
    greenLower = (0, 0, 102)
    greenUpper = (226, 33, 255)
    
    # Membuat mask dengan warna yang ingin dideteksi
    mask = cv2.inRange(hsv_image, greenLower, greenUpper)
    
    # Menghitung jumlah piksel yang memiliki warna yang sama dengan yang dideteksi
    pixel_count = cv2.countNonZero(mask)
    
    return pixel_count

# # Load gambar
# image = cv2.imread('gambar.jpg')

# # Mendapatkan jumlah piksel dengan warna yang ingin dideteksi
# count = count_pixels(image)
# print("Jumlah piksel dengan warna yang ditentukan:", count)
