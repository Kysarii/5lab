'''
Лабораторная работа №5 
Задана рекуррентная функция. Область определения функции – натуральные числа. 
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно (значение, время). 
Определить (смоделировать) границы применимости рекурсивного и итерационного подхода. 
Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.
Вариант 16 F(1) = 1,        F(n) = (-1)^n*(F(n–1) /(2n)!)
'''
import timeit
import matplotlib.pyplot as plt

# Кэш для хранения вычисленных значений факториалов

factorial_cache = {0: 1, 1: 1}


# Функция для вычисления факториала числа
def dynamic_fact(n):
    if n not in factorial_cache:
        factorial_cache[n] = n * dynamic_fact(n - 1)
    return factorial_cache[n]


def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)


# Функция для вычисления значения
def dynamic_F(n,znak = 1, cache={1: 1}):
    if n in cache:
        return cache[n]
    else:
        znak *= -1
        result = znak * (dynamic_F(n - 1, cache, znak)/ dynamic_fact(2 * n, znak))
        cache[n] = result
        return result


# Функция для записи времени
def score_time(func, n):
    return timeit.timeit(lambda: func(n), number=1000)


n_values = range(1, 100)
recursive_times = []
dynamic_times = []

for n in n_values:
    recursive_times.append(score_time(recursive_factorial, n))
    dynamic_times.append(score_time(dynamic_fact, n))

print(f"{'n':<10}{'Рекурсивное время (мс)':<25}{'Динамическое время (мс)':<25}")
for i, n in enumerate(n_values):
    print(f"{n:<10}{recursive_times[i]:<25}{dynamic_times[i]:<25}")

plt.plot(n_values, recursive_times, label='Рекурсивно')
plt.plot(n_values, dynamic_times, label='Динамическое')
plt.xlabel('n')
plt.ylabel('Время (в миллисекундах)')
plt.legend()
plt.title('Сравнение времени вычисления функции F(n)')
plt.show()
