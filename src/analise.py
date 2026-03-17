import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('data/processed/vendas_tratadas.csv')
faturamento_total = df['total'].sum()
vendas_por_produto = df.groupby('produto')['quantidade'].sum().sort_values(ascending=False)
melhor_vendedor = df.groupby('vendedor')['total'].sum().sort_values(ascending=False)
melhor_vendedor_nome = melhor_vendedor.index[0]
faturamento_melhor_vendedor = melhor_vendedor.iloc[0]
melhor_cliente = df.groupby('cliente')['total'].sum().sort_values(ascending=False)
top = melhor_cliente.index[0]
valor_cliente = melhor_cliente.iloc[0]
vendas_por_mes = df.groupby('mes')['total'].sum().sort_index()
vendas_por_mes.plot(kind='bar', color='skyblue')
plt.xlabel('Meses')
plt.ylabel('Total')
plt.title("Vendas por mês")
plt.xticks(rotation=0)
plt.tight_layout()

print("=== RESUMO ===")

print(f"Faturamento total: {faturamento_total}")
print("\nVendas por produto:")
print(vendas_por_produto)
print("\nMelhor vendedor:")
print(melhor_vendedor)
print(f"Melhor vendedor: {melhor_vendedor_nome} - Faturamento: {faturamento_melhor_vendedor}")
print(f"Top cliente: {top} - Total: {valor_cliente}")
print("\nVendas por mês:")
print(vendas_por_mes)
plt.show()
