import cv2


def calculate_average_rgb(image_path):
    image = cv2.imread(image_path)
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

    return average_r, average_g, average_b


# Ganti 'nama_gambar.jpg' dengan nama gambar Anda
image_path = 'nama_gambar.jpg'
average_r, average_g, average_b = calculate_average_rgb(image_path)

print(f"Rata-rata RGB: ({average_r}, {average_g}, {average_b})")
