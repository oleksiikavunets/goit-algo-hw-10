import random

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2


a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


def monte_carlo(num_experiments):
    res = 0

    for _ in range(num_experiments):
        points = [random.uniform(a, b) for _ in range(random.randint(500, 1000))]
        M = sum(f(point) for point in points)
        N = len(points)
        res += (M / N) * (b - a)
    res /= num_experiments
    return res


result, *_ = spi.quad(f, a, b)

print("Інтеграл:      ", result)

for i in range(100, 1001, 100):
    print("Експериментів: ", i)
    print("Монте-Карло:   ", monte_carlo(i))

# Інтеграл:       2.666666666666667
# Експериментів:  100
# Монте-Карло:    2.666179078998175
# Експериментів:  200
# Монте-Карло:    2.6604989406977757
# Експериментів:  300
# Монте-Карло:    2.660501714515586
# Експериментів:  400
# Монте-Карло:    2.669859761720438
# Експериментів:  500
# Монте-Карло:    2.6618929638272935
# Експериментів:  600
# Монте-Карло:    2.664544333505178
# Експериментів:  700
# Монте-Карло:    2.6657119921659937
# Експериментів:  800
# Монте-Карло:    2.6688535914177196
# Експериментів:  900
# Монте-Карло:    2.6665347315773364
# Експериментів:  1000
# Монте-Карло:    2.669085566045206
