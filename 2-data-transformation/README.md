README

Descrição do Projeto
Este projeto foi desenvolvido para resolver uma questão de extração, processamento e compactação de dados de um arquivo PDF. O objetivo é:

Extrair tabelas de um arquivo PDF.

Processar os dados extraindo e substituindo abreviações específicas (como "OD" e "AMB") por seus respectivos significados ("Odontologia" e "Ambulatório").

Salvar os dados em um arquivo CSV com a codificação adequada para garantir que caracteres especiais sejam corretamente exibidos.

Compactar o arquivo CSV em um arquivo ZIP.

Ferramentas Utilizadas
pdfplumber: Biblioteca utilizada para extrair tabelas do PDF. (pip install pdfplumber)

pandas: Biblioteca para manipulação de dados tabulares (DataFrames). (pip install pandas)

zipfile: Biblioteca para compactar o arquivo CSV em um arquivo ZIP. Já incluído no Python (não precisa instalar)

re: Biblioteca para manipulação de expressões regulares, útil para substituir os termos desejados nas tabelas. Já incluído no Python (não precisa instalar)

logging: Biblioteca para registrar informações sobre o andamento do processo (substituindo o print). Já incluído no Python (não precisa instalar)

Explicação do Código
Extração das Tabelas (extrair_tabela_do_pdf):

O arquivo PDF é aberto com a biblioteca pdfplumber, e todas as tabelas presentes em suas páginas são extraídas e armazenadas em uma lista.

Processamento de Dados (processar_dados):

Para cada tabela extraída, o código cria um DataFrame usando o pandas e realiza duas principais tarefas:

Substitui as abreviações "OD" por "Odontologia" e "AMB" por "Ambulatório" nas colunas e nas células da tabela.

Corrige a codificação dos caracteres para garantir que acentos e cedilhas sejam preservados corretamente.

Salvar e Compactar Arquivo (salvar_e_comprimir):

O DataFrame final é salvo como um arquivo CSV com a codificação utf-8-sig (para garantir que caracteres especiais sejam preservados).

O arquivo CSV gerado é então compactado em um arquivo ZIP.

Função Principal (principal):

A função principal é o ponto de entrada do programa. Ela chama as funções de extração, processamento, e salvamento/compactação.

Como Usar
Instalar as dependências: Antes de rodar o código, instale as bibliotecas necessárias:

Terminal
pip install pdfplumber pandas
Executar o código:

O código pode ser executado diretamente após configurar o caminho do PDF que você deseja processar.

O caminho do arquivo PDF, CSV e ZIP são passados como parâmetros para a função principal no final do script.

Para rodar o código:

Terminal
python script.py
Observação: Certifique-se de substituir os caminhos dos arquivos pdf_path, csv_path, e zip_path conforme o local onde seus arquivos estão armazenados.

O que está acontecendo no código?
Extração do PDF: O código percorre todas as páginas do PDF e extrai as tabelas. Cada tabela é armazenada em uma lista.

Substituição de termos: Para garantir que as abreviações sejam substituídas, utilizamos expressões regulares e o método applymap do pandas para substituir os valores nas colunas e nas células.

Correção de codificação: A codificação dos caracteres é corrigida para garantir que caracteres especiais, como acentos e cedilhas, sejam exibidos corretamente.

Salvamento e compactação: O DataFrame final é salvo em um arquivo CSV e compactado em um arquivo ZIP.

Conclusão:
Este script foi desenvolvido para automatizar a extração e processamento de dados de um arquivo PDF. Ele é eficiente e fácil de personalizar caso haja mais abreviações ou ajustes necessários no processo de transformação de dados.