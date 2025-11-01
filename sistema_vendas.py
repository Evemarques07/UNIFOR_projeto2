vendas = []
contador_id = 1
vendedores = ["Maria", "João", "Ana", "Carlos", "Beatriz"]
produtos = [{"Nome": "NoteBook", "Preco": 3000}, 
            {"Nome": "Mouse", "Preco": 100}, 
            {"Nome": "Teclado", "Preco": 150}, 
            {"Nome": "Monitor", "Preco": 800}, 
            {"Nome": "Webcam", "Preco": 200}, 
            {"Nome": "Fone", "Preco": 250}, 
            {"Nome": "Impressora", "Preco": 1200}, 
            {"Nome": "HD Externo", "Preco": 400}, 
            {"Nome": "Pendrive", "Preco": 80}
            ]



def registrar_venda(produto, vendedor, quantidade, valor_unitario, data):
    global contador_id
    
    if not produto or not vendedor:
        raise ValueError("Produto e vendedor são obrigatórios")
    if quantidade <= 0:
        raise ValueError("Quantidade deve ser maior que zero")
    if valor_unitario <= 0:
        raise ValueError("Valor unitário deve ser maior que zero")
    
    valor_total = quantidade * valor_unitario
    
    venda = {
        'id': contador_id,
        'produto': produto,
        'vendedor': vendedor,
        'quantidade': quantidade,
        'valor_unitario': valor_unitario,
        'valor_total': valor_total,
        'data': data
    }
    
    vendas.append(venda)
    contador_id += 1
    
    return venda

def calcular_total_vendas():
    return sum([venda['valor_total'] for venda in vendas])

def calcular_vendas_por_vendedor():
    vendedores = {}
    
    for venda in vendas:
        vendedor = venda['vendedor']
        if vendedor not in vendedores:
            vendedores[vendedor] = {
                'total_vendas': 0,
                'quantidade_vendas': 0,
                'valor_medio': 0
            }
        
        vendedores[vendedor]['total_vendas'] += venda['valor_total']
        vendedores[vendedor]['quantidade_vendas'] += 1
    
    for vendedor in vendedores:
        if vendedores[vendedor]['quantidade_vendas'] > 0:
            vendedores[vendedor]['valor_medio'] = (
                vendedores[vendedor]['total_vendas'] / 
                vendedores[vendedor]['quantidade_vendas']
            )
    
    return vendedores


def calcular_vendas_por_produto():
    produtos = {}
    
    for venda in vendas:
        produto = venda['produto']
        if produto not in produtos:
            produtos[produto] = {
                'total_vendido': 0,
                'quantidade_vendida': 0,
                'receita': 0
            }
        
        produtos[produto]['total_vendido'] += venda['valor_total']
        produtos[produto]['quantidade_vendida'] += venda['quantidade']
        produtos[produto]['receita'] += venda['valor_total']
    
    return produtos

def calcular_vendas_por_mes():
    meses = {}
    
    for venda in vendas:
        mes = extrair_mes(venda['data'])
        if mes not in meses:
            meses[mes] = 0
        meses[mes] += venda['valor_total']
    
    return meses

def ranking_vendedores(limite=5):
    vendas_vendedor = calcular_vendas_por_vendedor()
    ranking = [(vendedor, dados['total_vendas']) 
               for vendedor, dados in vendas_vendedor.items()]
    ranking_ordenado = sorted(ranking, key=lambda x: x[1], reverse=True)
    return ranking_ordenado[:limite]

def ranking_produtos(limite=5):
    vendas_produto = calcular_vendas_por_produto()
    ranking = [(produto, dados['quantidade_vendida']) 
               for produto, dados in vendas_produto.items()]
    ranking_ordenado = sorted(ranking, key=lambda x: x[1], reverse=True)
    return ranking_ordenado[:limite]

