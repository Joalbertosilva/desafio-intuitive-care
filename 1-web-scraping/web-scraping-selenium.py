import logging
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_anexo_link(driver, link_text):
    try:
        wait = WebDriverWait(driver, 10)
        link = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, link_text))).get_attribute('href')
        logging.info(f"Link para '{link_text}' encontrado com sucesso.")
        return link
    except Exception as e:
        logging.error(f"Erro ao encontrar o link para '{link_text}': {e}")
        return None

def get_anexo_links(driver):
    anexo_i_link = get_anexo_link(driver, "Anexo I")
    anexo_ii_link = get_anexo_link(driver, "Anexo II")
   
    return anexo_i_link, anexo_ii_link

def download_file(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if not os.path.exists("web-scraping"):
                os.makedirs("web-scraping")
            
            file_path = os.path.join("web-scraping", filename)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            logging.info(f'{filename} baixado com sucesso!')
        else:
            logging.error(f"Erro ao baixar {filename}: Status code {response.status_code}")
    except Exception as e:
        logging.error(f"Erro ao baixar {filename}: {e}")

def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
    driver.get(url)

    anexo_i_link, anexo_ii_link = get_anexo_links(driver)

    if anexo_i_link and anexo_ii_link:
        download_file(anexo_i_link, "Anexo_I.pdf")
        download_file(anexo_ii_link, "Anexo_II.pdf")

    driver.quit()

if __name__ == "__main__":
    main()
