import numpy as np
import matplotlib.pyplot as plt
import math


def f(x, y):
    return (x*y + math.exp(x)) / x


def solutionF(a, b, y0, h):
    x_values = np.arange(a, b+h, h)
    y_values = np.zeros(len(x_values))
    for i in range(0, len(x_values)):
        y_values[i] = 0.36 * math.exp(x_values[i]) + math.exp(x_values[i]) * np.log(x_values[i])
    return y_values


def euler(f, a, b, y0, h):
    x_vals = np.arange(a, b + h, h)
    y_vals = np.zeros(len(x_vals))
    y_vals[0] = y0

    for i in range(1, len(x_vals)):
        y_vals[i] = y_vals[i - 1] + h * f(x_vals[i - 1], y_vals[i - 1])

    return x_vals, y_vals


def improved_euler(f, a, b, y0, h):
    x_vals = np.arange(a, b + h, h)
    y_vals = np.zeros(len(x_vals))
    y_vals[0] = y0

    for i in range(1, len(x_vals)):
        y_mid = y_vals[i - 1] + h * f(x_vals[i - 1], y_vals[i - 1]) / 2
        y_vals[i] = y_vals[i - 1] + h * f(x_vals[i - 1] + h / 2, y_mid)

    return x_vals, y_vals


def runge_kutta(f, a, b, y0, h):
    x_vals = np.arange(a, b + h, h)
    y_vals = np.zeros(len(x_vals))
    y_vals[0] = y0

    for i in range(1, len(x_vals)):
        x_i = x_vals[i - 1]
        y_i = y_vals[i - 1]

        k1 = f(x_i, y_i)
        k2 = f(x_i + h / 2, y_i + h / 2 * k1)
        k3 = f(x_i + h / 2, y_i + h / 2 * k2)
        k4 = f(x_i + h, y_i + h * k3)

        y_vals[i] = y_i + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    return x_vals, y_vals


a = 1
b = 2
y0 = 1
h = 0.01

y_solution = solutionF(a, b, y0, h)
x_euler, y_euler = euler(f, a, b, y0, h)
x_improved_euler, y_improved_euler = improved_euler(f, a, b, y0, h)
x_rk4, y_rk4 = runge_kutta(f, a, b, y0, h)

plt.figure(figsize=(10, 6))
plt.plot(x_euler, y_euler, label="Метод Эйлера")
plt.plot(x_improved_euler, y_improved_euler, label="Улучшенный метод Эйлера")
plt.plot(x_rk4, y_rk4, label="Метод Рунге-Кутта 4-го порядка")
plt.plot(x_euler, y_solution, label="Точное решение")
plt.title("Решение задачи Коши численными методами")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
