def task1():
    def delenie(x, y):
        if x % y == 0:
            return "Число делится на ", y
        else:
            return "Число не делится на ", y
    x = int(input("Введите делимое: "))
    y = int(input("Введите делитель: "))
    print (delenie(x, y))
task1()


def task2():
    def delen(x):
        ans = 300 / x
        return ans
    try:
        x = int(input("Введите число: "))
        print (delen(x))
    except ValueError:
        print("Ошибка, введено не число!")
    except ZeroDivisionError:
        print("Ошибка, нельзя делить на ноль!")
#task2()



def task3():
    def magic(dat):
        result = dat.split('.')
        day = int(result[0])
        month = int(result[1])
        year = int(result[2])
        x = day * month
        y = year % 100
        if x == y:
            return True
        else:
            return False

    dat = str(input("Введите дату: "))
    print (magic(dat))
#task3()