def melhor_mes():
    vendas_mes = calcular_vendas_por_mes()
    if not vendas_mes:
        return None, 0
    
    melhor = max(vendas_mes.items(), key=lambda x: x[1])
    return melhor

def gerar_relatorio_geral():
    total_vendas = calcular_total_vendas()
    vendas_vendedor = calcular_vendas_por_vendedor()
    vendas_produto = calcular_vendas_por_produto()
    vendas_mes = calcular_vendas_por_mes()
    top_vendedores = ranking_vendedores(5)
    top_produtos = ranking_produtos(5)
    mes_destaque, valor_mes = melhor_mes()
    
    # Calcular média de vendas por vendedor
    num_vendedores = len(vendas_vendedor) if vendas_vendedor else 0
    media_vendas_por_vendedor = total_vendas / num_vendedores if num_vendedores > 0 else 0
    
    relatorio = {
        'total_geral': total_vendas,
        'quantidade_vendas': len(vendas),
        'vendedores': vendas_vendedor,
        'produtos': vendas_produto,
        'meses': vendas_mes,
        'top_vendedores': top_vendedores,
        'top_produtos': top_produtos,
        'melhor_mes': mes_destaque,
        'valor_melhor_mes': valor_mes,
        'media_vendas_por_vendedor': media_vendas_por_vendedor
    }
    
    return relatorio

def gerar_relatorio_vendedor(nome_vendedor):
    vendas_vendedor = [venda for venda in vendas if venda['vendedor'] == nome_vendedor]
    
    if not vendas_vendedor:
        return None
    
    total = sum([venda['valor_total'] for venda in vendas_vendedor])
    quantidade = len(vendas_vendedor)
    media = total / quantidade if quantidade > 0 else 0
    
    produtos_vendidos = {}
    for venda in vendas_vendedor:
        produto = venda['produto']
        if produto not in produtos_vendidos:
            produtos_vendidos[produto] = 0
        produtos_vendidos[produto] += venda['quantidade']
    
    relatorio = {
        'vendedor': nome_vendedor,
        'total_vendas': total,
        'quantidade_vendas': quantidade,
        'valor_medio': media,
        'produtos_vendidos': produtos_vendidos,
        'vendas_detalhadas': vendas_vendedor
    }
    
    return relatorio

def exibir_relatorio_vendas():
    if not vendas:
        print("Nenhuma venda registrada ainda.")
        print("\nOpções para carregar dados:")
        print("1. Use a opção 7 para carregar dados de exemplo")
        print("2. Use a opção 10 para carregar dataset CSV")
        return
    
    relatorio = gerar_relatorio_geral()
    
    print("=" * 50)
    print("         RELATÓRIO GERAL DE VENDAS")
    print("=" * 50)
    print(f"Total Geral de Vendas: {formatar_moeda(relatorio['total_geral'])}")
    print(f"Quantidade de Vendas: {relatorio['quantidade_vendas']}")
    print(f"Ticket Médio: {formatar_moeda(relatorio['total_geral'] / relatorio['quantidade_vendas'])}")
    
    print("\n--- TOP 5 VENDEDORES ---")
    for i, (vendedor, total) in enumerate(relatorio['top_vendedores'], 1):
        print(f"{i}. {vendedor}: {formatar_moeda(total)}")
    
    print("\n--- TOP 5 PRODUTOS ---")
    for i, (produto, quantidade) in enumerate(relatorio['top_produtos'], 1):
        print(f"{i}. {produto}: {quantidade} unidades")
    
    if relatorio['melhor_mes']:
        print(f"\n--- MELHOR MÊS ---")
        print(f"{relatorio['melhor_mes']}: {formatar_moeda(relatorio['valor_melhor_mes'])}")

def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def extrair_mes(data):
    return data[:7]

