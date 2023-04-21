import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo csv com os dados
df = pd.read_csv("limpo.csv")

fig, ax = plt.subplots()

ax.scatter(df['price'], df['percent_positive'])
ax.set_xlabel('Preço')
ax.set_ylabel('Percentual de revisões positivas')

plt.show()