def task1():
    a = [5, 18, 9, 230, 0]
    n = int(input('Введите число '))
    if n in a:
        print('Поздравляю, Вы угадали число!')
    else:
        print('Нет такого числа!')
#task1()

def task2():
    a = [10, 1, 'a', 6, 8, 1, 'a']
    b = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j] and a[i] not in b:
                b.append(a[i])
    print(b)
#task2()

def task3():
    a = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')
    n = int(input('Сколько выходных на неделе? '))
    print ('Ваши выходные дни: ', a[-n:])
    print('Ваши рабочие дни: ', a[0:-n])
#task3()

def task4():
    a = ['Алексеев', 'Иванов', 'Петров', 'Токарева', 'Постников', 'Орел', 'Анисимов', 'Курнаков', 'Измаилов', 'Крылов']
    b = ['Александров', 'Иванченко', 'Микулич', 'Круглов', 'Гурина', 'Базлова', 'Молокова', 'Панибратов', 'Конев', 'Киселев']
    team = tuple(a[1:6] + b[:5])
    print(a)
    print(b)
    print(team)
    print(len(team))
    print(sorted(team))
task4()