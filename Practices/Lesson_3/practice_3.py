import numpy as np

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

housing = "Housing.csv"
df = pd.read_csv(housing)

# Linear regression hypothesis
# print(df[["price", "area", "bedrooms", "bathrooms"]])


# Task 1 Напишіть функцію гіпотези лінійної регресії у векторному вигляді
def h(w_0, w_1, w_2, w_3, x_1, x_2, x_3):
    return w_0 + w_1 * x_1 + w_2 * x_2 + w_3 * x_3


# Task 2 Cтворіть функцію для обчислення функції втрат у векторному вигляді
def loss_function(w_0, w_1, w_2, w_3, df):
    n = df.area.shape[0]
    cost = 0

    for x_1, x_2, x_3, y in zip(df.area, df.bedrooms, df.bathrooms, df.price):
        cost = cost + (h(w_0, w_1, w_2, w_3, x_1, x_2, x_3) - y) ** 2

    return cost / (2 * n)


# w_0 = 0
# w_1 = np.linspace(-6000, 8000, 500)
# w_2 = np.linspace(-6000, 8000, 500)
# w_3 = np.linspace(-6000, 8000, 500)
# plt.plot(w_1, [loss_function(w_0, a, b, c, df) for a, b, c in zip(w_1, w_2, w_3)])
# plt.show()


# Task 3 Pеалізуйте один крок градієнтного спуску
def grad_step(
    w_0, w_1, w_2, w_3, grad_w_0, grad_w_1, grad_w_2, grad_w_3, learning_rate=0.001
):
    w_0 -= learning_rate * grad_w_0
    w_1 -= learning_rate * grad_w_1
    w_2 -= learning_rate * grad_w_2
    w_3 -= learning_rate * grad_w_3
    return w_0, w_1, w_2, w_3


# Task 4 знайдіть найкращі параметри w для датасету прогнозуючу ціну
# на будинок залежно від площі, кількості ванних кімнат та кількості спалень
