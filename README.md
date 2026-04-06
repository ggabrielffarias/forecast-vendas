**📊 Forecast de Vendas — Projeto de Portfólio**  
   
 *Projeto de análise e previsão de vendas utilizando Python e Power BI,*  
   
  *  
   
  com modelagem dimensional (Fato e Dimensão) aplicada desde a base de dados.*  
   
 ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANUlEQVR4nO3OMQ2AABAAsSNBCzpfFxNCmJHAjAU2QtIq6DIzW7UHAMBfnGt1V8fHEQAA3rsexO0F3jmX9Q8AAAAASUVORK5CYII=)  
   
 **🎯 Objetivo**  
   
 Construir um pipeline completo de dados que:  
1. Organiza os dados em um modelo dimensional (Fato + Dimensões)  
2. Realiza análise exploratória das vendas  
3. Prevê as vendas dos próximos 6 meses com base em tendência e sazonalidade  
 ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANklEQVR4nO3OMQ2AABAAsSPBCUbfDbIwwIAABiywEZJWQZeZ2ao9AAD+4liruzq/ngAA8Nr1ABwiBgererhLAAAAAElFTkSuQmCC)  
 **🛠️ Tecnologias Utilizadas**  
   
 | | |  
   
 |-|-|  
   
 | **Ferramenta** |  **Uso** |  
   
 | Python 3.x | Geração de dados, análise e forecast |  
   
 | Pandas / NumPy | Manipulação e modelagem de dados |  
   
 | Matplotlib / Seaborn | Visualizações |  
   
 | Power BI | Dashboard interativo |  
   
 | SQL (Oracle) | Consultas e transformações |  
   
    
 ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANElEQVR4nO3OQQmAUBBAwSf8GIJVt4MRjeHFCt5EmEkw28wc1RkAAH9xrWpV+9cTAABeux8RYAQ2VTY9QwAAAABJRU5ErkJggg==)  
 **🗂️ Estrutura do Projeto**  
   
 forecast-vendas/  
   
  ├── gerar_dados.py          # Geração dos dados fictícios  
   
  ├── analise_forecast.py     # EDA + modelo de previsão  
   
  ├── graficos/               # Gráficos exportados pelo Python  
   
  │   ├── 01_vendas_mensais.png  
   
  │   ├── 02_sazonalidade.png  
   
  │   ├── 03_categorias.png  
   
  │   ├── 04_canal_venda.png  
   
  │   └── 05_forecast.png  
   
  ├── dim_produto.csv  
   
  ├── dim_cliente.csv  
   
  ├── dim_tempo.csv  
   
  ├── fat_vendas.csv  
   
  └── README.md  
   
    
 ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANklEQVR4nO3OQQmAABRAsScYxpg/jU0sYQKvNrCCNxG2BFtmZquOAAD4i3Ot7mr/egIAwGvXA4EOBczQBLu9AAAAAElFTkSuQmCC)  
 **📐 Modelagem Dimensional**  
   
          dim_produto          dim_cliente         dim_tempo  
   
           ───────────          ───────────         ─────────  
   
           id_produto (PK)      id_cliente (PK)     id_data (PK)  
   
           nome_produto         nome_cliente        data  
   
           categoria            cidade              ano / mês / trimestre  
   
           preco_unitario       segmento            dia_semana  
   
    
   
                           fat_vendas (FATO)  
   
                           ─────────────────  
   
                           id_venda (PK)  
   
                           data (FK → dim_tempo)  
   
                           id_produto (FK → dim_produto)  
   
                           id_cliente (FK → dim_cliente)  
   
                           quantidade  
   
                           preco_unitario  
   
                           desconto_pct  
   
                           valor_total  
   
                           canal  
   
    
 ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAM0lEQVR4nO3OUQmAABBAsaeIGMOoF8R0JrGCfyJsCbbMzFldAQDwF/dWrdXx9QQAgNf2B/NoAzRnuYaXAAAAAElFTkSuQmCC)  
 **📈 Metodologia do Forecast**  
   
 O modelo de previsão utiliza duas componentes:  
