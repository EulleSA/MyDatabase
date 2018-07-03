from sys import path
path.append("..")
from Model.Models import *
from psycopg2 import ProgrammingError


class FuncionarioDAO:
    def __init__(self,db):
        self.db = db
        self.connection = db.connection

    def create_table(self):
        self.db.execute("CREATE TABLE Funcionario (id SERIAL PRIMARY KEY,nome TEXT NOT NULL,cpf INTEGER NOT NULL UNIQUE,sexo TEXT NOT NULL,anoNascimento TEXT NOT NULL)")

    def detele_table(self):
        self.db.execute("DROP TABLE IF EXISTS Funcionario")

    def insert_func(self,funcionario):
        sql_string = "INSERT INTO Funcionario (nome, cpf, sexo, anoNascimento) VALUES (%s, %s, %s, %s)"
        self.db.execute(sql_string, (funcionario.nome, funcionario.cpf, funcionario.sexo,funcionario.anoNascimento))


    def get_func_all(self,funcionario):
        sql_string = "SELECT * FROM funcionario"
        self.db.execute(sql_string)

        rows = self.db.fetchall()

        funcionarios = []

        for row in rows:
            name = row[1]
            cpf = row[2]
            sexo = row[3]
            anoNascimento = row[4]
            
            funcionario = Funcionario(name, cpf, sexo, anoNascimento)
            funcionarios.append(funcionario)

        return funcionarios


    def delete_one_func(self,funcionario):
        sql_string = "DELETE FROM funcionario WHERE nome = %s"
        self.db.execute(sql_string,(funcionario,))


    def edit_func_nome(self, new_name , old_name):
        sql_string = "UPDATE funcionario SET nome = %s WHERE nome = %s"
        self.db.execute(sql_string, (new_name, old_name))
        

    def edit_func_cpf(self, cpf , nome):
        sql_string = "UPDATE funcionario SET cpf = %s WHERE nome = %s"
        self.db.execute(sql_string, (cpf, nome)) 

    def edit_func_sexo(self, sexo , nome):
        sql_string = "UPDATE funcionario SET sexo = %s WHERE nome = %s"
        self.db.execute(sql_string, (sexo, nome)) 
    
    def edit_func_anoNascimento(self, anoNascimento , nome):
        sql_string = "UPDATE funcionario SET anoNascimento = %s WHERE nome = %s"
        self.db.execute(sql_string, (anoNascimento, nome)) 
    
    def get_from_name(self, name):
        sql_string = "SELECT * FROM funcionario WHERE nome = %s"
        self.db.execute(sql_string, (name,))

        try:
            row = self.db.fetchone()
            cpf = row[2]
            sexo = row[3]
            anoNascimento = row[4]

            funcionario = Funcionario(name, cpf, sexo , anoNascimento)
            return funcionario

        except ProgrammingError:
            raise Exception("No author with this name")

