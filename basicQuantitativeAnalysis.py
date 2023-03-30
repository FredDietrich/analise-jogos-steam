#!/usr/bin/python3

import pandas as pd

df = pd.read_csv('limpo.csv', delimiter=',', low_memory=False, index_col="id")

print(df.price.describe())

print(df.reviews.describe())
