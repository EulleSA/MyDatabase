CREATE TABLE Telefones(
	idTelefone INTEGER NOT NULL,
    numero VARCHAR(10) NOT NULL,
    
    PRIMARY KEY (idTelefone)
);

CREATE TABLE Login (
	idLogin INTEGER NOT NULL,
	nomeLogin VARCHAR(20) NOT NULL UNIQUE,
	senha VARCHAR(30) NOT NULL,

	PRIMARY KEY(idLogin)

);

CREATE TABLE Cliente (

	idCliente INTEGER NOT NULL,
    idTelefone INTEGER NOT NULL REFERENCES Telefones,
	nomeCliente VARCHAR(45) NOT NULL,
	cpf VARCHAR(20) NOT NULL UNIQUE,
	endereco VARCHAR(45) NOT NULL,
	sexo VARCHAR(10) NOT NULL CHECK(sexo = 'M' or sexo = 'F' or sexo = 'Outro'),
	dataNascimento DATE NOT NULL,

	PRIMARY KEY(idCliente)
);


CREATE TABLE Funcionario (

	idFuncionario INTEGER NOT NULL,
	idTelefone INTEGER NOT NULL REFERENCES Telefones,
	idLogin INTEGER NOT NULL REFERENCES Login,
	nomeFuncionario VARCHAR(45) NOT NULL,
	cpf VARCHAR(20) NOT NULL UNIQUE,
	cargo VARCHAR(30) NOT NULL CHECK (cargo = 'Farmacêutico' or cargo = 'Balconista'), --- Mais coisas
	endereco VARCHAR(45) NOT NULL,
	sexo VARCHAR(10) NOT NULL CHECK(sexo = 'M' or sexo = 'F' or sexo = 'Outro'),
	dataNascimento DATE NOT NULL,

	PRIMARY KEY(idFuncionario)
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
	tipoProduto VARCHAR(30) NOT NULL CHECK(tipoProduto='TarjaVermelha' or tipoProduto='TarjaPreta' or tipoProduto='TarjaAmarela')
	preco FLOAT NOT NULL,
	dataFabricacao DATE NOT NULL,
	dataValidade DATE NOT NULL,
	lote INTEGER NOT NULL,
	
	PRIMARY KEY(idProduto)
);

CREATE TABLE Compra(
	idCompra INTEGER NOT NULL,
    dataCompra DATE NOT NULL,
    dataEntrega DATE,
    quantidade INTEGER NOT NULL,
    valorTotal DECIMAL(10) NOT NULL,
    idProduto INTEGER NOT NULL REFERENCES Produto,
    idFornecedor INTEGER NOT NULL REFERENCES Fornecedor,
    
    PRIMARY KEY (idCompra)
);

CREATE TABLE Estoque (
	idEstoque INTEGER NOT NULL,
	idProduto INTEGER NOT NULL REFERENCES Produto,
	quantidade INTEGER NOT NULL,
	localizacao VARCHAR(30) NOT NULL,
	
	PRIMARY KEY(idEstoque)

);

CREATE TABLE Medico(
	crm INTEGER NOT NULL,
	nomeMedico VARCHAR(40) NOT NULL,

	PRIMARY KEY(crm)
);

CREATE TABLE Receita(
	idReceita INTEGER NOT NULL,
	dataPrescricao VARCHAR(10) NOT NULL,
	crm INTEGER NOT NULL REFERENCES Medico,

	PRIMARY KEY(idReceita)
);

CREATE TABLE Pedido(
	idPedido INTEGER NOT NULL,
	idProduto INTEGER NOT NULL REFERENCES Produto,
	idCliente INTEGER NOT NULL REFERENCES Cliente,
    idReceita INTEGER NOT NULL REFERENCES Receita,
	quantidade INTEGER NOT NULL,
	dataPedido DATE NOT NULL,

	PRIMARY KEY(idPedido)
);



CREATE TABLE Venda(
	idVenda INTEGER NOT NULL,
	idFuncinario INTEGER NOT NULL REFERENCES Funcionario,
    idPedido INTEGER NOT NULL REFERENCES Pedido,
	dataVenda DATE NOT NULL,
	formaPagamento VARCHAR(10) NOT NULL CHECK (formaPagamento = 'Dinheiro' or formaPagamento = 'Cartão'), 
	valorTotal FLOAT NOT NULL,

	PRIMARY KEY(idVenda)
);

CREATE TABLE Devolucao (
	idDevelocao INTEGER NOT NULL,
	idVenda INTEGER NOT NULL REFERENCES Venda,
	idProduto INTEGER NOT NULL REFERENCES Produto,
	motivo VARCHAR(40) NOT NULL,

	PRIMARY KEY(idDevelocao)
);


CREATE TABLE Remedio(
	idRemedio INTEGER NOT NULL,
	nomeRemedio VARCHAR(40) NOT NULL,

	PRIMARY KEY(idRemedio)
);

CREATE TABLE ReceitaRemedio(
	idReceita INTEGER NOT NULL REFERENCES Receita,
	idRemedio INTEGER NOT NULL REFERENCES Remedio,

	PRIMARY KEY(idReceita, idRemedio)
);