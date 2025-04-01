import logging
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DATABASE')

    engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    try:
        logging.info("Iniciando o carregamento dos arquivos CSV.")
        cadop = pd.read_csv('database/Relatorio_cadop.csv', sep=';', encoding='utf-8')
        contabeis = pd.read_csv('database/4T2024.csv', sep=';', encoding='utf-8')
        logging.info("Arquivos CSV carregados com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao carregar os arquivos CSV: {e}")
        raise

    logging.info("Padronizando os nomes das colunas dos arquivos CSV.")
    cadop.columns = [col.strip().lower().replace(' ', '_') for col in cadop.columns]
    contabeis.columns = [col.strip().lower().replace(' ', '_') for col in contabeis.columns]

    logging.info("Convertendo as colunas de datas.")
    cadop['data_registro_ans'] = pd.to_datetime(cadop['data_registro_ans'], errors='coerce')
    contabeis['data'] = pd.to_datetime(contabeis['data'], errors='coerce')

    try:
        logging.info("Iniciando a conversão de valores numéricos.")
        contabeis['vl_saldo_inicial'] = contabeis['vl_saldo_inicial'].astype(str).str.replace(',', '.').astype(float)
        contabeis['vl_saldo_final'] = contabeis['vl_saldo_final'].astype(str).str.replace(',', '.').astype(float)
        logging.info("Conversão de valores numéricos concluída com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao converter os valores numéricos: {e}")
        raise

    try:
        logging.info("Iniciando a inserção de dados na tabela 'operadoras_planos_de_saude'.")
        cadop.to_sql('operadoras_planos_de_saude', engine, if_exists='append', index=False)
        logging.info("Dados inseridos com sucesso na tabela 'operadoras_planos_de_saude'.")

        logging.info("Iniciando a inserção de dados na tabela 'demonstracoes_contabeis'.")
        contabeis.to_sql('demonstracoes_contabeis', engine, if_exists='append', index=False)
        logging.info("Dados inseridos com sucesso na tabela 'demonstracoes_contabeis'.")
    except Exception as e:
        logging.error(f"Erro ao inserir dados nas tabelas: {e}")
        raise

    logging.info("Processo concluído com sucesso!")

if __name__ == "__main__":
    main()
