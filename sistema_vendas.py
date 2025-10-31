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
    
    relatorio = {
        'total_geral': total_vendas,
        'quantidade_vendas': len(vendas),
        'vendedores': vendas_vendedor,
        'produtos': vendas_produto,
        'meses': vendas_mes,
        'top_vendedores': top_vendedores,
        'top_produtos': top_produtos,
        'melhor_mes': mes_destaque,
        'valor_melhor_mes': valor_mes
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
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '1':
            try:
                print("\n--- REGISTRAR NOVA VENDA ---")
                
                # Listar produtos disponíveis
                listar_produtos()
                produto_escolha = input("\nEscolha o produto (número ou nome): ").strip()
                
                # Tentar obter produto por número
                produto_obj = obter_produto_por_numero(produto_escolha)
                if produto_obj:
                    produto = produto_obj['Nome']
                    valor_sugerido = produto_obj['Preco']
                    print(f"Produto selecionado: {produto}")
                    print(f"Valor sugerido: R$ {valor_sugerido:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
                else:
                    produto = produto_escolha
                    valor_sugerido = None
                
                # Listar vendedores disponíveis
                listar_vendedores()
                vendedor_escolha = input("\nEscolha o vendedor (número ou nome): ").strip()
                
                # Tentar obter vendedor por número
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
        
        elif opcao == '0':
            print("Encerrando sistema...")
            break
        
        else:
            print("Opção inválida!")

def main():
    menu_interativo()

if __name__ == "__main__":
    main()