def carregar_csv():
    try:
        import pandas as pd
        df = pd.read_csv('dataset_vendas.csv')
        global vendas, contador_id
        vendas.clear()
        contador_id = 1
        
        for _, row in df.iterrows():
            venda = {
                'id': int(row['id']),
                'produto': row['produto'],
                'vendedor': row['vendedor'],
                'quantidade': int(row['quantidade']),
                'valor_unitario': float(row['valor_unitario']),
                'valor_total': float(row['valor_total']),
                'data': row['data']
            }
            vendas.append(venda)
        
        contador_id = len(vendas) + 1
        print(f"Carregados {len(vendas)} registros do CSV")
        return True
    except Exception as e:
        print(f"Erro ao carregar CSV: {e}")
        return False

def gerar_csvs_analises():
    import os
    import pandas as pd
    
    pasta_csv = "analises_csv"
    if not os.path.exists(pasta_csv):
        os.makedirs(pasta_csv)
    
    if not vendas:
        print("Nenhuma venda registrada. Carregue dados primeiro.")
        return False
    
    try:
        vendas_vendedor = calcular_vendas_por_vendedor()
        df_vendedores = pd.DataFrame([
            {
                'vendedor': vendedor,
                'total_vendas': dados['total_vendas'],
                'quantidade_vendas': dados['quantidade_vendas'],
                'valor_medio': dados['valor_medio']
            }
            for vendedor, dados in vendas_vendedor.items()
        ])
        df_vendedores = df_vendedores.sort_values('total_vendas', ascending=False)
        df_vendedores.to_csv(f"{pasta_csv}/analise_vendedores.csv", index=False, encoding='utf-8')
        
        vendas_produto = calcular_vendas_por_produto()
        df_produtos = pd.DataFrame([
            {
                'produto': produto,
                'total_vendido': dados['total_vendido'],
                'quantidade_vendida': dados['quantidade_vendida'],
                'receita': dados['receita']
            }
            for produto, dados in vendas_produto.items()
        ])
        df_produtos = df_produtos.sort_values('quantidade_vendida', ascending=False)
        df_produtos.to_csv(f"{pasta_csv}/analise_produtos.csv", index=False, encoding='utf-8')
        
        vendas_mes = calcular_vendas_por_mes()
        df_meses = pd.DataFrame([
            {
                'mes': mes,
                'total_vendas': total
            }
            for mes, total in sorted(vendas_mes.items())
        ])
        df_meses.to_csv(f"{pasta_csv}/analise_mensal.csv", index=False, encoding='utf-8')
        
        ranking_vend = ranking_vendedores(10)
        df_ranking_vend = pd.DataFrame(ranking_vend, columns=['vendedor', 'total_vendas'])
        df_ranking_vend['posicao'] = range(1, len(df_ranking_vend) + 1)
        df_ranking_vend = df_ranking_vend[['posicao', 'vendedor', 'total_vendas']]
        df_ranking_vend.to_csv(f"{pasta_csv}/ranking_vendedores.csv", index=False, encoding='utf-8')
        
        ranking_prod = ranking_produtos(10)
        df_ranking_prod = pd.DataFrame(ranking_prod, columns=['produto', 'quantidade_vendida'])
        df_ranking_prod['posicao'] = range(1, len(df_ranking_prod) + 1)
        df_ranking_prod = df_ranking_prod[['posicao', 'produto', 'quantidade_vendida']]
        df_ranking_prod.to_csv(f"{pasta_csv}/ranking_produtos.csv", index=False, encoding='utf-8')
        
        relatorio_geral = gerar_relatorio_geral()
        df_geral = pd.DataFrame([{
            'total_geral': relatorio_geral['total_geral'],
            'quantidade_vendas': relatorio_geral['quantidade_vendas'],
            'ticket_medio': relatorio_geral['total_geral'] / relatorio_geral['quantidade_vendas'],
            'melhor_mes': relatorio_geral['melhor_mes'],
            'valor_melhor_mes': relatorio_geral['valor_melhor_mes']
        }])
        df_geral.to_csv(f"{pasta_csv}/relatorio_geral.csv", index=False, encoding='utf-8')
        
        df_vendas_completas = pd.DataFrame(vendas)
        df_vendas_completas.to_csv(f"{pasta_csv}/vendas_completas.csv", index=False, encoding='utf-8')
        
        print(f"\nArquivos CSV gerados na pasta '{pasta_csv}':")
        print("- analise_vendedores.csv")
        print("- analise_produtos.csv") 
        print("- analise_mensal.csv")
        print("- ranking_vendedores.csv")
        print("- ranking_produtos.csv")
        print("- relatorio_geral.csv")
        print("- vendas_completas.csv")
        
        return True
        
    except Exception as e:
        print(f"Erro ao gerar CSVs: {e}")
        return False

