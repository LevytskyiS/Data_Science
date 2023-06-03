import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bestsellers_csv = "bestsellers with categories.csv"

# Task 3.1 Прочитайте csv файл (використовуйте функцію read_csv)
df = pd.read_csv(bestsellers_csv)

# Task 3.2 Виведіть перші п'ять рядків (використовується функція head)
df.head()

# Task 3.3 Виведіть розміри датасету (використовуйте атрибут shape)
df.shape

# Task 3.4
# Про скільки книг зберігає дані датасет?
len(pd.unique(df["Name"]))
# 351

df.columns = ["name", "author", "user_rating", "reviews", "price", "year", "genre"]

# Task 3.5 Перевірте, чи у всіх рядків вистачає даних: виведіть кількість
# пропусків (na) у кожному зі стовпців (використовуйте функції isna та sum)
np.sum(df.isnull())

# Чи є в якихось змінних пропуски?
# Ні

# Task 3.6 Перевірте, які є унікальні значення в колонці
# genre (використовуйте функцію unique)
pd.unique(df["genre"])

# Які є унікальні жанри?
# Non Fiction, Fiction

# Task 3.7 Тепер подивіться на розподіл цін:
# побудуйте діаграму (використовуйте kind='hist')
df["price"].plot(kind="hist", title="Price Frequency", grid=True)

# Task 3.8 Визначте, яка ціна у нас максимальна, мінімальна, середня,
# медіанна (використовуйте функції max, min, mean, median)
prices = df["price"]
max_p = prices.max()
min_p = prices.min()
mean_p = prices.mean()
median_p = prices.median()
# Максимальна ціна? - 105
# Мінімальна ціна? - 0
# Середня ціна? - 13.1
# Медіанна ціна? - 11.0

# Task 3.9 Який рейтинг у датасеті найвищий? Відповідь: 4.9
highest_rating = df["user_rating"].max()

# Task 3.10 Скільки книг мають такий рейтинг? Відповідь: 52
hr_books_df = df[df["user_rating"] >= highest_rating]
quantity = hr_books_df["name"].count()

# Task 3.11 Яка книга має найбільше відгуків? Відповідь: Where the Crawdads Sing
most_revs_book = df[df["reviews"] == df["reviews"].max()]["name"]

# Task 3.12 З тих книг, що потрапили до Топ-50 у 2015 році,
# яка книга найдорожча (можна використати проміжний датафрейм)? Відповідь: Humans of New York : Stories
top_50_2015 = (
    df.sort_values(by="user_rating", ascending=False).head(50).loc[(df["year"] == 2015)]
)
most_exp_book_2015 = top_50_2015[
    top_50_2015["price"] == top_50_2015["price"].max()
].name

# Task 3.13 Скільки книг жанру Fiction потрапили до Топ-50 у 2010 році (використовуйте &)? Відповідь: 2
fiction_2010 = len(
    df.sort_values(by="reviews", ascending=False)
    .head(50)
    .loc[((df["year"] == 2010) & (df["genre"] == "Fiction"))]
)

# Task 3.14 Скільки книг з рейтингом 4.9 потрапило до рейтингу
# у 2010 та 2011 роках (використовуйте | або функцію isin)? Відповідь: 1
b49 = df[
    (df["year"] == 2011) & (df["user_rating"] == 4.9)
    | (df["year"] == 2010) & (df["user_rating"] == 4.9)
]

# Task 3.15  насамкінець, давайте відсортуємо за зростанням ціни всі книги, які потрапили до
# рейтингу в 2015 році і коштують дешевше за 8 доларів (використовуйте функцію sort_values).
# Відповідь: Яка книга остання у відсортованому списку? Відповідь: Old School (Diary of a Wimpy Kid #10)
books_2015 = df[df["year"] == 2015].sort_values(by="price", ascending=True)
cheap_books_2015 = books_2015[(books_2015["price"] < 8)]
last_book = cheap_books_2015.tail(1).name
