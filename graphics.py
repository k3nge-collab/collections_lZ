import matplotlib.pyplot as plt
import math
# Тут будем хранить значения для графика
x_list = []
y_sq = []
y_exp = []
y_ln = []
y_cube = []
# Считаем от -2 до 2, шаг 0.1 чтобы линии были ровные
x = -2.0
while x <= 2.0:
    x_list.append(x)
    # Считаем значения функций
    y_sq.append(x**2)
    y_exp.append(math.exp(x))
    y_cube.append(x**3)
    # Логарифм от отрицательных не считается, поэтому проверяем
    if x > 0:
        y_ln.append(math.log(x))
    else:
        y_ln.append(None)    
    x = x + 0.1
# Настраиваем размер окна, чтобы график не был слишком маленьким
plt.figure(figsize=(8, 6))
# Рисуем график x^2, красный и с кружочками
# markevery=10 это чтобы точки не слипались в линию
plt.plot(x_list, y_sq, color='red', label='x^2', marker='o', markevery=10)
# Рисуем график e^x, синий с крестиками
plt.plot(x_list, y_exp, color='blue', label='e^x', marker='x', markevery=10)# Рисуем график ln(x), зелёный с квадратиками
plt.plot(x_list, y_ln, color='green', label='ln(x)', marker='s', markevery=10)
# Рисуем график x^3, оранжевый с треугольниками
plt.plot(x_list, y_cube, color='orange', label='x^3', marker='^', markevery=10)# Подписываем оси и пишем название
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.title("Графики функций")# Включаем сетку, так удобнее смотреть
plt.grid(True)# Показываем какой цвет за какую функцию отвечает
plt.legend()# Выводим окно с графиком на экран
plt.show()