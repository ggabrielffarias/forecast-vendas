📊 Forecast de Vendas — Projeto de Portfólio

Projeto de análise e previsão de vendas utilizando Python e Power BI, com modelagem dimensional (Fato e Dimensão) aplicada desde a base de dados.

🎯 Objetivo

Construir um pipeline completo de dados que:

Organiza os dados em um modelo dimensional (Fato + Dimensões)

Realiza análise exploratória das vendas

Prevê as vendas dos próximos 6 meses com base em tendência e sazonalidade

🛠️ Tecnologias Utilizadas

Ferramenta

Uso

Python 3.x

Geração de dados, análise e forecast

Pandas / NumPy

Manipulação e modelagem de dados

Matplotlib / Seaborn

Visualizações

Power BI

Dashboard interativo

SQL (Oracle)

Consultas e transformações

🗂️ Estrutura do Projeto

forecast-vendas/
├── gerar_dados.py              # Geração dos dados fictícios
├── analise_forecast.py         # EDA + modelo de previsão
├── graficos/                   # Gráficos exportados pelo Python
│   ├── 01_vendas_mensais.png
│   ├── 02_sazonalidade.png
│   ├── 03_categorias.png
│   ├── 04_canal_venda.png
│   └── 05_forecast.png
├── dim_produto.csv
├── dim_cliente.csv
├── dim_tempo.csv
├── fat_vendas.csv
└── README.md

📐 Modelagem Dimensional

Dimensão Produto

id_produto (PK)

nome_produto

categoria

preco_unitario

Dimensão Cliente

id_cliente (PK)

nome_cliente

cidade

segmento

Dimensão Tempo

id_data (PK)

data

ano

mês

trimestre

dia_semana

Fato Vendas

id_venda (PK)

data (FK → dim_tempo)

id_produto (FK → dim_produto)

id_cliente (FK → dim_cliente)

quantidade

preco_unitario

desconto_pct

valor_total

canal

📈 Metodologia do Forecast

O modelo de previsão utiliza duas componentes:

Tendência: regressão linear simples calculada sobre o histórico mensal

Sazonalidade: fator multiplicativo baseado na média histórica por mês

Forecast(t) = Tendência(t) × Sazonalidade(mês)

O intervalo de confiança foi estimado em ±12% sobre o valor previsto, representando a variabilidade histórica observada.

📊 Resultados

Principais Insights da Análise Exploratória

Novembro e Dezembro apresentam os maiores volumes (Black Friday + Natal)

Janeiro e Fevereiro são os meses mais fracos do ano

A tendência geral de vendas é crescimento de aproximadamente 15% ao ano

O canal Online representa a maior fatia das vendas

Previsão para os Próximos 6 Meses

Mês

Previsto

IC Inferior

IC Superior

Jan/2025

R$ 353k

R$ 311k

R$ 396k

Fev/2025

R$ 373k

R$ 328k

R$ 418k

Mar/2025

R$ 489k

R$ 430k

R$ 548k

Abr/2025

R$ 472k

R$ 415k

R$ 529k

Mai/2025

R$ 485k

R$ 427k

R$ 543k

Jun/2025

R$ 636k

R$ 560k

R$ 712k

Total previsto (6 meses): R$ 2,8 milhões

💡 Como Reproduzir

Clone o repositório:

git clone git@github.com:ggabrielffarias/forecast-vendas.git
cd forecast-vendas

Instale as dependências:

pip install pandas numpy matplotlib seaborn

Gere os dados:

python gerar_dados.py

Execute a análise:

python analise_forecast.py

📌 Próximos Passos

Implementar modelo Prophet para forecast mais sofisticado

Conectar dados ao Power BI via Python Connector

Adicionar análise por segmento de cliente

Criar API REST para consumo do forecast em tempo real

👤 Autor

Gabriel Farias

Analista de Dados | SQL | Power BI | Oracle | Python

📧 fariascompiuter@gmail.com

🔗 LinkedIn Post do Projeto:
https://www.linkedin.com/feed/update/urn:li:activity:7445188135988154368/

💻 Perfil no LinkedIn:
https://www.linkedin.com/in/gabriel-paix%C3%A3o-3a4a7b285/


