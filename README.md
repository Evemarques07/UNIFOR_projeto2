# 📊 Sistema de Análise de Vendas

Sistema completo para análise de vendas de loja desenvolvido em Python. Permite registrar vendas, calcular estatísticas por vendedor, produto e período, além de gerar rankings, relatórios detalhados, CSVs de análise e gráficos visuais.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Objetivo

Desenvolver um sistema para análise de vendas que permita:
- Registrar vendas com validação de dados
- Calcular estatísticas de vendas por vendedor, produto e período
- Identificar produtos mais vendidos e melhores vendedores
- Gerar relatórios completos em texto, CSV e gráficos
- Analisar tendências temporais de vendas

## ✨ Funcionalidades

### 📈 Cadastro de Vendas
- ✅ Registrar vendas com validação automática
- ✅ Cálculo automático do valor total
- ✅ Geração de ID único para cada venda
- ✅ Seleção rápida de vendedores e produtos por número
- ✅ Sugestão automática de preços baseada no catálogo

### 👥 Análises por Vendedor
- ✅ Total de vendas por vendedor
- ✅ Quantidade de vendas realizadas
- ✅ Valor médio por venda
- ✅ Média de vendas por vendedor
- ✅ Ranking de melhores vendedores
- ✅ Produtos vendidos por vendedor

### 🛍️ Análises por Produto
- ✅ Total vendido por produto
- ✅ Quantidade vendida
- ✅ Receita gerada por produto
- ✅ Ranking de produtos mais vendidos

### 📅 Análises Temporais
- ✅ Vendas agrupadas por mês/ano
- ✅ Identificação do melhor mês
- ✅ Evolução temporal das vendas
- ✅ Comparação entre períodos

### 📋 Relatórios e Exportações
- ✅ Relatório geral completo
- ✅ Relatório específico por vendedor
- ✅ Exportação para CSV (análises gerais e específicas)
- ✅ Geração de gráficos automatizada

### 📊 Visualizações Gráficas
- 🔥 **Heatmap**: Quantidade de produtos vendidos por vendedor
- 📊 **Gráfico de Barras**: Total de vendas por vendedor
- 📈 **Gráfico de Colunas**: Vendas por ano por vendedor
- 🏆 **Top 10**: Produtos mais vendidos
- 📉 **Linha Temporal**: Evolução das vendas por mês
- 🥧 **Pizza**: Participação na receita por produto
- 📊 **Múltiplas Linhas**: Desempenho mensal por vendedor

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem principal
- **Pandas**: Manipulação e análise de dados
- **Matplotlib**: Geração de gráficos estáticos
- **Seaborn**: Visualizações estatísticas avançadas
- **NumPy**: Operações numéricas

## 📁 Estrutura do Projeto

```
projeto/
├── 📄 sistema_vendas.py          # Sistema principal
├── 📄 gerar_dataset.py           # Gerador de datasets sintéticos
├── 📄 demo.py                    # Demonstração do sistema
├── 📄 testes.py                  # Testes unitários
├── 📄 dataset_vendas.csv         # Dataset principal (1500+ registros)
├── 📄 vendas_exemplo.csv         # Dataset de exemplo menor
├── 📄 requirements.txt           # Dependências Python
├── 📄 README.md                  # Esta documentação
├── 📁 analises_csv/             # CSVs de análises (gerados automaticamente)
│   ├── analise_vendedores.csv
│   ├── analise_produtos.csv
│   ├── analise_mensal.csv
│   ├── ranking_vendedores.csv
│   ├── ranking_produtos.csv
│   ├── relatorio_geral.csv
│   └── vendas_completas.csv
├── 📁 graficos/                 # Gráficos PNG (gerados automaticamente)
│   ├── heatmap_vendedor_produto.png
│   ├── vendas_por_vendedor.png
│   ├── vendas_ano_vendedor.png
│   ├── top_produtos_quantidade.png
│   ├── evolucao_vendas_mes.png
│   ├── receita_produto_pizza.png
│   └── desempenho_mensal_vendedor.png
├── 📁 venv/                     # Ambiente virtual Python
└── 📁 relatorios/               # Relatórios em texto (gerados automaticamente)
```

## ⚙️ Instalação e Configuração

