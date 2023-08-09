from app import app
from app.controller import count_pixel_image_controller, count_rgb_image


@app.route('/')
def index():
    return 'hello flask'


@app.route('/img_controller')
def img():
    return count_pixel_image_controller.testImgController()


@app.route('/file-upload', methods=['POST'])
def fileupload():
    return count_pixel_image_controller.testImgController()


@app.route('/file-upload-rgb', methods=['POST'])
def fileupload2():
    return count_rgb_image.calculate_average_rgb()
