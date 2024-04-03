def task1():
    a = {'Russia': 'Moscow', 'Italy': 'Rome', 'France': 'Paris', 'Spain': 'Madrid'}
    print (a)
    print (a['Italy'])
    print (sorted(a))
#task1()


def task2():
    one = set('авеинорст')
    two = set('дклмпу')
    three = set('бгёья')
    four = set('йы')
    five = set('жзхцч')
    eight = set('шэю')
    ten = set('фщъ')
    a = input('Введите слово ')
    n = 0
    for i in a:
        if i in one:
            n +=1
        elif i in two:
            n +=2
        elif i in three:
            n +=3
        elif i in four:
            n +=4
        elif i in five:
            n +=5
        elif i in eight:
            n +=8
        else:
            n +=10
    print('Стоимость слова - ', n)
#task2()

def task3():
    a = int(input('Сколько всего студентов? '))
    b =  set()
    x = set()
    for i in range (a):
        fam = input('Введите свою фамилию ')
        lng = int(input('Сколько языков вы знаете? '))
        for j in range (lng):
            c = input('Введите один из языков ')
            if c not in b:
                b.add(c)
            if c == 'китайский':
                x.add(fam)
    print('Всего различных языков - ', len(b))
    print('Студенты, знающие китайский - 'x)
task3()
