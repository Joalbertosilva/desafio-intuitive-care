-- Database: nivelamento_saude

-- DROP DATABASE IF EXISTS nivelamento_saude;

CREATE DATABASE nivelamento_saude
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


CREATE TABLE operadoras_planos_de_saude (
    registro_ans VARCHAR PRIMARY KEY,
    cnpj VARCHAR,
    razao_social VARCHAR,
    nome_fantasia VARCHAR,
    modalidade VARCHAR,
    logradouro VARCHAR,
    numero VARCHAR,
    complemento VARCHAR,
    bairro VARCHAR,
    cidade VARCHAR,
    uf VARCHAR,
    cep VARCHAR,
    ddd VARCHAR,
    telefone VARCHAR,
    fax VARCHAR,
    endereco_eletronico VARCHAR,
    representante VARCHAR,
    cargo_representante VARCHAR,
    regiao_de_comercializacao VARCHAR,
    data_registro_ans DATE
);

CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE,
    reg_ans VARCHAR,
    cd_conta_contabil VARCHAR,
    descricao VARCHAR,
    vl_saldo_inicial NUMERIC,
    vl_saldo_final NUMERIC
);


SELECT * FROM operadoras_planos_de_saude LIMIT 10;
SELECT * FROM demonstracoes_contabeis;

SELECT 
    o.registro_ans,
    o.razao_social,
    d.descricao,
    d.data,
    d.vl_saldo_final AS despesas
FROM demonstracoes_contabeis d
JOIN operadoras_planos_de_saude o 
  ON d.reg_ans = o.registro_ans
WHERE 
    d.descricao ILIKE '%SINISTROS%'
    AND d.vl_saldo_final > 0
    AND d.data IS NOT NULL
    AND date_trunc('quarter', d.data) = date_trunc('quarter', DATE '2024-10-01') -- Q4 2024
ORDER BY d.vl_saldo_final DESC
LIMIT 10;

SELECT 
    o.registro_ans,
    o.razao_social,
    SUM(d.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras_planos_de_saude o 
  ON d.reg_ans = o.registro_ans
WHERE 
    d.descricao ILIKE '%SINISTROS%'
    AND d.vl_saldo_final > 0
    AND d.data IS NOT NULL
    AND EXTRACT(YEAR FROM d.data) = 2024
GROUP BY o.registro_ans, o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;

