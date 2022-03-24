import matplotlib.pyplot as plt
import numpy as np
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
x = np.linspace(-100, 100, 100)
y = a*x**2 + b*x + c
fig, ax = plt.subplots()
ax.plot(x, y, color="purple", linestyle='dashdot', label="x(y)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

plt.show()
fig.savefig('graphic.png')