N = int(input("Введите натуральное число N: "))

def factorial_sum(N):
    sum_s = 1.0
    factorial_value = 1.0

    for i in range(1, N + 1):
        factorial_value *= i
        sum_s += 1 / factorial_value

    return sum_s

result = factorial_sum(N)
print(f"{result:.5f}")