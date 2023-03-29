#!/usr/bin/python3

import pandas as pd

df = pd.read_csv('pronto.csv', delimiter=',', low_memory=False, index_col="id")

important_cols = ["title", "release_date", "developer", "genres", "price", "reviews", "percent_positive"]

df = df.dropna(subset=important_cols)

df = df[df.columns.intersection(important_cols)]

# -- Lidando com preço

def correct_price(price):
    if price == 'Free to play':
        return 0.0
    elif ',' in price:
        price = price.replace(',', '')
    return float(price)

def convert_to_brl(line):
    return round(line * 0.062, 2) # cotação da rupee no dia 29 de março de 2023

df.price = df.price.apply(correct_price) # corrigindo o preço, para os casos de string, e grátis

df.price = df.price.apply(convert_to_brl) # convertendo o preço agora de rupee para brl

# -- Lidando com percent de reviews

def convert_percentage_to_decimal(percentage):
    print(percentage)
    percentage = percentage.replace('%', '')
    return float(float(percentage) / 100)

df.percent_positive = df.percent_positive.apply(convert_percentage_to_decimal)

df.to_csv('teste1.csv')
