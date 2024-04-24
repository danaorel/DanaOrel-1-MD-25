from PIL import Image, ImageDraw, ImageFont
def task1():
    img = Image.open('Z:/1-МД-25/Орел Дана/открытка.jpg')
    print(img.size)
    cropped = img.crop((100, 600, 697, 900))
    cropped.show()
    cropped.save('Z:/1-МД-25/Орел Дана/обрезанная_открытка.jpg')
#task1()

def task2():
    postcards = {'День Рождения' :'Z:/1-МД-25/Орел Дана/открытка.jpg', '8 марта':'Z:/1-МД-25/Орел Дана/8march.jpg', '23 февраля':'Z:/1-МД-25/Орел Дана/23feb.jpg'}
    holiday = input('Введите праздник ')
    if holiday in postcards:
            n = str(postcards[holiday])
            #print(n)
            img = Image.open(n)
            img.show()
task2()
