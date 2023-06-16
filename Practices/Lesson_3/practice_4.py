import random

import pandas as pd
import numpy as np

df = pd.read_csv("Housing.csv")


def cost(y: np.array, h: np.array) -> float:
    return np.mean((h - y) ** 2) / 2


class LinearRegressionM:
    def __init__(
        self, lr: float = 0.001, thr: float = 0.00001, n_epochs: int = 1000
    ) -> None:
        self.lr = lr
        self.thr = thr
        self.n_epochs = n_epochs
        self.w = np.array(
            [random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)]
        )
        print(f"Init w: {self.w}")

    def predict(self, X: list) -> list:
        return self.w @ X.T

    def update_w(self, X: np.array, y: np.array):
        m = len(y)
        h = self.predict(X)
        self.w -= self.lr / m * X.T @ (h - y)

    def fit(self, X: np.array, y: np.array):
        last_cost = 1000000
        for i in range(self.n_epochs):
            self.update_w(X, y)
            new_cost = cost(y, self.predict(X))
            if last_cost - new_cost < self.thr:
                print(
                    f"Ітерація # {i}, ваги: {self.w}, мінімальне значення cost функції: {new_cost}"
                )
                break
            last_cost = new_cost


def normalization(data):
    mean = np.mean(data)
    value_range = np.max(data) - np.min(data)
    result = []
    for x in data:
        norm_x = (x - mean) / value_range
        result.append(norm_x)
    return result


norm_df = pd.DataFrame()
norm_df["price"] = normalization(df.price)
norm_df["area"] = normalization(df.area)
norm_df["bedrooms"] = normalization(df.bedrooms)
norm_df["bathrooms"] = normalization(df.bathrooms)


X = np.array([norm_df.area, norm_df.bedrooms, norm_df.bathrooms]).T
y = np.array(norm_df.price)

linear_regression = LinearRegressionM(lr=0.05, thr=0.0001, n_epochs=10000)
linear_regression.fit(X, y)


# Аналітичне рішення
def h(X, W):
    return np.dot(X, W)


def loss_function(X, Y, W):
    m = X.shape[0]
    return np.square(h(X, W) - Y).sum() / (2 * m)


weights = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
analytical = loss_function(X, y, weights)
print(f"Ваги: {weights}, cost/loss функції при аналітичному рішенні: {analytical}")
