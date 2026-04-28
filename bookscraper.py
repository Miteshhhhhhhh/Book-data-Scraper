import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws.append(["TITLE", "PRICE", "STOCK", "RATING"])

for page in range(1,51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    result = requests.get(url)
    result.encoding = "utf-8"
    soup = BeautifulSoup(result.text, "html.parser")

    books = soup.find_all("h3")
    prices = soup.find_all("p", class_="price_color")
    stock = soup.find_all("p", class_="instock availability")
    ratings = soup.find_all("p", class_="star-rating")


    for book,price,stock,rating in zip(books, prices, stock, ratings):
        ws.append([book.text, price.text, stock.text, rating["class"][1]])

wb.save("books_data.xlsx")

import os
os.startfile("books_data.xlsx")

