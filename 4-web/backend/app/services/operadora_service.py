from app.database import engine
from sqlalchemy import text
import logging

def buscar_operadoras(nome_fantasia):
    nome_fantasia = nome_fantasia.strip().replace("'", "''")

    base_query = """
        SELECT 
            o.registro_ans,
            o.razao_social,
            o.nome_fantasia,
            SUM(d.vl_saldo_final) AS total_despesas
        FROM demonstracoes_contabeis d
        JOIN operadoras_planos_de_saude o 
            ON d.reg_ans = o.registro_ans
        WHERE 
            d.descricao ILIKE '%SINISTROS%'
            AND d.vl_saldo_final > 0
            AND d.data IS NOT NULL
            AND EXTRACT(YEAR FROM d.data) = 2024
    """

    if nome_fantasia:
        base_query += f" AND o.nome_fantasia ILIKE '%{nome_fantasia}%'"

    base_query += """
        GROUP BY o.registro_ans, o.razao_social, o.nome_fantasia
        ORDER BY total_despesas DESC
    """

    logging.info(f"Query executada:\n{base_query}")

    with engine.connect() as conn:
        result = conn.execute(text(base_query))
        registros = result.fetchall()
        colunas = result.keys()
        return [dict(zip(colunas, row)) for row in registros]
