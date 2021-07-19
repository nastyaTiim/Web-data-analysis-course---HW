from flask import Flask, render_template
import pandas as pd
import random

app = Flask(__name__)

BOOK_BASE = pd.read_excel('books.xlsx')


@app.route("/")
def start():
    return render_template('index.html')


@app.route("/main", methods=['POST'])
def main():
    index = random.randint(0, BOOK_BASE.shape[0] - 1)
    book_data = {
        "name": BOOK_BASE.iloc[index]['Название'],
        "genre": BOOK_BASE.iloc[index]['Жанр'],
        "author": BOOK_BASE.iloc[index]['Автор'],
        "picture": BOOK_BASE.iloc[index]['Картинка'],
        "url": BOOK_BASE.iloc[index]['Ссылка'],
    }
    return render_template('main.html', book_data=book_data)
