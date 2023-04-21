import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo csv com os dados
df = pd.read_csv("limpo.csv")

# Filtrando os jogos com pelo menos 100 avaliações
df = df[df['reviews'] >= 100]

# Plotando o histograma do atributo "price"
plt.hist(df['price'], bins=20)
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.title('Distribuição de Frequência do Preço dos Jogos')
plt.show()