- **Tendência**: Regressão linear simples calculada sobre o histórico mensal  
- **Sazonalidade**: Fator multiplicativo baseado na média histórica por mês  
   
 Forecast(t) = Tendência(t) × Sazonalidade(mês)  
   
    
   
 O intervalo de confiança foi estimado em **±12%** sobre o valor previsto,  
   
    
   
  representando a variabilidade histórica observada.  
 ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANUlEQVR4nO3OQQ2AQBAAsSHhiQMcoWp9ngBsYIEfIWkVdJuZs5oAAPiLe6+O6vp6AgDAa+sBhZgEOcyZTEcAAAAASUVORK5CYII=)  
 **📊 Resultados**  
 **Principais Insights da Análise Exploratória:**  
- **Novembro e Dezembro** apresentam os maiores volumes (Black Friday + Natal)  
- **Janeiro e Fevereiro** são os meses mais fracos do ano  
- A tendência geral de vendas é **crescimento de ~15% ao ano**  
- O canal **Online** representa a maior fatia das vendas  
 **Previsão para os Próximos 6 Meses:**  
   
 | | | | |  
   
 |-|-|-|-|  
   
 | **Mês** |  **Previsto** |  **IC Inferior** |  **IC Superior** |  
   
 | Jan/2025 | R$ 353k | R$ 311k | R$ 396k |  
   
 | Fev/2025 | R$ 373k | R$ 328k | R$ 418k |  
   
 | Mar/2025 | R$ 489k | R$ 430k | R$ 548k |  
   
 | Abr/2025 | R$ 472k | R$ 415k | R$ 529k |  
   
 | Mai/2025 | R$ 485k | R$ 427k | R$ 543k |  
   
 | Jun/2025 | R$ 636k | R$ 560k | R$ 712k |  
   
    
 **Total previsto (6 meses): R$ 2,8 milhões**  
 ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANUlEQVR4nO3OMQ2AABAAsSPBCUbfD6JYGBDBgAU2QtIq6DIzW7UHAMBfHGt1V+fXEwAAXrseHDoF+/8A8n0AAAAASUVORK5CYII=)  
 **💡 Como Reproduzir**  
**Clone o repositório**  
 git clone [git@github.com:ggabrielffarias/forecast-vendas.git  
  cd forecast-vendas  
   
    
   
  # Instale as dependências  
   
  pip install pandas numpy matplotlib seaborn  
   
    
   
  # Gere os dados  
   
  python gerar_dados.py  
   
    
   
  # Execute a análise  
   
  python analise_forecast.py  
   
    
   
 ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANUlEQVR4nO3OQQmAABRAsSd4EMxgBTP+ANa0hxW8ibAl2DIzR3UFAMBf3Gu1VefXEwAAXtsfSrADVc4vuNIAAAAASUVORK5CYII=)  
   
 **📌 Próximos Passos**](https://github.com/seu-usuario/forecast-vendas "https://github.com/seu-usuario/forecast-vendas")  
- Implementar modelo Prophet (Meta) para forecast mais sofisticado  
- Conectar dados ao Power BI via Python connector  
- Adicionar análise por segmento de cliente  
- Criar API REST para consumo do forecast em tempo real  
 ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANklEQVR4nO3OMQ2AABAAsSNhRgDCMMPyOlGADCywEZJWQZeZ2aszAAD+4l6rrTq+ngAA8Nr1AKKrBEE79VWHAAAAAElFTkSuQmCC)  
 **👤 Autor**  
   
 Gabriel Farias  
   
    
   
  Analista de Dados | SQL · Power BI · Oracle · Python  
   
 📧 [fariascompiuter@gmail.com  
   
  🔗 ](mailto:fariascompiuter@gmail.com "mailto:fariascompiuter@gmail.com")[https://www.linkedin.com/feed/update/urn:li:activity:7445188135988154368/  
   
  💻 https://www.linkedin.com/in/gabriel-paix%C3%A3o-3a4a7b285/  
 **forecast-vendas**](https://linkedin.com/in/seu-perfil "https://linkedin.com/in/seu-perfil")  
