-- Tabelas --

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
	idLogin INTEGER NOT NULL REFERENCES Login,

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
	tipoProduto VARCHAR(30) NOT NULL,
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
	idFuncionario INTEGER NOT NULL REFERENCES Funcionario,
    idPedido INTEGER NOT NULL REFERENCES Pedido,
	dataVenda DATE NOT NULL,
	formaPagamento VARCHAR(10) NOT NULL CHECK (formaPagamento = 'Dinheiro' or formaPagamento = 'Cartão'), 
	valorTotal FLOAT NOT NULL,

	PRIMARY KEY(idVenda)
);

CREATE TABLE Devolucao (
	idDevolucao INTEGER NOT NULL,
	idVenda INTEGER NOT NULL REFERENCES Venda,
	idProduto INTEGER NOT NULL REFERENCES Produto,
	motivo VARCHAR(140) NOT NULL,

	PRIMARY KEY(idDevolucao)
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

-- Fim da criação das tabelas ---


-- Criação das triggers --
	-- Trigger que impede que o pagamento seja diferente das formas de pagamento impostas --
CREATE FUNCTION pagamento_gatilho() RETURNS trigger AS $pagamento_gatilho$
BEGIN 
	IF NEW.formaPagamento != 'Dinheiro' or NEW.formaPagamento != 'Cartão' THEN
		RAISE EXCEPTION 'O pagamento só pode ser feito por meio de dinheiro(especie) ou cartão'
	END IF;
RETURN NEW;
END;
$pagamento_gatilho$ LANGUAGE plpgsql;

CREATE TRIGGER pagamento_inserts BEFORE INSERT OR UPDATE 
on Venda
FOR EACH ROW EXECUTE
PROCEDURE pagamento_gatilho();


-- Trigger que impede que um produto seja inserido com validade inferior a 6 meses --

CREATE FUNCTION verificaValidade() RETURNS trigger AS $verificaValidade$
BEGIN
	IF age(NEW.datavalidade, current_date) < '6 mons' THEN
    	RAISE EXCEPTION 'Data validade com menos de 6 meses para vencer!';
    END IF;
    RETURN NEW;
END;
$verificaValidade$ LANGUAGE plpgsql;

CREATE TRIGGER verificaAno BEFORE INSERT 
ON produto
FOR EACH ROW EXECUTE
PROCEDURE verificaValidade();


-- Trigger que impede que um produto de tarja preta ou vermelha seja vendido sem a receita -- 

CREATE FUNCTION verifica_medicamento() RETURNS trigger AS $verifica_medicamento$
BEGIN 
	IF tipoProduto = 'Tarja Preta' or 'Tarja Vermelha' THEN
		IF idReceita = NULL THEN
			RAISE EXCEPTION 'Você não pode fazer o pedido de um medicamento Tarja preta ou Vermelha sem a receita'
		END IF;
	RETURN NEW;
	END IF;
END;
$verifica_medicamento$ LANGUAGE plpgsql;

CREATE TRIGGER verifica_medicamento BEFORE INSERT
on Pedido
FOR EACH ROW EXECUTE
PROCEDURE verifica_medicamento();


 
-- Criação das Transações -- 

	-- Transação 1 --

BEGIN
UPDATE Produto SET tipoProduto = 'TarjaVermelha' WHERE idProduto = 8;
SAVEPOINT SAVEPOINT_1;
UPDATE Produto SET tipoProduto = 'TarjaVermelha' WHERE idProduto = 1;
SELECT * FROM Produto WHERE idProduto = 8;
ROLLBACK SAVEPOINT_1;
SELECT * FROM Produto WHERE idProduto = 8;
COMMIT



-- Transação 2 - Concorrente --
	-- Transação A --
BEGIN;
INSERT INTO Medico(crm,nomeMedico)
VALUES ('134343','Tucaco');
SELECT * FROM Medico;
COMMIT



	-- Transação B --

BEGIN 
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT * FROM Produto WHERE crm = '134343';
COMMIT;

-- Fim das transações --