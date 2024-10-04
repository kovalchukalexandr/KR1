S = [2, 3, 5, 6, 0, 0]
summ = 0
capacity = len(S) - 1
k = 0
if S[-1] == 0  and S[-2] == 0:
    while k <= capacity:
        summ += S[k] ** 2
        k += 1

print("Сумма чисел: ", summ)