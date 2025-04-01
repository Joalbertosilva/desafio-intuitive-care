import pdfplumber
import pandas as pd
import zipfile
import re
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Função para extrair todas as tabelas do PDF
def extrair_tabela_do_pdf(caminho_pdf):
    logging.info("Iniciando extração das tabelas do PDF.")
    with pdfplumber.open(caminho_pdf) as pdf:
        todas_as_tabelas = []
        for pagina in pdf.pages:
            tabela = pagina.extract_table()
            if tabela:
                todas_as_tabelas.append(tabela)
    logging.info(f"{len(todas_as_tabelas)} tabelas extraídas.")
    return todas_as_tabelas

# Função para processar os dados extraídos
def processar_dados(tabelas):
    logging.info("Iniciando o processamento dos dados extraídos.")
    todos_os_dados = []
    for tabela in tabelas:
        df = pd.DataFrame(tabela[1:], columns=tabela[0])
        df.columns = df.columns.str.replace(r'\bOD\b', 'Odontologia', regex=True)
        df.columns = df.columns.str.replace(r'\bAMB\b', 'Ambulatório', regex=True)
        df = df.applymap(lambda x: re.sub(r'\bOD\b', 'Odontologia', x) if isinstance(x, str) else x)
        df = df.applymap(lambda x: re.sub(r'\bAMB\b', 'Ambulatório', x) if isinstance(x, str) else x)
        df = df.applymap(lambda x: x.encode('utf-8').decode('utf-8') if isinstance(x, str) else x)
        todos_os_dados.append(df)
    logging.info("Processamento de dados concluído.")
    return pd.concat(todos_os_dados, ignore_index=True)

# Função para salvar e compactar os dados
def salvar_e_comprimir(df, caminho_csv, caminho_zip):
    logging.info(f"Salvando o DataFrame em: {caminho_csv}")
    df.to_csv(caminho_csv, index=False, encoding='utf-8-sig', sep=';')
    
    logging.info(f"Compactando o CSV em: {caminho_zip}")
    with zipfile.ZipFile(caminho_zip, 'w') as zipf:
        zipf.write(caminho_csv, arcname="teste-joao.csv")
    
    logging.info("Arquivo CSV e ZIP criados com sucesso.")

# Função principal
def principal(caminho_pdf, caminho_csv, caminho_zip):
    tabelas = extrair_tabela_do_pdf(caminho_pdf)
    
    df_final = processar_dados(tabelas)
    
    df_final = df_final.dropna(axis=1, how='all')  
    df_final = df_final.reset_index(drop=True)  
    
    salvar_e_comprimir(df_final, caminho_csv, caminho_zip)

# Executando a função principal
if __name__ == "__main__":
    caminho_pdf = "web-scraping/Anexo_I.pdf"  
    caminho_csv = "data-transformation/teste_joao.csv"  
    caminho_zip = "data-transformation/teste_zip_joao.zip"  
    principal(caminho_pdf, caminho_csv, caminho_zip)
