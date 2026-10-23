import random
# Спрашиваем размеры матрицы
n = int(input("Введите количество строк (N): "))
m = int(input("Введите количество столбцов (M): "))
# Заполняем матрицу случайными числами от 1 до 9
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(1, 9))
    matrix.append(row)
# Показываем исходную матрицу
print("\nИсходная матрица:")
for row in matrix:
    print(row)
# Транспонируем: строки становятся столбцами,
# то есть элемент [i][j] переезжает в [j][i]
transposed = []
for j in range(m):
    new_row = []
    for i in range(n):
        new_row.append(matrix[i][j])
    transposed.append(new_row)
# Показываем транспонированную
print("\nТранспонированная матрица:")
for row in transposed:
    print(row)
# Считаем определитель исходной матрицы методом Гаусса
det_original = None
if len(matrix) == len(matrix[0]):
    a = [row[:] for row in matrix]
    size = len(a)
    det_original = 1
    for i in range(size):
        # Если на диагонали ноль — ищем ненулевую строку и меняемся
        if a[i][i] == 0:
            found = False
            for k in range(i + 1, size):
                if a[k][i] != 0:
                    a[i], a[k] = a[k], a[i]
                    det_original = -det_original
                    found = True
                    break
            if not found:
                det_original = 0
                break
        # Обнуляем элементы ниже диагонали
        for k in range(i + 1, size):
            factor = a[k][i] / a[i][i]
            for j in range(i, size):
                a[k][j] -= factor * a[i][j]
        det_original *= a[i][i]
# Считаем определитель транспонированной матрицы тем же способом
det_transposed = None
if len(transposed) == len(transposed[0]):
    a = [row[:] for row in transposed]
    size = len(a)
    det_transposed = 1
    for i in range(size):
        if a[i][i] == 0:
            found = False
            for k in range(i + 1, size):
                if a[k][i] != 0:
                    a[i], a[k] = a[k], a[i]
                    det_transposed = -det_transposed
                    found = True
                    break
            if not found:
                det_transposed = 0
                break
        for k in range(i + 1, size):
            factor = a[k][i] / a[i][i]
            for j in range(i, size):
                a[k][j] -= factor * a[i][j]
        det_transposed *= a[i][i]
print("\nОпределитель исходной матрицы:", det_original)
print("Определитель транспонированной матрицы:", det_transposed)
# Сравниваем: по свойству определителя det(A) = det(Aᵀ),
# так что для квадратных матриц они должны совпасть
if det_original is None:
    print("Матрица не квадратная — определитель не существует.")
elif det_original == det_transposed:
    print("Определители равны.")
else:
    print("Определители не равны.")