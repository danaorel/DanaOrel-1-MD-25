def task1():
    import os
    from PIL import Image
    before = "/Users/store78/Desktop/uni/python/before"
    after = "/Users/store78/Desktop/uni/python/after"
    if not os.path.exists(after):
        os.makedirs(after)
    def process_image(inp, outp):
        image = Image.open(inp)
        resized = image.resize((200, 200))
        resized.save(outp)
    for root, dirs, files in os.walk(before):
        for name in files:
            inp = os.path.join(root, name)
            outp = os.path.join(after, name)
            process_image(inp, outp)
#task1()
def task2():
    import os
    from PIL import Image
    before = "/Users/store78/Desktop/uni/python/before"
    after = "/Users/store78/Desktop/uni/python/after"
    if not os.path.exists(after):
        os.makedirs(after)
    def process_image(inp, outp):
        image = Image.open(inp)
        resized = image.resize((200, 200))
        resized.save(outp)
    for name in os.listdir(before):
        if name.endswith(".jpg") or name.endswith(".png"):
            inp = os.path.join(before, name)
            outp = os.path.join(after, name)
            process_image(inp, outp)
#task2()
def task3():
    total = 0
    with open('/Users/store78/Desktop/uni/python/products.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        print("Нужно купить:")
        for row in reader:
            product, k, price = row
            cost = int(k) * int(price)
            total += cost
            print(f"{product} - {k} шт. за {price} руб.")
    print(f"Итоговая сумма: {total} руб.")
task3()