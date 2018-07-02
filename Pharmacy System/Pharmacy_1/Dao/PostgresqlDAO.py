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

    def insert(self,funcionario):
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