import logging
import pandas as pd
from sqlalchemy import create_engine, text

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_trimestre(engine):
    query_trimestre = text("""
    SELECT 
        o.registro_ans,
        o.razao_social,
        d.descricao,
        d.data,
        d.vl_saldo_final AS despesas
    FROM demonstracoes_contabeis d
    JOIN operadoras_planos_de_saude o 
      ON d.reg_ans = o.registro_ans
    WHERE 
        d.descricao ILIKE '%SINISTROS%'
        AND d.vl_saldo_final > 0
        AND d.data IS NOT NULL
        AND date_trunc('quarter', d.data) = date_trunc('quarter', DATE '2024-10-01')
    ORDER BY d.vl_saldo_final DESC
    LIMIT 10;
    """)

    with engine.connect() as conn:
        return pd.read_sql(query_trimestre, conn)

def get_anual(engine):
    query_anual = text("""
    SELECT 
        o.registro_ans,
        o.razao_social,
        SUM(d.vl_saldo_final) AS total_despesas
    FROM demonstracoes_contabeis d
    JOIN operadoras_planos_de_saude o 
      ON d.reg_ans = o.registro_ans
    WHERE 
        d.descricao ILIKE '%SINISTROS%'
        AND d.vl_saldo_final > 0
        AND d.data IS NOT NULL
        AND EXTRACT(YEAR FROM d.data) = 2024
    GROUP BY o.registro_ans, o.razao_social
    ORDER BY total_despesas DESC
    LIMIT 10;
    """)

    with engine.connect() as conn:
        return pd.read_sql(query_anual, conn)

def main():
    user = 'postgres'
    password = 'joao'
    host = 'localhost'
    port = '5432'
    database = 'nivelamento_saude'

    try:
        engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')
        logging.info("Conexão com o banco de dados estabelecida com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao conectar ao banco de dados: {e}")
        return

    while True:
        print("\nEscolha uma opção:")
        print("1. Ver os 10 primeiros do trimestre")
        print("2. Ver os 10 primeiros do ano")
        print("3. Ver ambos")
        print("4. Sair")

        choice = input("Digite o número da opção desejada: ")

        if choice == '1':
            df_trimestre = get_trimestre(engine)
            print("\n=== Top 10 Operadoras com maiores despesas no 4º trimestre de 2024 ===")
            print(df_trimestre)

        elif choice == '2':
            df_anual = get_anual(engine)
            print("\n=== Top 10 Operadoras com maiores despesas acumuladas em 2024 ===")
            print(df_anual)

        elif choice == '3':
            df_trimestre = get_trimestre(engine)
            df_anual = get_anual(engine)
            print("\n=== Top 10 Operadoras com maiores despesas no 4º trimestre de 2024 ===")
            print(df_trimestre)
            print("\n=== Top 10 Operadoras com maiores despesas acumuladas em 2024 ===")
            print(df_anual)

        elif choice == '4':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

if __name__ == "__main__":
    main()
