import pandas as pd
import random
from datetime import datetime, timedelta

vendedores = ["Maria", "João", "Ana", "Carlos", "Beatriz"]
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

def gerar_data_aleatoria():
    inicio = datetime(2021, 1, 1)
    fim = datetime(2024, 12, 31)
    delta = fim - inicio
    data_aleatoria = inicio + timedelta(days=random.randint(0, delta.days))
    return data_aleatoria.strftime("%Y-%m-%d")

def gerar_dataset(num_registros=1500):
    dados = []
    
    for i in range(1, num_registros + 1):
        vendedor = random.choice(vendedores)
        produto = random.choice(produtos)
        quantidade = random.randint(1, 10)
        
        variacao_preco = random.uniform(0.8, 1.2)
        valor_unitario = round(produto["Preco"] * variacao_preco, 2)
        valor_total = quantidade * valor_unitario
        data = gerar_data_aleatoria()
        
        registro = {
            'id': i,
            'produto': produto["Nome"],
            'vendedor': vendedor,
            'quantidade': quantidade,
            'valor_unitario': valor_unitario,
            'valor_total': valor_total,
            'data': data
        }
        dados.append(registro)
    
    df = pd.DataFrame(dados)
    df = df.sort_values('data')
    df['id'] = range(1, len(df) + 1)
    
    return df

def salvar_dataset(df, nome_arquivo='dataset_vendas.csv'):
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')
    print(f"Dataset salvo como {nome_arquivo}")
    print(f"Total de registros: {len(df)}")
    print(f"Período: {df['data'].min()} a {df['data'].max()}")
    print(f"Total de vendas: R$ {df['valor_total'].sum():,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

def main():
    print("Gerando dataset de vendas...")
    df = gerar_dataset(1500)
    salvar_dataset(df)
    
    print("\nPrimeiros 5 registros:")
    print(df.head())

if __name__ == "__main__":
    main()