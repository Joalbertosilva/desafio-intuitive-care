README

Descrição do Projeto
Este projeto foi desenvolvido para atender aos requisitos do teste de nivelamento solicitado, com foco na criação de uma API em Python para manipulação de dados de operadoras de planos de saúde e uma interface frontend com Vue.js para exibição dos dados.

As funcionalidades principais são:

Filtrar operadoras por nome fantasia.

Exibir as 10 operadoras com maiores despesas ou mostrar todos os registros de uma operadora, com base no filtro aplicado.

Ferramentas Utilizadas
Backend:
Python (Flask): Framework utilizado para criar a API. (pip install flask)

SQLAlchemy: Biblioteca para interagir com o banco de dados PostgreSQL. (pip install sqlalchemy)

PostgreSQL: Banco de dados utilizado para armazenar os dados das operadoras de planos de saúde. 

psycopg2: Driver para conectar o SQLAlchemy ao PostgreSQL. (pip install psycopg2)

logging: Para registrar informações sobre o andamento do processo.

Frontend:
Vue.js: Framework para a criação de uma interface interativa.

Vite: Ferramenta de build para o projeto Vue.js.

Postman: Utilizado para testar a API.

Funcionalidade do Código
Backend (Flask)
A API foi desenvolvida em Python com Flask. Ela oferece uma rota /api/registros que permite buscar informações das operadoras, filtrando por nome fantasia e exibindo:

As 10 operadoras com maiores despesas, ou

Todos os registros de uma operadora selecionada.

Função get_registros:
Filtra os registros pela operadora desejada (nome_fantasia).

Se o parâmetro top=10 for passado, limita a resposta às 10 maiores operadoras por despesas.

Se não passar o filtro de nome ou o top=10, retorna todos os registros.

Exemplo de URLs:

Para ver todos os registros:

Terminal
http://localhost:5000/api/registros
Para ver os top 10 registros:

Terminal
http://localhost:5000/api/registros?top=10
Para filtrar por nome (exemplo com UNIMED):

Terminal
http://localhost:5000/api/registros?nome_fantasia=UNIMED
Para filtrar por nome e ver os top 10:

Terminal
http://localhost:5000/api/registros?nome_fantasia=UNIMED&top=10
Frontend (Vue.js)
O frontend foi desenvolvido em Vue.js, e a aplicação consome a API para exibir os dados das operadoras de planos de saúde.

Funcionalidade de Pesquisa:
O usuário pode pesquisar uma operadora por nome fantasia.

Pode escolher entre:

Exibir as 10 operadoras com maiores despesas.

Exibir todos os registros de uma operadora.

Estrutura do código:
Botões:

"Top 10": Exibe as 10 operadoras com maiores despesas.

"Mostrar Todos": Exibe todos os registros da operadora filtrada.

Campo de pesquisa: Permite ao usuário digitar o nome da operadora e filtrar as informações.

Como Usar
Backend (Flask)
Instalar dependências do backend:

Execute o seguinte no terminal:

Rodar o servidor Flask:

Para iniciar o servidor backend, execute:

Terminal
python app.py
Isso rodará a API em http://localhost:5000.

Testar a API com Postman:

Crie uma nova requisição no Postman:

Método: GET

URL: http://localhost:5000/api/registros

Você pode também passar parâmetros para testar:

Filtrar por nome fantasia:

Terminal
http://localhost:5000/api/registros?nome_fantasia=UNIMED
Limitar a 10 primeiros:

Terminal
http://localhost:5000/api/registros?top=10
Frontend (Vue.js)
Instalar dependências do frontend:

No terminal, para criar a pasta vue:

Terminal
npm create vite@latest
api-project
cd api-project
npm install
Rodar o servidor de desenvolvimento:

Para iniciar o servidor frontend, execute:

Terminal
npm run dev
A aplicação será acessível em http://localhost:5173.

Interface Vue: A interface permite ao usuário fazer buscas e escolher entre ver os Top 10 ou Todos os registros de uma operadora.

A configuração de proxy no Vite é essencial para permitir que o frontend (Vue.js) se comunique com a API backend (Flask) sem problemas de CORS.

No arquivo vite.config.js, a seguinte configuração de proxy foi adicionada:

server: {
  proxy: {
    '/api': 'http://localhost:5000'
  }
}

Como Funciona:
As requisições feitas para /api no frontend (ex: http://localhost:5173/api/registros) são redirecionadas automaticamente para o backend Flask rodando em http://localhost:5000.

Isso evita problemas de CORS e simplifica as URLs, permitindo que o frontend e o backend se comuniquem de forma transparente durante o desenvolvimento.



Conclusão
Este projeto oferece uma API em Flask que permite consultar operadoras de planos de saúde por nome fantasia, filtrando e exibindo as 10 maiores despesas ou todos os registros de uma operadora selecionada. A interface frontend em Vue.js interage com a API, fornecendo uma maneira fácil e intuitiva para visualizar e pesquisar as operadoras.