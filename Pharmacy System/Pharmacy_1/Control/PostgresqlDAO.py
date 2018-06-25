from sys import path
path.append("..")
from Model.Models import *
from psycopg2 import ProgrammingError


class FuncionarioDAO:
    def __init__(self,db):
        self.db = db
        self.connection = db.connection

    def create_table(self):
        self.db.execute("CREATE TABLE Funcionario (id SERIAL PRIMARY KEY,nome TEXT NOT NULL,cpf NOT NULL UNIQUE,sexo TEXT NOT NULL)")

    def detele_table(self):
        self.db.execute("DROP TABLE IF EXISTS Funcionario")

    def insert(self, funcionario):
        sql_string = "INSERT INTO author (nome, cpf, sexo) VALUES (%s, %s, %s)"
        self.db.execute(sql_string, (funcionario.nome, funcionario.cpf, funcionario.sexo))
