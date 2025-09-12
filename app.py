import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Cria o app
app = dash.Dash(__name__)

# Carrega os dados (precisa ter o arquivo economic_data.csv na mesma pasta)
df = pd.read_csv("economic_data.csv")

# Cria visualização
fig = px.line(df, x="date", y="gdp_growth", title="GDP Growth Rate")

# Layout do app
app.layout = html.Div([
    html.H1("Painel de Indicadores Econômicos"),
    dcc.Graph(figure=fig)
])

# Roda o servidor
if __name__ == "__main__":
   app.run(debug=True)