### 1. Clone o Repositório
```bash
git clone https://github.com/Evemarques07/UNIFOR_projeto2.git
cd UNIFOR_projeto2
```

### 2. Crie o Ambiente Virtual
```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o Sistema
```bash
python sistema_vendas.py
```

## 🚀 Como Usar

### Menu Principal

O sistema apresenta um menu interativo com as seguintes opções:

```
========================================
    SISTEMA DE ANÁLISE DE VENDAS
========================================
1. Registrar Nova Venda
2. Relatório Geral
3. Relatório por Vendedor
4. Ranking de Vendedores
5. Ranking de Produtos
6. Vendas por Mês
7. Carregar Dados de Exemplo
8. Listar Todas as Vendas
9. Listar Vendedores e Produtos
10. Carregar Dataset CSV
11. Gerar CSVs de Análises
12. Gerar CSV de Vendedor Específico
13. Gerar CSV com Todas as Vendas de um Vendedor
14. Gerar Gráficos de Análise
0. Sair
```

### Fluxo Recomendado

1. **Primeira execução**: Use a opção 10 para carregar o dataset CSV completo (1500+ registros)
2. **Visualizar dados**: Use a opção 2 para ver o relatório geral
3. **Análises específicas**: Use as opções 3-6 para análises detalhadas
4. **Exportar dados**: Use as opções 11-13 para gerar CSVs
5. **Visualizações**: Use a opção 14 para gerar gráficos

### Exemplos Práticos

#### Registrando uma Venda
```
Escolha uma opção: 1

--- PRODUTOS DISPONÍVEIS ---
1. NoteBook - R$ 3.000,00
2. Mouse - R$ 100,00
3. Teclado - R$ 150,00
...

Escolha o produto (número ou nome): 1
Produto selecionado: NoteBook
Valor sugerido: R$ 3.000,00

--- VENDEDORES DISPONÍVEIS ---
1. Maria
2. João
3. Ana
...

Escolha o vendedor (número ou nome): 1
Vendedor selecionado: Maria
Quantidade: 2
Usar valor sugerido R$ 3.000,00? (s/n): s
Data (YYYY-MM-DD): 2024-11-01

Venda registrada com sucesso! ID: 1501
Valor total: R$ 6.000,00
```

#### Exemplo de Relatório Geral
```
==================================================
         RELATÓRIO GERAL DE VENDAS
==================================================
Total Geral de Vendas: R$ 5.437.475,55
Quantidade de Vendas: 1500
Ticket Médio: R$ 3.624,98
Média de Vendas por Vendedor: R$ 1.087.495,11

--- TOP 5 VENDEDORES ---
1. Ana: R$ 1.123.456,78
2. João: R$ 1.087.234,56
3. Maria: R$ 1.076.543,21
4. Carlos: R$ 1.075.432,10
5. Beatriz: R$ 1.074.809,90

--- TOP 5 PRODUTOS ---
1. Pendrive: 156 unidades
2. Mouse: 154 unidades
3. Teclado: 148 unidades
4. Webcam: 147 unidades
5. Fone: 145 unidades

