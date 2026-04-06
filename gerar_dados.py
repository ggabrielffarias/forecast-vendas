```python
"""
PROJETO: Forecast de Vendas
Autor: [Gabriel Farias]
Descrição: Geração de dados fictícios de vendas com modelagem dimensional
"""

import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

# --------------------------------------------------
# DIMENSÃO: PRODUTO
# --------------------------------------------------
produtos = pd.DataFrame({
    'id_produto': range(1, 11),
    'nome_produto': [
        'Notebook Pro', 'Mouse Gamer', 'Teclado Mecânico', 'Monitor 24"',
        'Headset USB', 'Webcam HD', 'SSD 480GB', 'Memória RAM 16GB',
        'Cabo HDMI', 'Hub USB'
    ],
    'categoria': [
        'Computadores', 'Periféricos', 'Periféricos', 'Monitores',
        'Periféricos', 'Periféricos', 'Armazenamento', 'Armazenamento',
        'Cabos', 'Acessórios'
    ],
    'preco_unitario': [4500, 280, 650, 1200, 350, 420, 380, 520, 45, 90]
})

# --------------------------------------------------
# DIMENSÃO: CLIENTE
# --------------------------------------------------
cidades = [
    'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba',
    'Porto Alegre', 'Belém', 'Fortaleza', 'Salvador'
]

segmentos = ['Varejo', 'Corporativo', 'Governo', 'Educação']

clientes = pd.DataFrame({
    'id_cliente': range(1, 51),
    'nome_cliente': [f'Cliente_{i:03d}' for i in range(1, 51)],
    'cidade': [random.choice(cidades) for _ in range(50)],
    'segmento': [random.choice(segmentos) for _ in range(50)],
    'estado': [random.choice(['SP', 'RJ', 'MG', 'PR', 'RS', 'PA', 'CE', 'BA']) for _ in range(50)]
})

# --------------------------------------------------
# DIMENSÃO: TEMPO
# --------------------------------------------------
datas = pd.date_range(start='2022-01-01', end='2024-12-31', freq='D')


# --------------------------------------------------
# FATO: VENDAS
# --------------------------------------------------
registros = []

for _ in range(5000):
    data = random.choice(datas)
    produto = produtos.sample(1).iloc[0]
    cliente = clientes.sample(1).iloc[0]

    mes = data.month

    # Ajuste de sazonalidade
    sazonalidade = 1.0
    if mes in [11, 12]:
        sazonalidade = 1.8
    elif mes in [1, 2]:
        sazonalidade = 0.7
    elif mes in [6, 7]:
        sazonalidade = 1.2

    # Crescimento gradual por ano
    tendencia = 1.0 + (data.year - 2022) * 0.15

    quantidade = max(1, int(np.random.poisson(3 * sazonalidade * tendencia)))
    preco = produto['preco_unitario'] * np.random.uniform(0.85, 1.10)
    desconto = round(random.choice([0, 0, 0, 5, 10, 15]), 2)
    valor_total = round(quantidade * preco * (1 - desconto / 100), 2)

    registros.append({
        'id_venda': len(registros) + 1,
        'data': data,
        'id_produto': produto['id_produto'],
        'id_cliente': cliente['id_cliente'],
        'quantidade': quantidade,
        'preco_unitario': round(preco, 2),
        'desconto_pct': desconto,
        'valor_total': valor_total,
        'canal': random.choice(['Online', 'Loja Física', 'Representante'])
    })

fat_vendas = pd.DataFrame(registros)

# --------------------------------------------------
# DIMENSÃO DE TEMPO
# --------------------------------------------------
dim_tempo = pd.DataFrame({
    'id_data': range(1, len(datas) + 1),
    'data': datas,
    'ano': datas.year,
    'trimestre': datas.quarter,
    'mes': datas.month,
    'nome_mes': datas.strftime('%B'),
    'semana': datas.isocalendar().week.astype(int),
    'dia_semana': datas.day_name(),
    'is_fim_de_semana': datas.dayofweek >= 5
})

# --------------------------------------------------
# EXPORTAÇÃO DOS ARQUIVOS
# --------------------------------------------------
produtos.to_csv('dim_produto.csv', index=False, encoding='utf-8-sig')
clientes.to_csv('dim_cliente.csv', index=False, encoding='utf-8-sig')
dim_tempo.to_csv('dim_tempo.csv', index=False, encoding='utf-8-sig')
fat_vendas.to_csv('fat_vendas.csv', index=False, encoding='utf-8-sig')

print('Dados gerados com sucesso!')
print(f'fat_vendas: {len(fat_vendas)} registros')
print(f'dim_produto: {len(produtos)} produtos')
print(f'dim_cliente: {len(clientes)} clientes')
print(f'dim_tempo: {len(dim_tempo)} datas')
```

Principais ajustes feitos:

* Removido caminho absoluto local `/home/claude/...`
* Removida referência a ambiente externo
* Comentários simplificados
* Estrutura mais limpa para GitHub
* Mantida apenas a lógica de negócio e geração dos dados

