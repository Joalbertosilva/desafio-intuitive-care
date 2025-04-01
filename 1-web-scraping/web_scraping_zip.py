import zipfile
import os
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_zip(pdf_files, zip_filename):
    try:
        with zipfile.ZipFile(zip_filename, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
            for pdf in pdf_files:
                if os.path.exists(pdf):
                    zipf.write(pdf, os.path.basename(pdf))
                    logging.info(f"Arquivo {os.path.basename(pdf)} adicionado ao ZIP com sucesso.")
                else:
                    logging.warning(f"O arquivo {pdf} não foi encontrado.")
    except Exception as e:
        logging.error(f"Erro ao criar o arquivo zip: {e}")

def main():
    
    pdf_files = [os.path.join("web-scraping", "Anexo_I.pdf"), os.path.join("web-scraping", "Anexo_II.pdf")]

    zip_filename = os.path.join("web-scraping", "anexos.zip")

    if not os.path.exists("web-scraping"):
        os.makedirs("web-scraping")
        logging.info(f"Diretório 'web-scraping' foi criado.")

    create_zip(pdf_files, zip_filename)

if __name__ == "__main__":
    main()
