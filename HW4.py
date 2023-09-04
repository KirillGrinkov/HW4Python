# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

arr1 = []
arr2 = []
sum_arr = []
n = int(input("Введите количество чисел первого множества: "))
for i in range(n):
    x = int(input("Введите значение первого множества: "))
    arr1.append(x)

m= int(input("Введите количество чисел второго множества: "))
for i in range(m):
    y = int(input("Введите значение второго множества: "))
    arr2.append(y)

print()
print(arr1)
print(arr2)
arr1.sort()
arr2.sort()
print()
print(arr1)
print(arr2)
print()
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            sum_arr.append(arr1[i])


unique_arr = list(set(sum_arr))
print(unique_arr)





# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.Эти кусты обладают разной урожайностью, поэтому ко времени сбора на 
# них выросло различное число ягод — на i-ом кусте выросло ai ягод.В этом фермерском хозяйстве внедрена 
# система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих
# модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды 
# с этого куста и с двух соседних с ним.Напишите программу для нахождения максимального числа ягод, которое 
# может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.




# def max_collected_berries(berries):
#     n = len(berries)
#     max_collected = 0
    
#     for i in range(1, n - 1):
#         collected = berries[i] + berries[i - 1] + berries[i + 1]
#         max_collected = max(max_collected, collected)
    
#     return max_collected

# N = int(input("Введите количество кустов: "))
# berries = []
# for i in range(N):
#     ai = int(input(f"Введите количество ягод на кусте {i + 1}: "))
#     berries.append(ai)

# result = max_collected_berries(berries)
# print(f"Максимальное количество ягод, которое можно собрать за один заход: {result}")