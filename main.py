n = int(input("Введите число n: "))
# S - сумма чисел, которая выводится из выражения 1+1/2**2+1/3**2+...+1/n**2
S = 0
while n >= 1:
    S += 1 / (n ** 2)
    n -= 1
print("Сумма чисел: ", S)