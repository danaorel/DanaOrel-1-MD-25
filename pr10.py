def task1():
    import json
    with open('/Users/store78/Desktop/uni/python/products.json', 'r') as file:
        data = json.load(file)
    for product in data['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
#task1()
def task2():
    import json
    with open('/Users/store78/Desktop/uni/python/products.json', 'r') as file:
        data = json.load(file)
    for product in data['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
    new_product_name = input("Введите название: ")
    new_product_price = float(input("Введите цену: "))
    new_product_weight = int(input("Введите: "))
    new_product_available = input("Продукт в наличии?: ").lower() == 'да' #если вводят "да" возвращает true
    new_product = {
        "name": new_product_name,
        "price": new_product_price,
        "weight": new_product_weight,
        "available": new_product_available
    }
    data['products'].append(new_product)
    for product in data['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
#task2()
def task3():
    with open('/Users/store78/Desktop/uni/python/en-ru.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    ru_en_dict = {}
    for line in lines:
        english_word, russian_transl = line.strip().split(' - ')
        russian_words = [word.strip() for word in russian_transl.split(',')]
        for russian_word in russian_words:
            if russian_word in ru_en_dict:
                ru_en_dict[russian_word].append(english_word)
            else:
                ru_en_dict[russian_word] = [english_word]

    with open('/Users/store78/Desktop/uni/python/ru-en.txt', 'w', encoding='utf-8') as file:
        for russian_word in sorted(ru_en_dict.keys()):
            english_words = ', '.join(sorted(ru_en_dict[russian_word]))
            file.write(f"{russian_word} – {english_words}\n")
#task3()