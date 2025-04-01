Desafio Intuitive Care Este projeto foi desenvolvido para atender ao desafio de nivelamento proposto, com o objetivo de demonstrar habilidades em web scraping, transformação de dados, banco de dados e desenvolvimento de uma API.

As principais ferramentas utilizadas foram Python, VSCode, SQL e Vue.js.

Funcionalidades

Web Scraping Foi implementado um script em Python para realizar o web scraping no site da ANS (Agência Nacional de Saúde Suplementar), onde os dados dos procedimentos e eventos de saúde são extraídos, baixados e compactados em um arquivo ZIP.

Transformação de Dados O projeto extraiu os dados da tabela Rol de Procedimentos e Eventos em Saúde, que estava disponível em formato PDF, e os salvou em um arquivo CSV. Além disso, as abreviações das colunas foram substituídas pelas descrições completas, conforme especificado no documento.

Banco de Dados Foram criados scripts SQL para:

Estruturar as tabelas no banco de dados a partir dos arquivos CSV baixados.

Importar os dados para o banco de dados, com o devido cuidado com o encoding.

Criar consultas analíticas para identificar as 10 operadoras com maiores despesas no último trimestre e no último ano na categoria "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO
HOSPITALAR".

API Foi desenvolvida uma API utilizando Python para servir como backend. A API interage com o frontend desenvolvido em Vue.js, permitindo buscar e retornar informações relevantes sobre as operadoras de plano de
saúde a partir do CSV preparado.

Frontend O frontend foi criado utilizando Vue.js para criar uma interface web que interage com a API, permitindo realizar buscas textuais nas operadoras e exibir os resultados.

Ferramentas Utilizadas Python: Para o desenvolvimento do web scraping, transformação de dados e API.

VSCode: Editor de código utilizado para o desenvolvimento.

SQL: Para a criação das tabelas e consultas analíticas no banco de dados.

Vue.js: Framework JavaScript para desenvolvimento da interface web.

Postman: Utilizado para testar a API e garantir o correto funcionamento das rotas.

Como Rodar o Projeto Clone o repositório:

Terminal git clone https://github.com/Joalbertosilva/desafio-intuitive-care.git Instale as dependências do Python:

Terminal pip install -r requirements.txt Inicie o servidor da API:

Terminal python app.py Para o frontend, navegue até o diretório do Vue.js e execute:

Terminal npm install npm run serve Acesse o frontend na URL local gerada pelo Vue.js.

Conclusão Este projeto foi uma excelente oportunidade de demonstrar competências técnicas em diversas áreas, incluindo a manipulação de dados em Python, desenvolvimento de APIs e interface com Vue.js, além do uso de SQL para análise de dados. O projeto atende a todos os requisitos especificados no teste de nivelamento, incluindo a integração entre os componentes.