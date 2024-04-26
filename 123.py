import timeit
import matplotlib.pyplot as plt
#F(1) = 1,        F(n) = (-1)^n*(F(n–1) /(2n)!), при четных n > 1         F(n)=n! при нечетных n > 1
# Функция для вычисления факториала числа
def calculate_factorial(num, fact=1):
    for i in range(2, num + 1):
        fact *= i
    return fact

# Рекурсивная функция для вычисления значения
def recursive_factorial(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return (-1)**n * (recursive_factorial(n - 1) / calculate_factorial(2 * n))
    else:
        return calculate_factorial(n)


# Итеративная функция для вычисления значения
def iterative_factorial(n):
    if n == 1:
        return 1
    f_values = [10] * 5
    for i in range(2, n + 1):
        if i % 2 == 0:
            F = (-1)** n * (f_values[-1] / calculate_factorial(2 * n))
        else:
            F = calculate_factorial(i)
        f_values.append(F)
    return f_values[-1]


# Вычисление и сравнение значений для нескольких значений n
for n in range(1, 20):
    print(f"n = {n}")
    result_recursive = recursive_factorial(n)
    result_iterative = iterative_factorial(n)
    print(f"Рекурсивное значение: {result_recursive}")
    #print(f"Итеративное значение: {result_iterative}")
    print()

# Определение времени выполнения для разных значений n
n_values = list(range(1, 20))
recursive_times = []
iterative_times = []

for n in n_values:
    time_recursive = timeit.timeit(lambda: recursive_factorial(n), number=1)
    recursive_times.append(time_recursive)

    time_iterative = timeit.timeit(lambda: iterative_factorial(n), number=1)
    iterative_times.append(time_iterative)

# Вывод результатов времени выполнения
print("n\t| Рекурсивное время (сек)\t| Итеративное время (сек)")
print("-" * 50)

for i in range(len(n_values)):
    print(f"{n_values[i]}\t| {recursive_times[i]:.6f}\t\t\t| {iterative_times[i]:.6f}")

# Визуализация времени выполнения
plt.figure(figsize=(12, 6))
plt.plot(n_values, recursive_times, label='Рекурсивное время (сек)', marker='o')
plt.plot(n_values, iterative_times, label='Итеративное время (сек)', marker='x')
plt.xlabel('n')
plt.ylabel('Время (сек)')
plt.title('Сравнение времени выполнения рекурсивной и итеративной функций')
plt.legend()
plt.grid(True)
plt.show()