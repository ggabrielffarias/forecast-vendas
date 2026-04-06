```python
"""
PROJETO: Forecast de Vendas — Análise Exploratória + Previsão
Autor: [Gabriel Farias]
"""

import os
import warnings
from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

warnings.filterwarnings('ignore')

# --------------------------------------------------
# CONFIGURAÇÕES VISUAIS
# --------------------------------------------------
plt.rcParams['figure.facecolor'] = '#0f1117'
plt.rcParams['axes.facecolor'] = '#1a1d27'
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['axes.edgecolor'] = '#2d3047'
plt.rcParams['grid.color'] = '#2d3047'
plt.rcParams['font.family'] = 'DejaVu Sans'

COR_PRINCIPAL = '#00c9a7'
COR_SECUNDARIA = '#845ef7'
COR_ALERTA = '#ff6b6b'
COR_FORECAST = '#ffd43b'

OUTPUT = 'output'
os.makedirs(OUTPUT, exist_ok=True)

# --------------------------------------------------
# CARREGAR DADOS
# --------------------------------------------------
fat = pd.read_csv('fat_vendas.csv', parse_dates=['data'])
dim_prod = pd.read_csv('dim_produto.csv')
dim_cli = pd.read_csv('dim_cliente.csv')

fat = fat.merge(
    dim_prod[['id_produto', 'nome_produto', 'categoria']],
    on='id_produto'
)

fat = fat.merge(
    dim_cli[['id_cliente', 'segmento', 'cidade']],
    on='id_cliente'
)

fat['ano_mes'] = fat['data'].dt.to_period('M')

print('Dados carregados com sucesso!')
print(f"Período: {fat['data'].min().date()} a {fat['data'].max().date()}")
print(f"Total de vendas: R$ {fat['valor_total'].sum():,.2f}")
print(f"Ticket médio: R$ {fat['valor_total'].mean():,.2f}")

# --------------------------------------------------
# 1. VENDAS MENSAIS + MÉDIAS MÓVEIS
# --------------------------------------------------
vendas_mes = fat.groupby('ano_mes')['valor_total'].sum().reset_index()
vendas_mes['ano_mes_dt'] = vendas_mes['ano_mes'].dt.to_timestamp()
vendas_mes['media_movel_3m'] = vendas_mes['valor_total'].rolling(3, center=True).mean()
vendas_mes['media_movel_6m'] = vendas_mes['valor_total'].rolling(6, center=True).mean()

fig, ax = plt.subplots(figsize=(14, 5))

ax.bar(
    vendas_mes['ano_mes_dt'],
    vendas_mes['valor_total'],
    color=COR_PRINCIPAL,
    alpha=0.4,
    width=20,
    label='Venda Mensal'
)

ax.plot(
    vendas_mes['ano_mes_dt'],
    vendas_mes['media_movel_3m'],
    color=COR_PRINCIPAL,
    linewidth=2.5,
    label='Média Móvel 3M'
)

ax.plot(
    vendas_mes['ano_mes_dt'],
    vendas_mes['media_movel_6m'],
    color=COR_SECUNDARIA,
    linewidth=2,
    linestyle='--',
    label='Média Móvel 6M'
)

ax.set_title('Vendas Mensais com Médias Móveis', fontsize=15, fontweight='bold', pad=15)
ax.set_ylabel('Valor Total (R$)')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R$ {x/1e6:.1f}M'))
ax.legend(facecolor='#1a1d27', edgecolor='#2d3047')
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUTPUT}/01_vendas_mensais.png', dpi=150, bbox_inches='tight')
plt.close()

print('Gráfico 1 gerado: vendas mensais')

# --------------------------------------------------
# 2. SAZONALIDADE POR MÊS
# --------------------------------------------------
fat['mes'] = fat['data'].dt.month
nomes_mes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

sazon = fat.groupby('mes')['valor_total'].mean().reset_index()
sazon['nome_mes'] = sazon['mes'].apply(lambda x: nomes_mes[x - 1])

fig, ax = plt.subplots(figsize=(12, 5))

cores = [
    COR_ALERTA if v == sazon['valor_total'].max()
    else COR_SECUNDARIA if v == sazon['valor_total'].min()
    else COR_PRINCIPAL
    for v in sazon['valor_total']
]

bars = ax.bar(
    sazon['nome_mes'],
    sazon['valor_total'],
    color=cores,
    alpha=0.85,
    edgecolor='#0f1117'
)

for bar, val in zip(bars, sazon['valor_total']):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 500,
        f'R${val/1e3:.0f}k',
        ha='center',
        va='bottom',
        fontsize=8.5,
        color='white'
    )

ax.set_title('Sazonalidade — Ticket Médio por Mês', fontsize=15, fontweight='bold', pad=15)
ax.set_ylabel('Ticket Médio (R$)')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R$ {x/1e3:.0f}k'))
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUTPUT}/02_sazonalidade.png', dpi=150, bbox_inches='tight')
plt.close()

print('Gráfico 2 gerado: sazonalidade')

# --------------------------------------------------
# 3. TOP CATEGORIAS
# --------------------------------------------------
cat_vendas = fat.groupby('categoria')['valor_total'].sum().sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(10, 5))

bars = ax.barh(
    cat_vendas.index,
    cat_vendas.values,
    color=COR_PRINCIPAL,
    alpha=0.85
)

for bar, val in zip(bars, cat_vendas.values):
    ax.text(
        val + cat_vendas.values.max() * 0.01,
        bar.get_y() + bar.get_height() / 2,
        f'R$ {val/1e6:.2f}M',
        va='center',
        fontsize=9,
        color='white'
    )

ax.set_title('Total de Vendas por Categoria', fontsize=15, fontweight='bold', pad=15)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R$ {x/1e6:.1f}M'))
ax.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUTPUT}/03_categorias.png', dpi=150, bbox_inches='tight')
plt.close()

print('Gráfico 3 gerado: categorias')

# --------------------------------------------------
# 4. CANAL DE VENDA
# --------------------------------------------------
canal = fat.groupby('canal')['valor_total'].sum()

fig, ax = plt.subplots(figsize=(7, 7))

cores_pizza = [COR_PRINCIPAL, COR_SECUNDARIA, COR_ALERTA]

wedges, texts, autotexts = ax.pie(
    canal.values,
    labels=canal.index,
    autopct='%1.1f%%',
    colors=cores_pizza,
    wedgeprops={'edgecolor': '#0f1117', 'linewidth': 2},
    textprops={'color': 'white'}
)

for texto in autotexts:
    texto.set_fontsize(11)
    texto.set_fontweight('bold')

ax.set_title('Distribuição por Canal de Venda', fontsize=15, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig(f'{OUTPUT}/04_canal_venda.png', dpi=150, bbox_inches='tight', facecolor='#0f1117')
plt.close()

print('Gráfico 4 gerado: canal de venda')

# --------------------------------------------------
# 5. FORECAST COM TENDÊNCIA E SAZONALIDADE
# --------------------------------------------------
vendas_mes['indice'] = range(len(vendas_mes))
vendas_mes['mes_num'] = vendas_mes['ano_mes'].dt.month

fat_sazonalidade = fat.groupby(fat['data'].dt.month)['valor_total'].mean()
fat_sazonalidade_normalizada = fat_sazonalidade / fat_sazonalidade.mean()

X = vendas_mes['indice'].values
y = vendas_mes['valor_total'].values

coef = np.polyfit(X, y, 1)
tendencia_fn = np.poly1d(coef)

ultimo_idx = vendas_mes['indice'].max()
ultimo_mes = vendas_mes['ano_mes'].max()
periodos_forecast = 6

forecast_meses = pd.period_range(
    start=ultimo_mes + 1,
    periods=periodos_forecast,
    freq='M'
)

forecast_idx = np.arange(
    ultimo_idx + 1,
    ultimo_idx + 1 + periodos_forecast
)

forecast_base = tendencia_fn(forecast_idx)

forecast_vals = []

for i, periodo in enumerate(forecast_meses):
    sazonalidade = fat_sazonalidade_normalizada.get(periodo.month, 1.0)
    forecast_vals.append(forecast_base[i] * sazonalidade)

forecast_vals = np.array(forecast_vals)
ic_sup = forecast_vals * 1.12
ic_inf = forecast_vals * 0.88

datas_hist = vendas_mes['ano_mes_dt']
datas_fc = [periodo.to_timestamp() for periodo in forecast_meses]

fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(
    datas_hist,
    vendas_mes['valor_total'],
    color=COR_PRINCIPAL,
    linewidth=2.5,
    label='Histórico',
    zorder=3
)

ax.plot(
    datas_hist,
    tendencia_fn(X),
    color='white',
    linewidth=1,
    linestyle=':',
    alpha=0.4,
    label='Tendência'
)

ax.plot(
    datas_fc,
    forecast_vals,
    color=COR_FORECAST,
    linewidth=2.5,
    linestyle='--',
    label='Forecast 6M',
    zorder=3
)

ax.fill_between(
    datas_fc,
    ic_inf,
    ic_sup,
    color=COR_FORECAST,
    alpha=0.15,
    label='Intervalo de Confiança (±12%)'
)

ax.axvline(
    x=datas_hist.iloc[-1],
    color='white',
    linewidth=1,
    linestyle='--',
    alpha=0.4
)

ax.text(
    datas_hist.iloc[-1],
    ax.get_ylim()[1] * 0.95,
    '  Hoje',
    color='white',
    fontsize=9,
    alpha=0.6
)

ax.set_title('Forecast de Vendas — Próximos 6 Meses', fontsize=15, fontweight='bold', pad=15)
ax.set_ylabel('Valor Total (R$)')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R$ {x/1e6:.1f}M'))
ax.legend(facecolor='#1a1d27', edgecolor='#2d3047')
ax.grid(alpha=0.2)

plt.tight_layout()
plt.savefig(f'{OUTPUT}/05_forecast.png', dpi=150, bbox_inches='tight')
plt.close()

print('Gráfico 5 gerado: forecast')

# --------------------------------------------------
# RESUMO DO FORECAST
# --------------------------------------------------
print('\nFORECAST — PRÓXIMOS 6 MESES:')
print(f"{'Mês':<15} {'Previsto':>15} {'Mín (IC)':>15} {'Máx (IC)':>15}")
print('-' * 62)

for periodo, valor, minimo, maximo in zip(forecast_meses, forecast_vals, ic_inf, ic_sup):
    print(
        f"{str(periodo):<15} "
        f"R$ {valor:>11,.2f} "
        f"R$ {minimo:>11,.2f} "
        f"R$ {maximo:>11,.2f}"
    )

total_forecast = forecast_vals.sum()

print(f'\nTotal previsto (6 meses): R$ {total_forecast:,.2f}')
print(f'\nAnálise concluída! Gráficos salvos em: {OUTPUT}')
```

