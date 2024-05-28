def task1():
    class Restaurant:
        def __init__(self, name, cuisine_type):
            self.name = name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название: {self.name}")
            print(f"Кухня: {self.cuisine_type}")
        def open_restaurant(self):
            print(f"Ресторан {self.name} открыт!")

    class IceCreamStand(Restaurant):
        def __init__(self, name, cuisine_type):
            super().__init__(name, cuisine_type)
            self.flavors = []
        def flavors_menu(self):
            for flavor in self.flavors:
                print(flavor)
    ice_cream_stand = IceCreamStand("Кафе-мороженое", "Мороженое")
    ice_cream_stand.flavors = ["Ванильное", "Клубничное", "Шоколадное"]
    ice_cream_stand.describe_restaurant()
    ice_cream_stand.flavors_menu()
#task1()
def task2():
    class Restaurant:
        def __init__(self, name, cuisine_type):
            self.name = name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название: {self.name}")
            print(f"Кухня: {self.cuisine_type}")
        def open_restaurant(self):
            print(f"Ресторан {self.name} открыт!")
    class IceCreamStand(Restaurant):
        def __init__(self, name, cuisine_type, location, work_hours):
            super().__init__(name, cuisine_type)
            self.location = location
            self.work_hours = work_hours
            self.flavors = []
        def flavors_menu(self):
            for flavor in self.flavors:
                print(flavor)
        def location_and_hours(self):
            print(f"Локация: {self.location}")
            print(f"Рабочие часы: {self.work_hours}")
        def add_flavor(self, flavor):
            self.flavors.append(flavor)
            print(f"{flavor} мороженое добавлено.")
        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"{flavor} мороженое удалено.")
            else:
                print(f"{flavor} - такого вкуса нет.")
        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"{flavor} - в наличии.")
            else:
                print(f"{flavor} - нет в наличии.")
        def na_palochke(self):
            print("Предлагаем мороженое на палочке")
        def v_rozhke(self):
            print("Предлагаем мороженое в рожке")

    ice_cream_stand = IceCreamStand("Кафе-мороженое", "Мороженое", "Невский пр. 35", "10:00 - 20:00")

    ice_cream_stand.add_flavor("Ванильное")
    ice_cream_stand.add_flavor("Клубничное")
    ice_cream_stand.add_flavor("Шоколадное")

    ice_cream_stand.describe_restaurant()
    ice_cream_stand.flavors_menu()
    ice_cream_stand.location_and_hours()
    ice_cream_stand.check_flavor("Ванильное")
    ice_cream_stand.remove_flavor("Шоколадное")
    ice_cream_stand.na_palochke()
    ice_cream_stand.v_rozhke()
task2()