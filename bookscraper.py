import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook

url = "https://books.toscrape.com"
result = requests.get(url)

soup = BeautifulSoup(result.text, "html.parser")

books = soup.find_all("h3")
prices = soup.find_all("p", class_="price_color")

wb = Workbook()
ws = wb.active
ws.append(["TITLE", "PRICE"])

for book,price in zip(books, prices):
    ws.append([book.text, price.text])

wb.save("Menu.xlsx")

import os
os.startfile("Menu.xlsx")