--- MELHOR MÊS ---
2024-08: R$ 234.567,89
```

## 📊 Datasets Inclusos

### Dataset Principal (dataset_vendas.csv)
- **Registros**: 1500+ vendas
- **Período**: 2021-01-01 a 2024-12-31
- **Vendedores**: Maria, João, Ana, Carlos, Beatriz
- **Produtos**: 9 produtos com preços variados
- **Valor Total**: ~R$ 5.4 milhões

### Dados de Exemplo (vendas_exemplo.csv)
- **Registros**: 20 vendas de demonstração
- **Período**: Janeiro a Março 2024
- **Uso**: Testes rápidos e demonstrações

## 📈 Tipos de Análises Disponíveis

### 1. Análises por Vendedor
- Total de vendas em valor
- Quantidade de transações
- Ticket médio por venda
- Média de vendas entre todos os vendedores
- Produtos vendidos por vendedor
- Histórico detalhado de vendas

### 2. Análises por Produto
- Receita total por produto
- Quantidade vendida
- Participação no faturamento
- Ranking de popularidade

### 3. Análises Temporais
- Vendas mensais e anuais
- Sazonalidade de vendas
- Tendências de crescimento
- Identificação de picos e vales

### 4. Análises Cruzadas
- Heatmap vendedor vs produto
- Performance mensal por vendedor
- Evolução temporal por categoria

## 🎨 Gráficos Gerados

O sistema gera automaticamente 7 tipos de gráficos:

1. **Heatmap Vendedor x Produto**: Mostra a quantidade de cada produto vendido por cada vendedor
2. **Barras - Vendas por Vendedor**: Total de vendas em valor por vendedor
3. **Colunas - Vendas Anuais**: Comparação de vendas por ano e vendedor
4. **Barras - Top 10 Produtos**: Produtos mais vendidos em quantidade
5. **Linha - Evolução Temporal**: Evolução das vendas mês a mês
6. **Pizza - Receita por Produto**: Participação percentual na receita
7. **Múltiplas Linhas - Performance Mensal**: Desempenho de cada vendedor ao longo do tempo

## 💾 Exportações CSV

O sistema permite exportar dados em múltiplos formatos CSV:

### Análises Gerais
- `analise_vendedores.csv`: Estatísticas completas por vendedor
- `analise_produtos.csv`: Estatísticas completas por produto
- `analise_mensal.csv`: Vendas agrupadas por mês
- `ranking_vendedores.csv`: Ranking ordenado de vendedores
- `ranking_produtos.csv`: Ranking ordenado de produtos
- `relatorio_geral.csv`: Resumo executivo geral
- `vendas_completas.csv`: Dataset completo de vendas

### Análises Específicas por Vendedor
- `vendedor_[nome]_resumo.csv`: Resumo estatístico
- `vendedor_[nome]_produtos.csv`: Produtos vendidos
- `vendedor_[nome]_detalhado.csv`: Todas as vendas detalhadas
- `todas_vendas_[nome].csv`: Histórico completo ordenado

## 🧪 Testes

Execute os testes unitários para verificar a integridade do sistema:

```bash
python testes.py
```

O sistema inclui testes para:
- Validação de entrada de dados
- Cálculos de estatísticas
- Funções de formatação
- Geração de rankings
- Operações de arquivo

## 🔧 Estrutura de Dados

### Venda Individual
```python
venda = {
    'id': 1,
    'produto': 'NoteBook',
    'vendedor': 'Maria',
    'quantidade': 2,
    'valor_unitario': 3000.00,
    'valor_total': 6000.00,
    'data': '2024-11-01'
}
```

### Catálogo de Produtos
```python
produtos = [
    {"Nome": "NoteBook", "Preco": 3000},
    {"Nome": "Mouse", "Preco": 100},
    {"Nome": "Teclado", "Preco": 150},
    {"Nome": "Monitor", "Preco": 800},
    {"Nome": "Webcam", "Preco": 200},
    {"Nome": "Fone", "Preco": 250},
    {"Nome": "Impressora", "Preco": 1200},
    {"Nome": "HD Externo", "Preco": 400},
    {"Nome": "Pendrive", "Preco": 80}
]
```

### Vendedores Cadastrados
```python
vendedores = ["Maria", "João", "Ana", "Carlos", "Beatriz"]
```

### Estrutura do Relatório Geral
```python
relatorio = {
    'total_geral': 5437475.55,
    'quantidade_vendas': 1500,
    'vendedores': {...},  # Dados detalhados por vendedor
    'produtos': {...},    # Dados detalhados por produto
    'meses': {...},       # Vendas por mês
    'top_vendedores': [...],  # Ranking dos vendedores
    'top_produtos': [...],    # Ranking dos produtos
    'melhor_mes': '2024-08',
    'valor_melhor_mes': 234567.89,
    'media_vendas_por_vendedor': 1087495.11  # Nova funcionalidade
}
```

## ⚡ Principais Funções

### Cadastro e Validação
- `registrar_venda()`: Registra nova venda com validações
- `carregar_csv()`: Carrega dataset de arquivo CSV
- `carregar_dados_exemplo()`: Carrega dados de demonstração

### Cálculos e Estatísticas
- `calcular_total_vendas()`: Total geral de vendas
- `calcular_vendas_por_vendedor()`: Estatísticas por vendedor
- `calcular_vendas_por_produto()`: Estatísticas por produto
- `calcular_vendas_por_mes()`: Vendas agrupadas por mês

### Rankings e Análises
- `ranking_vendedores()`: Top vendedores por valor
- `ranking_produtos()`: Top produtos por quantidade
- `melhor_mes()`: Mês com maior volume de vendas

### Relatórios
- `gerar_relatorio_geral()`: Relatório completo
- `gerar_relatorio_vendedor()`: Relatório específico
- `exibir_relatorio_vendas()`: Exibição formatada

### Exportações
- `gerar_csvs_analises()`: Gera todos os CSVs de análise
- `gerar_csv_vendedor_especifico()`: CSV específico de vendedor
- `gerar_csv_todas_vendas_vendedor()`: Histórico completo
- `gerar_graficos()`: Gera todos os gráficos visuais

### Utilitários
- `formatar_moeda()`: Formatação monetária brasileira
- `extrair_mes()`: Extração de mês da data
- `listar_vendedores()`: Lista vendedores disponíveis
- `listar_produtos()`: Lista produtos do catálogo

## 🛡️ Validações Implementadas

- ✅ Produto e vendedor obrigatórios
- ✅ Quantidade deve ser maior que zero
- ✅ Valor unitário deve ser maior que zero
- ✅ Verificação de vendedor existente
- ✅ Tratamento de divisão por zero
- ✅ Validação de formato de data
- ✅ Verificação de arquivos CSV

## 🎓 Recursos Técnicos Utilizados

- **Tipos de dados**: int, float, str, dict, list
- **Estruturas de controle**: if/else, for, while
- **Funções**: com parâmetros e retorno
- **List comprehension**: para filtragem e transformação
- **Dict comprehension**: para agrupamento de dados
- **Funções lambda**: com map, filter, sorted
- **Tratamento de exceções**: try/except
- **Formatação de strings**: f-strings
- **Operações com arquivos**: CSV, criação de diretórios
- **Visualização de dados**: matplotlib, seaborn

## 🔍 Análise de Performance

### Dataset Principal
- **Registros**: 1.500 vendas
- **Período**: 4 anos (2021-2024)
- **Volume**: ~R$ 5,4 milhões
- **Processamento**: < 1 segundo para análises
- **Gráficos**: ~5-10 segundos para geração completa

### Escalabilidade
- Suporta até 100k registros sem problemas de performance
- Geração de CSVs otimizada com pandas
- Gráficos em alta resolução (300 DPI)

## 🚨 Troubleshooting

### Erro de Política de Execução (Windows)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Erro de Importação de Bibliotecas
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Erro de Geração de Gráficos
- Verifique se matplotlib e seaborn estão instalados
- Em ambientes sem interface gráfica, o sistema usa backend 'Agg'

### Arquivo CSV Não Encontrado
- Execute `python gerar_dataset.py` para gerar novo dataset
- Verifique se o arquivo está na pasta correta

## 📈 Roadmap Futuro

### ✅ Atualizações Recentes
- [x] **Média de Vendas por Vendedor**: Adicionado cálculo da média de vendas por vendedor no relatório geral
- [x] **Tratamento de Divisão por Zero**: Implementado proteção contra divisão por zero no cálculo da média

### 🔮 Próximas Funcionalidades
- [ ] Interface web com Flask/Django
- [ ] Dashboard interativo com Plotly/Dash
- [ ] Integração com banco de dados (SQLite/PostgreSQL)
- [ ] API REST para integração externa
- [ ] Análises preditivas com Machine Learning
- [ ] Alertas automáticos de performance
- [ ] Relatórios em PDF automatizados
- [ ] Integração com sistemas ERP

## 👨‍💻 Desenvolvimento

### Para Contribuir
1. Fork o repositório
2. Crie uma branch feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Add nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

### Convenções de Código
- Siga PEP 8 para estilo Python
- Adicione docstrings para funções públicas
- Inclua testes para novas funcionalidades
- Mantenha compatibilidade com Python 3.8+

## 📄 Licença

Este projeto é de uso educacional e pode ser modificado livremente para fins acadêmicos.

## 👨‍🎓 Autor

Desenvolvido como projeto acadêmico para MBA em Inteligência Artificial - UNIFOR

---

**📧 Suporte**: Para dúvidas ou sugestões, abra uma [issue](https://github.com/Evemarques07/UNIFOR_projeto2/issues) no repositório.

**⭐ Gostou do projeto?** Deixe uma estrela no repositório!
