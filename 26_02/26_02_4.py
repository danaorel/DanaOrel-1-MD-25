import random
def f():
    n1 = random.randint(1,10)
    n2 = random.randint(1, 10)
    return n1, n2
def check(n1, n2, user):
    ans = n1 + n2
    if user == ans:
        print("Правильно!")
        return True
    else:
        print("Ответ неверный")
        return False
right = 0
wrong = 0
while wrong < 3:
    n1, n2 = f()
    user = int(input(f"{n1} + {n2} = "))
    if check(n1, n2, user):
        right += 1
    else:
        wrong +=1
print ("Игра окончена. Правильных ответов: ", right)