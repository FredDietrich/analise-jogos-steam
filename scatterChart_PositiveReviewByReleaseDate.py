import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go

# Lendo o arquivo csv com os dados
df = pd.read_csv("limpo.csv", index_col="id")

# Convertendo o campo release_date para datetime
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

# Filtrando dados com preço menor que 100
df = df[df["price"] < 100]

# Criando o gráfico
fig = go.Figure(data=go.Scatter(
    x=df["release_date"],
    y=df["percent_positive"],
    mode='markers',
    text=df["title"] + "<br>" + "Preço: " + df["price"].astype(str) + " dólares<br>" + "Reviews: " + df["reviews"].astype(str),
    hoverinfo="text"
))

# Personalizando o layout do gráfico
fig.update_layout(
    title="Percentual de reviews positivas em relação à data de lançamento",
    xaxis_title="Data de lançamento",
    yaxis_title="% de reviews positivas",
    yaxis_tickformat=".2%",
    hovermode="closest",
    template="simple_white"
)

# Exibindo o gráfico
fig.show()