import cv2
import numpy as np
from app import response, app, uploadconfig
from flask import request
import os
import uuid
from werkzeug.utils import secure_filename


def calculate_average_rgb():
    try:
        judul = request.form.get('judul')
        if 'file' not in request.files:
            return response.badRequest([], "file not found")

        file = request.files['file']

        if file.filename == '':
            return response.badRequest([], "file tidak tersedia")

        if file and uploadconfig.allowed_file(file.filename):
            uid = uuid.uuid4()
            filename = secure_filename(file.filename)
            renamefile = "Flask-"+str(uid)+filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))
            # pixels = count_pixels('upload/'+renamefile)
            image = cv2.imread('upload/'+renamefile)
            height, width, _ = image.shape
            total_r = 0
            total_g = 0
            total_b = 0

            total_pixels = width * height

            for y in range(height):
                for x in range(width):
                    b, g, r = image[y, x]
                    total_r += r
                    total_g += g
                    total_b += b

            average_r = total_r // total_pixels
            average_g = total_g // total_pixels
            average_b = total_b // total_pixels

            # return average_r, average_g, average_b
            return response.success(
                {
                    'r': str(average_r),
                    'g': str(average_g),
                    'b': str(average_b)
                }, "Success upload file"
            )
        else:
            return response.badRequest([], "file tidak di ijinkan")
        # return response.success("controller running","success")
    except Exception as e:
        print(e)
        print("e")
