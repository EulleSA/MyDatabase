CREATE DATABASE postgres
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;


CREATE TABLE Cliente (

	idCliente INTEGER NOT NULL,
	nomeCliente VARCHAR(45) NOT NULL,
	cpf INTEGER NOT NULL UNIQUE,
	telefone INTEGER ,
	endereço VARCHAR(45) NOT NULL,
	sexo VARCHAR(10) NOT NULL CHECK(sexo = 'M' or sexo = 'F' or sexo = 'Outro'),
	dataNascimento 	VARCHAR(10) NOT NULL,

	PRIMARY KEY(idCliente)
);

CREATE TABLE Login (
	idLogin INTEGER NOT NULL,
	nomeLogin VARCHAR(20) NOT NULL UNIQUE,
	senha VARCHAR(30) NOT NULL,

	PRIMARY KEY(idLogin)

);


CREATE TABLE Funcionário (

	idFuncionario INTEGER NOT NULL,
	nomeFuncionario VARCHAR(45) NOT NULL,
	cpf INTEGER NOT NULL UNIQUE,
	cargo VARCHAR(30) NOT NULL CHECK (cargo = 'Farmacêutico' or cargo = 'Vendedora'), --- Mais coisas
	telefone INTEGER ,
	endereço VARCHAR(45) NOT NULL,
	sexo VARCHAR(10) NOT NULL CHECK(sexo = 'M' or sexo = 'F' or sexo = 'Outro'),
	dataNascimento VARCHAR(10) NOT NULL,

	PRIMARY KEY(idFuncinario)


);


CREATE TABLE Fornecedor (

	idFornecedor INTEGER NOT NULL,
	nomeFornecedor VARCHAR(45) NOT NULL,
	cnpj INTEGER NOT NULL UNIQUE,
	telefone INTEGER NOT NULL,

	PRIMARY KEY(idFornecedor)	


);

CREATE TABLE Produto (
	idProduto INTEGER NOT NULL,
	nomeProduto VARCHAR(45) NOT NULL,
	tipoProduto VARCHAR(30) NOT NULL,
	preço FLOAT NOT NULL,
	dataFabricação VARCHAR(10) NOT NULL,
	dataValidade VARCHAR(10) NOT NULL,
	lote INTEGER NOT NULL,
	
	PRIMARY KEY(idProduto)

);

CREATE TABLE Estoque (
	idEstoque INTEGER NOT NULL,
	quantidade INTEGER ,
	localização VARCHAR(30) NOT NULL,
	
);
