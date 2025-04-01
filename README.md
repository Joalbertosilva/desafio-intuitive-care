# Desafio Intuitive Care

Este projeto foi desenvolvido para atender ao desafio de nivelamento proposto, com o objetivo de demonstrar habilidades em **web scraping**, **transformação de dados**, **banco de dados** e **desenvolvimento de uma API**.

As principais ferramentas utilizadas foram **Python**, **VSCode**, **SQL** e **Vue.js**.

---

## Funcionalidades

### 1. Web Scraping
Foi implementado um script em Python para realizar o web scraping no site da ANS (Agência Nacional de Saúde Suplementar), onde os dados dos procedimentos e eventos de saúde são extraídos, baixados e compactados em um arquivo `.zip`.

### 2. Transformação de Dados
O projeto extrai os dados da tabela **Rol de Procedimentos e Eventos em Saúde**, originalmente disponível em **formato PDF**, e os salva em um arquivo `.csv`.  
Além disso, as abreviações das colunas foram substituídas pelas descrições completas, conforme especificado no documento.

### 3. Banco de Dados
Foram criados scripts SQL para:
- Estruturar as tabelas no banco de dados a partir dos arquivos CSV baixados.
- Importar os dados para o banco, cuidando do encoding adequado.
- Criar consultas analíticas para identificar as **10 operadoras com maiores despesas** no último trimestre e no último ano na categoria:


### 4. API
Foi desenvolvida uma API utilizando **Flask (Python)** para servir como backend.  
Ela interage com o frontend em Vue.js, permitindo buscar e retornar informações relevantes sobre as operadoras de plano de saúde.

### 5. Frontend
O frontend foi construído utilizando **Vue.js**, criando uma interface web que:
- Consome os dados da API.
- Permite buscas textuais nas operadoras.
- Exibe os resultados em tempo real.

---

## Tecnologias Utilizadas

- **Python**: Web scraping, transformação de dados e desenvolvimento da API.
- **VSCode**: Editor de código.
- **SQL**: Criação das tabelas e consultas analíticas.
- **Vue.js**: Criação da interface do frontend.
- **Postman**: Testes da API e verificação das rotas.

---

## Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Joalbertosilva/desafio-intuitive-care.git
cd desafio-intuitive-care
```
### 2. Inicie o servidor da API
```bash
python app.py
```
### 3. Rode o frontend (Vue.js)
Navegue até a pasta do frontend e execute: 
```bash
npm install
npm run serve
```
### 4. Acesse o frontend
Abra a URL local gerada pelo Vue.js no navegador (geralmente http://localhost:8080).

## Conclusão
Este projeto foi uma excelente oportunidade para demonstrar competências técnicas em:

Manipulação e transformação de dados com Python.

Desenvolvimento de APIs RESTful.

Criação de interfaces interativas com Vue.js.

Utilização de SQL para análises analíticas.

Integração entre camadas (backend + frontend).

Atende a todos os requisitos especificados no teste de nivelamento, com entrega funcional e modular.

Recursos, você pode ver no postman o seu uso
[Collection](https://drive.google.com/file/d/15UyF6nPUGYB-NbzW3fYNnLTxMF6YzNKm/view?usp=drive_link)








