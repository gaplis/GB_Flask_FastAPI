import time


def slow_func():
    print('Начало функции')
    time.sleep(5)
    print('Конец функции')


print('Начало программы')
slow_func()
print('Конец программы')
