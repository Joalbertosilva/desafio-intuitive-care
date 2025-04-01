README

Descrição do Projeto
Este projeto foi desenvolvido para resolver a questão de extração, processamento e análise de dados provenientes de arquivos CSV. O objetivo é:

Carregar dados de arquivos CSV contendo informações de operadoras de planos de saúde e demonstrações contábeis.

Processar os dados, convertendo tipos de dados e realizando ajustes de formatação.

Inserir os dados processados em um banco de dados PostgreSQL.

Realizar consultas SQL para identificar as 10 operadoras com as maiores despesas no último trimestre e no último ano.

Usar o logging para registrar o andamento do processo.

Ferramentas Utilizadas
pandas: Biblioteca para manipulação de dados tabulares (DataFrames). (pip install pandas)

SQLAlchemy: Biblioteca para interação com o banco de dados PostgreSQL. (pip install sqlalchemy)

psycopg2: Driver para conectar o SQLAlchemy ao PostgreSQL. (pip install psycopg2)

logging: Biblioteca para registrar informações sobre o andamento do processo (substituindo o print).

Explicação do Código
Carregamento dos Dados (Carregar Dados)
Os arquivos CSV são carregados utilizando o pandas.read_csv(). O código garante que as colunas sejam padronizadas (transformando para minúsculas e substituindo espaços por underscores).

Processamento dos Dados (Processar Dados)
Após o carregamento dos arquivos, as seguintes ações são realizadas:

Conversão de tipos de dados:

As colunas de data são convertidas para o formato datetime.

As colunas numéricas são convertidas para o tipo float, com a substituição de vírgulas por pontos.

Inserção de dados no banco de dados:

Os dados são inseridos nas tabelas operadoras_planos_de_saude e demonstracoes_contabeis no banco de dados PostgreSQL utilizando o método to_sql() do pandas.

Consultas SQL (Consultas)
Duas consultas SQL são executadas para identificar as 10 operadoras com as maiores despesas:

Último Trimestre: A consulta encontra as operadoras com maiores despesas no último trimestre de 2024.

Acumulado Anual: A consulta encontra as operadoras com maiores despesas no ano de 2024.

Função Principal (Função Principal)
A função principal chama as funções de carregamento, processamento e execução das consultas SQL.

Logging
O código utiliza a biblioteca logging para registrar as informações durante o processo. Isso inclui a confirmação do carregamento de arquivos, a conversão de dados e a inserção no banco de dados, bem como a execução das consultas.

Como Usar
Instalar as dependências: Antes de rodar o código, instale as bibliotecas necessárias:

Terminal
pip install pandas sqlalchemy psycopg2
Estrutura de Arquivos:

database/Relatorio_cadop.csv: Arquivo CSV com informações sobre operadoras de planos de saúde.

database/4T2024.csv: Arquivo CSV com as demonstrações contábeis.

load-data.py: Script Python que realiza o carregamento dos arquivos CSV para o banco de dados PostgreSQL.

queries.py: Script Python que realiza as consultas SQL no banco de dados.

Rodando o código:

Execute o script load-data.py para carregar os dados no banco:

Terminal
python load-data.py
Após carregar os dados, execute o script queries.py para visualizar as 10 operadoras com as maiores despesas no último trimestre e no último ano:

Terminal
python queries.py
Banco de Dados:

O código conecta-se a um banco de dados PostgreSQL local.

As tabelas operadoras_planos_de_saude e demonstracoes_contabeis são criadas e alimentadas com os dados dos arquivos CSV.

O que está acontecendo no código?
Carregamento de Dados: O código carrega os dados dos arquivos CSV, ajustando os nomes das colunas e convertendo os tipos de dados conforme necessário.

Processamento de Dados: O código processa os dados convertendo as colunas numéricas e de datas e insere esses dados nas tabelas do banco de dados.

Consultas SQL: Após inserir os dados, duas consultas SQL são executadas para identificar as 10 operadoras com as maiores despesas no último trimestre e no último ano.

Logs: O progresso e os erros durante o processo são registrados usando a biblioteca logging.

Conclusão
Esse projeto fornece uma solução completa para carregar, processar e consultar dados de operadoras de planos de saúde, e é uma boa demonstração de como usar Python, SQL e PostgreSQL para análise de dados. Além disso, o uso de logging permite acompanhar o andamento do processo de maneira eficiente.

