N = int(input("Введите натуральное число N: "))

# squares_numbers_smaller - массив, квадраты натуральных чисел которого меньше N
squares_numbers_smaller = []

# smaller_numbers - числа, которые меньше заданного N
smaller_numbers = N
while smaller_numbers > 0:
    if smaller_numbers ** 2 <= N:
        squares_numbers_smaller.append(smaller_numbers ** 2)
    smaller_numbers -= 1

print(squares_numbers_smaller)