def gerar_csv_vendedor_especifico(nome_vendedor):
    import os
    import pandas as pd
    
    pasta_csv = "analises_csv"
    if not os.path.exists(pasta_csv):
        os.makedirs(pasta_csv)
    
    relatorio = gerar_relatorio_vendedor(nome_vendedor)
    if not relatorio:
        print(f"Vendedor '{nome_vendedor}' não encontrado.")
        return False
    
    try:
        df_vendedor = pd.DataFrame([{
            'vendedor': relatorio['vendedor'],
            'total_vendas': relatorio['total_vendas'],
            'quantidade_vendas': relatorio['quantidade_vendas'],
            'valor_medio': relatorio['valor_medio']
        }])
        
        df_produtos_vendedor = pd.DataFrame([
            {
                'produto': produto,
                'quantidade': qtd
            }
            for produto, qtd in relatorio['produtos_vendidos'].items()
        ])
        
        df_vendas_detalhadas = pd.DataFrame(relatorio['vendas_detalhadas'])
        
        nome_arquivo_base = nome_vendedor.replace(' ', '_').lower()
        df_vendedor.to_csv(f"{pasta_csv}/vendedor_{nome_arquivo_base}_resumo.csv", index=False, encoding='utf-8')
        df_produtos_vendedor.to_csv(f"{pasta_csv}/vendedor_{nome_arquivo_base}_produtos.csv", index=False, encoding='utf-8')
        df_vendas_detalhadas.to_csv(f"{pasta_csv}/vendedor_{nome_arquivo_base}_detalhado.csv", index=False, encoding='utf-8')
        
        print(f"\nArquivos CSV do vendedor '{nome_vendedor}' gerados:")
        print(f"- vendedor_{nome_arquivo_base}_resumo.csv")
        print(f"- vendedor_{nome_arquivo_base}_produtos.csv")
        print(f"- vendedor_{nome_arquivo_base}_detalhado.csv")
        
        return True
        
    except Exception as e:
        print(f"Erro ao gerar CSV do vendedor: {e}")
        return False

def gerar_csv_todas_vendas_vendedor(nome_vendedor):
    import os
    import pandas as pd
    
    pasta_csv = "analises_csv"
    if not os.path.exists(pasta_csv):
        os.makedirs(pasta_csv)
    
    vendas_vendedor = [venda for venda in vendas if venda['vendedor'] == nome_vendedor]
    
    if not vendas_vendedor:
        print(f"Nenhuma venda encontrada para o vendedor '{nome_vendedor}'.")
        return False
    
    try:
        df_todas_vendas = pd.DataFrame(vendas_vendedor)
        df_todas_vendas = df_todas_vendas.sort_values('data')
        
        nome_arquivo_base = nome_vendedor.replace(' ', '_').lower()
        nome_arquivo = f"{pasta_csv}/todas_vendas_{nome_arquivo_base}.csv"
        df_todas_vendas.to_csv(nome_arquivo, index=False, encoding='utf-8')
        
        total_vendas = sum([venda['valor_total'] for venda in vendas_vendedor])
        
        print(f"\nCSV gerado: todas_vendas_{nome_arquivo_base}.csv")
        print(f"Total de registros: {len(vendas_vendedor)}")
        print(f"Valor total das vendas: {formatar_moeda(total_vendas)}")
        print(f"Período: {min([v['data'] for v in vendas_vendedor])} a {max([v['data'] for v in vendas_vendedor])}")
        
        return True
        
    except Exception as e:
        print(f"Erro ao gerar CSV de todas as vendas: {e}")
        return False

