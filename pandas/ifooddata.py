import pandas as pd

df = pd.read_csv('ifood/pedidos.csv')

print(df['endereco_origem'].tail())


