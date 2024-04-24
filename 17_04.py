from PIL import Image, ImageFilter
import os
def task1():
    img = Image.open("0.jpg")
    print(f"Размер изображения: {img.size}")
    print(f"Формат изображения: {img.size}")
    print(f"Цветовая модель: {img.size}")
task1()

def task2():
    img = Image.open("0.jpg")
    small = img.resize((img.width // 3, img.height//3))
    small.save("small.jpg")
    horizontal = image.transpose(Image.FLIP_LEFT_RIGHT)
    horizontal.save("horizontal.jpg")
    vertical = image.transpose(Image.FLIP_TOP_BOTTOM)
    vertical.save("vertical.jpg")
task2()

def task3():
    os.makedirs("filter", exist_ok=True)
    image_files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for filename in image_files:
        image = Image.open(filename)
        sharpened = image.filter(ImageFilter.SHARPEN)
        new_filename = os.path.join("filter", f"sharpen{filename}")
        sharpened.save(new_filename)
task3()