def gerar_graficos():
    import os
    import pandas as pd
    
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import seaborn as sns
        import numpy as np
    except ImportError as e:
        print(f"Erro: Bibliotecas necessárias não encontradas - {e}")
        print("Execute: pip install matplotlib seaborn")
        return False
    
    pasta_graficos = "graficos"
    if not os.path.exists(pasta_graficos):
        os.makedirs(pasta_graficos)
    
    if not vendas:
        print("Nenhuma venda registrada. Carregue dados primeiro.")
        return False
    
    try:
        plt.style.use('default')
        sns.set_palette("husl")
        
        df_vendas = pd.DataFrame(vendas)
        df_vendas['ano'] = df_vendas['data'].str[:4]
        df_vendas['mes'] = df_vendas['data'].str[:7]
        
        heatmap_data = df_vendas.groupby(['vendedor', 'produto'])['quantidade'].sum().unstack(fill_value=0)
        
        plt.figure(figsize=(12, 8))
        sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlOrRd', cbar_kws={'label': 'Quantidade Vendida'})
        plt.title('Mapa de Calor: Quantidade de Produtos Vendidos por Vendedor', fontsize=14, fontweight='bold')
        plt.xlabel('Produtos', fontsize=12)
        plt.ylabel('Vendedores', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'{pasta_graficos}/heatmap_vendedor_produto.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        vendas_vendedor = df_vendas.groupby('vendedor')['valor_total'].sum().sort_values(ascending=False)
        plt.figure(figsize=(10, 6))
        bars = plt.bar(vendas_vendedor.index, vendas_vendedor.values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57'])
        plt.title('Total de Vendas por Vendedor', fontsize=14, fontweight='bold')
        plt.xlabel('Vendedores', fontsize=12)
        plt.ylabel('Valor Total (R$)', fontsize=12)
        plt.xticks(rotation=45)
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'R$ {height:,.0f}'.replace(',', '.'), 
                    ha='center', va='bottom', fontsize=10)
        plt.tight_layout()
        plt.savefig(f'{pasta_graficos}/vendas_por_vendedor.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        vendas_ano_vendedor = df_vendas.groupby(['ano', 'vendedor'])['valor_total'].sum().unstack(fill_value=0)
        plt.figure(figsize=(12, 8))
        vendas_ano_vendedor.plot(kind='bar', stacked=False, figsize=(12, 8))
        plt.title('Vendas por Ano por Vendedor', fontsize=14, fontweight='bold')
        plt.xlabel('Ano', fontsize=12)
        plt.ylabel('Valor Total (R$)', fontsize=12)
        plt.legend(title='Vendedores', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig(f'{pasta_graficos}/vendas_ano_vendedor.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        produtos_vendidos = df_vendas.groupby('produto')['quantidade'].sum().sort_values(ascending=False).head(10)
        plt.figure(figsize=(12, 6))
        bars = plt.bar(range(len(produtos_vendidos)), produtos_vendidos.values, color='skyblue')
        plt.title('Top 10 Produtos Mais Vendidos (Quantidade)', fontsize=14, fontweight='bold')
        plt.xlabel('Produtos', fontsize=12)
        plt.ylabel('Quantidade Vendida', fontsize=12)
        plt.xticks(range(len(produtos_vendidos)), produtos_vendidos.index, rotation=45, ha='right')
        for i, bar in enumerate(bars):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}', ha='center', va='bottom', fontsize=10)
        plt.tight_layout()
        plt.savefig(f'{pasta_graficos}/top_produtos_quantidade.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        vendas_mes = df_vendas.groupby('mes')['valor_total'].sum()
        plt.figure(figsize=(14, 6))
        plt.plot(vendas_mes.index, vendas_mes.values, marker='o', linewidth=2, markersize=6, color='#FF6B6B')
        plt.title('Evolução das Vendas por Mês', fontsize=14, fontweight='bold')
        plt.xlabel('Mês', fontsize=12)
        plt.ylabel('Valor Total (R$)', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        for i, v in enumerate(vendas_mes.values):
            if i % 3 == 0:
                plt.text(vendas_mes.index[i], v, f'R$ {v:,.0f}'.replace(',', '.'), 
                        ha='center', va='bottom', fontsize=8)
        plt.tight_layout()
        plt.savefig(f'{pasta_graficos}/evolucao_vendas_mes.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        receita_produto = df_vendas.groupby('produto')['valor_total'].sum().sort_values(ascending=False).head(8)
        plt.figure(figsize=(10, 10))
        colors = plt.cm.Set3(np.linspace(0, 1, len(receita_produto)))
        wedges, texts, autotexts = plt.pie(receita_produto.values, labels=receita_produto.index, 
                                          autopct='%1.1f%%', startangle=90, colors=colors)
        plt.title('Participação na Receita por Produto', fontsize=14, fontweight='bold')
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        plt.tight_layout()
        plt.savefig(f'{pasta_graficos}/receita_produto_pizza.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        vendedor_mes = df_vendas.groupby(['mes', 'vendedor'])['valor_total'].sum().unstack(fill_value=0)
        plt.figure(figsize=(16, 8))
        for vendedor in vendedor_mes.columns:
            plt.plot(vendedor_mes.index, vendedor_mes[vendedor], marker='o', label=vendedor, linewidth=2)
        plt.title('Desempenho Mensal por Vendedor', fontsize=14, fontweight='bold')
        plt.xlabel('Mês', fontsize=12)
        plt.ylabel('Valor Total (R$)', fontsize=12)
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'{pasta_graficos}/desempenho_mensal_vendedor.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"\nGráficos gerados na pasta '{pasta_graficos}':")
        print("- heatmap_vendedor_produto.png")
        print("- vendas_por_vendedor.png")
        print("- vendas_ano_vendedor.png")
        print("- top_produtos_quantidade.png")
        print("- evolucao_vendas_mes.png")
        print("- receita_produto_pizza.png")
        print("- desempenho_mensal_vendedor.png")
        
        return True
        
    except Exception as e:
        print(f"Erro ao gerar gráficos: {e}")
        import traceback
        traceback.print_exc()
        return False

def listar_vendedores():
    print("\n--- VENDEDORES DISPONÍVEIS ---")
    for i, vendedor in enumerate(vendedores, 1):
        print(f"{i}. {vendedor}")
    return vendedores

def listar_produtos():
    print("\n--- PRODUTOS DISPONÍVEIS ---")
    for i, produto in enumerate(produtos, 1):
        print(f"{i}. {produto['Nome']} - R$ {produto['Preco']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    return produtos

def obter_vendedor_por_numero(numero):
    try:
        numero = int(numero)
        if 1 <= numero <= len(vendedores):
            return vendedores[numero - 1]
        else:
            return None
    except ValueError:
        return None

def obter_produto_por_numero(numero):
    try:
        numero = int(numero)
        if 1 <= numero <= len(produtos):
            return produtos[numero - 1]
        else:
            return None
    except ValueError:
        return None

def carregar_dados_exemplo():
    dados_exemplo = [
        ('Notebook Dell', 'Maria Silva', 2, 3500.00, '2024-01-15'),
        ('Mouse Logitech', 'João Santos', 5, 89.90, '2024-01-16'),
        ('Teclado Mecânico', 'Maria Silva', 3, 250.00, '2024-01-17'),
        ('Monitor Samsung', 'Ana Costa', 1, 1200.00, '2024-01-18'),
        ('Webcam HD', 'João Santos', 2, 150.00, '2024-01-19'),
        ('Notebook Dell', 'Ana Costa', 1, 3500.00, '2024-01-20'),
        ('Fone Bluetooth', 'Maria Silva', 4, 120.00, '2024-02-01'),
        ('Impressora HP', 'João Santos', 1, 800.00, '2024-02-02'),
        ('HD Externo', 'Ana Costa', 3, 300.00, '2024-02-03'),
        ('Pendrive 64GB', 'Maria Silva', 10, 45.00, '2024-02-05')
    ]
    
    for produto, vendedor, quantidade, valor_unitario, data in dados_exemplo:
        registrar_venda(produto, vendedor, quantidade, valor_unitario, data)
    
    print(f"Carregados {len(dados_exemplo)} registros de exemplo.")

def menu_interativo():
    while True:
        print("\n" + "=" * 40)
        print("    SISTEMA DE ANÁLISE DE VENDAS")
        print("=" * 40)
        print("1. Registrar Nova Venda")
        print("2. Relatório Geral")
        print("3. Relatório por Vendedor")
        print("4. Ranking de Vendedores")
        print("5. Ranking de Produtos")
        print("6. Vendas por Mês")
        print("7. Carregar Dados de Exemplo")
        print("8. Listar Todas as Vendas")
        print("9. Listar Vendedores e Produtos")
        print("10. Carregar Dataset CSV")
        print("11. Gerar CSVs de Análises")
        print("12. Gerar CSV de Vendedor Específico")
        print("13. Gerar CSV com Todas as Vendas de um Vendedor")
        print("14. Gerar Gráficos de Análise")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '1':
            try:
                print("\n--- REGISTRAR NOVA VENDA ---")
                
                listar_produtos()
                produto_escolha = input("\nEscolha o produto (número ou nome): ").strip()
                
                produto_obj = obter_produto_por_numero(produto_escolha)
                if produto_obj:
                    produto = produto_obj['Nome']
                    valor_sugerido = produto_obj['Preco']
                    print(f"Produto selecionado: {produto}")
                    print(f"Valor sugerido: R$ {valor_sugerido:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
                else:
                    produto = produto_escolha
                    valor_sugerido = None
                
                listar_vendedores()
                vendedor_escolha = input("\nEscolha o vendedor (número ou nome): ").strip()
                
                vendedor_selecionado = obter_vendedor_por_numero(vendedor_escolha)
                if vendedor_selecionado:
                    vendedor = vendedor_selecionado
                    print(f"Vendedor selecionado: {vendedor}")
                else:
                    vendedor = vendedor_escolha
                
                quantidade = int(input("Quantidade: "))
                
                if valor_sugerido:
                    usar_sugerido = input(f"Usar valor sugerido R$ {valor_sugerido:,.2f}? (s/n): ".replace(',', 'X').replace('.', ',').replace('X', '.')).strip().lower()
                    if usar_sugerido == 's' or usar_sugerido == 'sim':
                        valor_unitario = valor_sugerido
                    else:
                        valor_unitario = float(input("Valor unitário: R$ "))
                else:
                    valor_unitario = float(input("Valor unitário: R$ "))
                
                data = input("Data (YYYY-MM-DD): ").strip()
                
                venda = registrar_venda(produto, vendedor, quantidade, valor_unitario, data)
                print(f"\nVenda registrada com sucesso! ID: {venda['id']}")
                print(f"Valor total: {formatar_moeda(venda['valor_total'])}")
                
            except ValueError as e:
                print(f"Erro: {e}")
            except Exception as e:
                print(f"Erro inesperado: {e}")
        
        elif opcao == '2':
            exibir_relatorio_vendas()
        
        elif opcao == '3':
            nome = input("Nome do vendedor: ").strip()
            relatorio = gerar_relatorio_vendedor(nome)
            
            if relatorio:
                print(f"\n--- RELATÓRIO DE {relatorio['vendedor'].upper()} ---")
                print(f"Total de Vendas: {formatar_moeda(relatorio['total_vendas'])}")
                print(f"Quantidade de Vendas: {relatorio['quantidade_vendas']}")
                print(f"Valor Médio por Venda: {formatar_moeda(relatorio['valor_medio'])}")
                
                print("\nProdutos Vendidos:")
                for produto, qtd in relatorio['produtos_vendidos'].items():
                    print(f"  {produto}: {qtd} unidades")
            else:
                print("Vendedor não encontrado.")
        
        elif opcao == '4':
            top_vendedores = ranking_vendedores(10)
            print("\n--- RANKING DE VENDEDORES ---")
            for i, (vendedor, total) in enumerate(top_vendedores, 1):
                print(f"{i}. {vendedor}: {formatar_moeda(total)}")
        
        elif opcao == '5':
            top_produtos = ranking_produtos(10)
            print("\n--- RANKING DE PRODUTOS ---")
            for i, (produto, quantidade) in enumerate(top_produtos, 1):
                print(f"{i}. {produto}: {quantidade} unidades")
        
        elif opcao == '6':
            vendas_mes = calcular_vendas_por_mes()
            print("\n--- VENDAS POR MÊS ---")
            for mes in sorted(vendas_mes.keys()):
                print(f"{mes}: {formatar_moeda(vendas_mes[mes])}")
        
        elif opcao == '7':
            carregar_dados_exemplo()
        
        elif opcao == '8':
            if vendas:
                print("\n--- TODAS AS VENDAS ---")
                for venda in vendas:
                    print(f"ID {venda['id']}: {venda['produto']} - {venda['vendedor']} - "
                          f"{venda['quantidade']}un x {formatar_moeda(venda['valor_unitario'])} = "
                          f"{formatar_moeda(venda['valor_total'])} ({venda['data']})")
            else:
                print("Nenhuma venda registrada.")
        
        elif opcao == '9':
            print("\n" + "=" * 40)
            print("    VENDEDORES E PRODUTOS CADASTRADOS")
            print("=" * 40)
            listar_vendedores()
            listar_produtos()
        
        elif opcao == '10':
            print("\n--- CARREGAR DATASET CSV ---")
            if carregar_csv():
                print("Dataset carregado com sucesso!")
            else:
                print("Falha ao carregar dataset.")
        
        elif opcao == '11':
            print("\n--- GERAR CSVs DE ANÁLISES ---")
            if gerar_csvs_analises():
                print("CSVs de análises gerados com sucesso!")
            else:
                print("Falha ao gerar CSVs.")
        
        elif opcao == '12':
            print("\n--- GERAR CSV DE VENDEDOR ESPECÍFICO ---")
            nome = input("Nome do vendedor: ").strip()
            if gerar_csv_vendedor_especifico(nome):
                print(f"CSVs do vendedor '{nome}' gerados com sucesso!")
            else:
                print("Falha ao gerar CSVs do vendedor.")
        
        elif opcao == '13':
            print("\n--- GERAR CSV COM TODAS AS VENDAS DE UM VENDEDOR ---")
            nome = input("Nome do vendedor: ").strip()
            if gerar_csv_todas_vendas_vendedor(nome):
                print(f"CSV com todas as vendas de '{nome}' gerado com sucesso!")
            else:
                print("Falha ao gerar CSV.")
        
        elif opcao == '14':
            print("\n--- GERAR GRÁFICOS DE ANÁLISE ---")
            if gerar_graficos():
                print("Gráficos gerados com sucesso!")
            else:
                print("Falha ao gerar gráficos.")
        
        elif opcao == '0':
            print("Encerrando sistema...")
            break
        
        else:
            print("Opção inválida!")

def main():
    menu_interativo()

if __name__ == "__main__":
    main()