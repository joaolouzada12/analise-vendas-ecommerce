import pandas as pd
import random
from datetime import datetime, timedelta

produtos = ["Mouse", "Teclado", "Monitor", "Headset", "Webcam"]
vendedores = ["Carlos", "Ana", "Pedro"]
clientes = [f"Cliente_{i}" for i in range(1, 21)]

linhas = []

for i in range(1, 101):

    produto = random.choice(produtos)
    vendedor = random.choice(vendedores)
    cliente = random.choice(clientes)

    preco = {
        "Mouse": 80,
        "Teclado": 150,
        "Monitor": 900,
        "Headset": 250,
        "Webcam": 300
    }[produto]

    quantidade = random.randint(1,4)

    data = datetime(2026,1,1) + timedelta(days=random.randint(0,90))

    linhas.append({
        "id_venda": i,
        "data": data,
        "produto": produto,
        "cliente": cliente,
        "vendedor": vendedor,
        "preco": preco,
        "quantidade": quantidade
    })

df = pd.DataFrame(linhas)

df.to_csv("dados/vendas.csv", index=False)