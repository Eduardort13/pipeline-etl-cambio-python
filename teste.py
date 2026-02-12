import requests
import pandas as pd
import sqlite3
import os
import time
from datetime import datetime

def inicializar_banco():
    conexao = sqlite3.connect('meu_portfolio_dados.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historico_cambio (
            data TEXT PRIMARY KEY,
            maximo REAL,
            minimo REAL,
            fechamento REAL,
            variacao REAL
        )
    ''')
    conexao.commit()
    return conexao

while True:
    print(f"\n--- Início do Ciclo: {datetime.now().strftime('%H:%M:%S')} ---")
    
    url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/5"
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            dados_brutos = response.json()
            
            
            df = pd.DataFrame(dados_brutos)
            df['Data'] = pd.to_datetime(df['timestamp'].astype(int), unit='s').dt.strftime('%Y-%m-%d')
            df = df[['Data', 'high', 'low', 'bid', 'pctChange']]
            df.columns = ['data', 'maximo', 'minimo', 'fechamento', 'variacao']
            
            
            conn = inicializar_banco()
            
            
            linhas_inseridas = 0
            for _, linha in df.iterrows():
                try:
                    linha_dict = linha.to_dict()
                    conn.execute('''
                        INSERT OR IGNORE INTO historico_cambio (data, maximo, minimo, fechamento, variacao)
                        VALUES (:data, :maximo, :minimo, :fechamento, :variacao)
                    ''', linha_dict)
                    linhas_inseridas += 1
                except Exception as e:
                    print(f"Erro ao inserir linha: {e}")
            
            conn.commit()
            print(f"Dados processados e enviados ao SQL.")

            
            df_sql = pd.read_sql_query("SELECT * FROM historico_cambio ORDER BY data DESC", conn)
            df_sql.to_excel("relatorio_acumulado.xlsx", index=False)
            print("Excel atualizado com base no histórico do Banco de Dados.")
            
            conn.close()
            
        else:
            print(f"Erro na API: {response.status_code}")

    except Exception as e:
        print(f"Erro no pipeline: {e}")

    print("Aguardando 1 minuto")

    time.sleep(60)
