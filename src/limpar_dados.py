import pandas as pd

df = pd.read_csv('data/raw/vendas.csv')

df['produto'] = df['produto'].str.strip().str.upper()
df['cliente'] = df['cliente'].str.strip().str.upper()
df['vendedor'] = df['vendedor'].str.strip().str.upper()
df['data'] = pd.to_datetime(df['data'])
df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month
df['total'] = df['preco'] * df['quantidade']

df.to_csv('data/processed/vendas_tratadas.csv', index=False)
print(df.head())
