def task1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} предлагает  {self.cuisine_type}.")
        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")
    newRestaurant = Restaurant("Italiano", "итальянскую кухню")

    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
#task1()
def task2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} предлагает {self.cuisine_type}.")
        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")
    restaurant1 = Restaurant("France", "французскую кухню")
    restaurant2 = Restaurant("Burrito", "мексиканскую кухню")
    restaurant3 = Restaurant("Sushi", "японскую кухню")
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
#task2()
def task3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, restaurant_rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = restaurant_rating
        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} предлагает {self.cuisine_type}. Рейтинг: {self.rating}")
        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")
        def update_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.restaurant_name} обновлен: {self.rating}")
    restaurant1 = Restaurant("Italiano", "итальянскую кухню", 4.6)
    restaurant1.describe_restaurant()
    restaurant1.update_rating(4.9)
task3()