import pandas as pd

df = pd.read_csv('data/processed/vendas_tratadas.csv')
faturamento_total = df['total'].sum()

print(f"Faturamento total: {faturamento_total}")