class FornecedorDAO:
    def  __init__(self,db):
        self.db = db

    def create_table(self):
        sql_string = self.db.execute("CREATE TABLE Fornecedor ( id SERIAL PRIMARY KEY , nome TEXT NOT NULL , cnpj INTEGER NOT NULL UNIQUE, " +
                                    "funcionario_id INTEGER REFERENCES Funcionario (id) ON UPDATE CASCADE ON DELETE CASCADE)")

    def detele_table(self):
        self.db.execute("DROP TABLE IF EXISTS Fornecedor")

    def insert_forn(self,fornecedor):

        sql_string = "SELECT id FROM funcionario WHERE nome = %s"
        self.db.execute(sql_string, (fornecedor.funcionario.nome,))
        func_id = self.db.fetchone()[0]
        
        sql_string = "INSERT INTO Fornecedor (nome, cnpj, funcionario_id) VALUES (%s, %s, %s)"
        self.db.execute(sql_string, (fornecedor.nome, fornecedor.cnpj, func_id))  

    
    def get_forn_all(self,fornecedor):
        sql_string = "SELECT * FROM fornecedor"
        self.db.execute(sql_string)

        rows = self.db.fetchall()

        fornecedores = []

        for row in rows:
            name = row[1]
            cnpj = row[2]
            funcionario_id = row[3]
            
            fornecedor = Fornecedor(name, cnpj, funcionario_id)
            fornecedores.append(fornecedor)

        return fornecedores

    def delete_one_forn(self,fornecedor):
        sql_string = "DELETE FROM fornecedor WHERE nome = %s"
        self.db.execute(sql_string,(fornecedor,))

    def edit_forn_nome(self, new_name , old_name):
        sql_string = "UPDATE fornecedor SET nome = %s WHERE nome = %s"
        self.db.execute(sql_string, (new_name, old_name))

    def edit_forn_cnpj(self,cnpj, nome):
        sql_string = "UPDATE fornecedor SET cnpj = %s WHERE nome = %s"
        self.db.execute(sql_string,(cnpj,nome))


    def get_from_name(self, nome):
        sql_string = "SELECT * FROM fornecedor WHERE nome = %s"
        self.db.execute(sql_string, (nome,))

        try:
            row = self.db.fetchone()
            cnpj = row[2]
            funcionario_id = row[3]

            fornecedor = Fornecedor(nome, cnpj,funcionario_id)
            return fornecedor

        except ProgrammingError:
            raise Exception("Nenhum fornecedor com esse nome")


class ProdutoDAO:
    
    def __init__(self,db):
        self.db =  db

    def create_table(self):
        self.db.execute("CREATE TABLE Produto (id SERIAL PRIMARY KEY , nome TEXT NOT NULL , preco FLOAT NOT NULL , quantidade INTEGER NOT NULL, "+ 
        "fornecedor_id INTEGER REFERENCES fornecedor (id) ON UPDATE CASCADE ON DELETE CASCADE, "+
        "funcionario_id INTEGER REFERENCES funcionario (id) ON UPDATE CASCADE ON DELETE CASCADE)")

    def detele_table(self):
        self.db.execute("DROP TABLE IF EXISTS Produto")

    def insert_prod(self,produto):
        sql_string = "SELECT id FROM fornecedor WHERE nome = %s"
        self.db.execute(sql_string, (produto.fornecedor.nome,))
        fornecedor_id = self.db.fetchone()[0]

        sql_string = "SELECT id FROM funcionario WHERE nome = %s"
        self.db.execute(sql_string, (produto.funcionario.nome,))
        funcionario_id = self.db.fetchone()[0]

        sql_string = "INSERT INTO Produto (nome, preco, quantidade, fornecedor_id, funcionario_id) VALUES (%s, %s, %s, %s, %s)"
        self.db.execute(sql_string,(produto.nome, produto.preco, produto.quantidade, fornecedor_id, funcionario_id))


    def get_prod_all(self,fornecedor):
        sql_string = "SELECT * FROM produto"
        self.db.execute(sql_string)

        rows = self.db.fetchall()

        produtos = []

        for row in rows:
            nome = row[1]
            preco = row[2]
            quantidade = row[3]
            fornecedor_id = row[4]
            funcionario_id = row[5]

            produto = Produto(nome, preco, quantidade, fornecedor_id, funcionario_id)
            produtos.append(produto)

        return produtos


    def delete_one_prod(self,produto):
        sql_string = "DELETE FROM produto WHERE nome = %s"
        self.db.execute(sql_string,(produto,))


    def edit_prod_nome(self, new_name , old_name):
        sql_string = "UPDATE produto SET nome = %s WHERE nome = %s"
        self.db.execute(sql_string, (new_name, old_name))

    def edit_prod_price(self,preco,nome):
        sql_string = "UPDATE produto SET preco = %s WHERE nome = %s"
        self.db.execute(sql_string,(preco,nome))

    def edit_prod_quant(self,quantidade, nome):
        sql_string = "UPDATE produto SET quantidade = %s WHERE nome = %s"
        self.db.execute(sql_string,(quantidade,nome))