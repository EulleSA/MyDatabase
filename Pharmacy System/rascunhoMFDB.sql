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
	endereco VARCHAR(45) NOT NULL,
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


CREATE TABLE Funcionario (

	idFuncionario INTEGER NOT NULL,
	nomeFuncionario VARCHAR(45) NOT NULL,
	cpf INTEGER NOT NULL UNIQUE,
	cargo VARCHAR(30) NOT NULL CHECK (cargo = 'Farmacêutico' or cargo = 'Balconista'), --- Mais coisas
	telefone INTEGER ,
	endereco VARCHAR(45) NOT NULL,
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
	preco FLOAT NOT NULL,
	dataFabricacao VARCHAR(10) NOT NULL,
	dataValidade VARCHAR(10) NOT NULL,
	lote INTEGER NOT NULL,
	
	PRIMARY KEY(idProduto)

);

CREATE TABLE Estoque (
	idEstoque INTEGER NOT NULL,
	idProduto INTEGER NOT NULL REFERENCES Produto,
	quantidade INTEGER ,
	localizacao VARCHAR(30) NOT NULL,
	
	PRIMARY KEY(idEstoque)

);


CREATE TABLE Devolucao (
	idDevelocao INTEGER NOT NULL,
	idVenda INTEGER NOT NULL REFERENCES Venda,
	idProduto INTEGER NOT NULL REFERENCES Produto,
	motivo VARCHAR(40) NOT NULL,

	PRIMARY KEY(idDevelocao)
)


CREATE TABLE Venda(
	idVenda INTEGER NOT NULL,
	idFuncinario INTEGER NOT NULL REFERENCES Funcionario,
	dataVenda VARCHAR(10) NOT NULL,
	formaPagamento VARCHAR(10) NOT NULL CHECK (formaPagamento = 'Dinheiro' or formaPagamento = 'Cartão'), 
	valorTotal FLOAT NOT NULL,

	PRIMARY KEY(idVenda)
)

CREATE TABLE Pedido(
	idPedido INTEGER NOT NULL,
	idProduto INTEGER NOT NULL REFERENCES Produto,
	idCliente INTEGER NOT NULL REFERENCES Cliente,
	idVenda INTEGER NOT NULL REFERENCES Venda,
	quantidade INTEGER NOT NULL,
	dataPedido VARCHAR(10) NOT NULL,

	PRIMARY KEY(idPedido)
)

CREATE TABLE Receita(
	idReceita INTEGER NOT NULL,
	dataPrescricao VARCHAR(10) NOT NULL,
	crm INTEGER NOT NULL REFERENCES Medico,

	PRIMARY KEY(idReceita)
)

CREATE TABLE Medico(
	crm INTEGER NOT NULL,
	nomeMedico VARCHAR(40) NOT NULL,

	PRIMARY KEY(crm)
)

CREATE TABLE ReceitaRemedio(
	idReceita INTEGER NOT NULL,
	idRemedio INTEGER NOT NULL,

	PRIMARY KEY(idReceita),
	PRIMARY KEY(idRemedio)
)

CREATE TABLE Remedio(
	idRemedio INTEGER NOT NULL,
	nomeRemedio VARCHAR(40) NOT NULL,

	PRIMARY KEY(idRemedio)
)