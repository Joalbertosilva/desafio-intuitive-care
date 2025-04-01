README

Descrição do Projeto
Este projeto tem como objetivo automatizar o download de arquivos (Anexo I e Anexo II) de uma página da web utilizando Selenium e requests, e em seguida compactar os arquivos em um arquivo ZIP. O processo foi dividido em duas etapas principais:

Web Scraping: Acessar a página, buscar e baixar os arquivos PDF.

Compactação: Compactar os arquivos baixados em um único arquivo ZIP.

Ferramentas Utilizadas
Selenium: Usado para automação do navegador e fazer o scraping da página da web. (pip install selenium)

requests: Usado para baixar os arquivos PDF da web. (pip install requests)

WebDriverManager: Gerencia automaticamente o chromedriver necessário para o Selenium. (pip install webdriver-manager)

zipfile: Usado para criar o arquivo ZIP que compacta os arquivos PDF. Já incluso no Python (não requer instalação).

logging: Para registrar o andamento do processo e mensagens de erro ou sucesso. Já incluso no Python (não requer instalação).

Explicação das Partes Importantes do Código
WebDriverWait:

Usado para garantir que o código espere até que os elementos (links para os anexos) estejam presentes na página antes de tentar acessá-los. Isso evita erros relacionados ao carregamento dinâmico da página.

Função get_anexo_links:

A função utiliza o Selenium para encontrar os links para "Anexo I" e "Anexo II" com base no texto parcial dos links. O uso de WebDriverWait garante que o Selenium aguarde até que os elementos estejam visíveis e acessíveis.

Função download_file:

Após localizar os links, a função download_file utiliza requests para baixar os arquivos PDF para a pasta web-scraping.

Função create_zip:

Após os arquivos serem baixados, a função create_zip usa a biblioteca zipfile para compactar os arquivos PDF em um único arquivo ZIP.

Como Usar
Instalar as dependências:

Execute o seguinte comando para instalar as bibliotecas necessárias:

Terminal
pip install selenium webdriver-manager requests
Executar o script:

Primeiro, execute o script de web scraping para baixar os arquivos PDF:

Terminal
python web-scraping-selenium.py
Depois, execute o script de compactação para criar o arquivo ZIP:

Terminal
python web-scraping-zip.py
Verifique a pasta web-scraping:

Os arquivos PDF serão baixados e armazenados na pasta web-scraping, e o arquivo ZIP será gerado com os arquivos compactados.

O que está acontecendo no código?
web-scraping-selenium.py:

Selenium acessa a página especificada.

Utiliza WebDriverWait para garantir que os links dos anexos estejam disponíveis.

Usa requests para baixar os arquivos PDF e salvá-los na pasta web-scraping.

web-scraping-zip.py:

Verifica se os arquivos PDF existem na pasta web-scraping.

Compacta os arquivos PDF em um arquivo anexos.zip usando zipfile.

Mais Detalhes Importantes
Modularização: As funções foram organizadas para tornar o código mais limpo e manutenível. Cada função tem uma responsabilidade clara.

Logs: O uso de logging em todo o processo ajuda a registrar os sucessos, erros e aviso sobre o andamento do processo, o que facilita a depuração e o monitoramento.

Conclusão:
Esse projeto utiliza o Selenium para realizar scraping de arquivos PDF em uma página da web e o requests para fazer o download dos arquivos. Após o download, o código utiliza a biblioteca zipfile para compactar os arquivos baixados em um arquivo ZIP. A modularização e o uso de logging tornam o código mais eficiente e fácil de depurar.