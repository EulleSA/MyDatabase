from sys import path
path.append("..")
from Model.Models import *
from psycopg2 import *

class Funcionario:
	def __init__(self,db):
		self.db = db
		self.connection = db.connection

	def create_table(self):
		self.db.execute("CREATE TABLE Funcionario (id SERIAL PRIMARY KEY, nome TEXT NOT NULL UNIQUE, cpf INTEGER NOT NULL UNIQUE, sexo TEXT NOT NULL,anoNascimento INTEGER NOT NULL)
	def delete_table(self):
		self.db.execute("DROP TABLE IF EXISTS Funcionario")
	def insert(self,funcionario):
		sql_string = "INSERT INTO Funcionario (nome,cpf,sexo,anoNascimento) VALUES (%s,%s,%s)"
	def remove(self,funcionario):
	
	def update_name(self, old_name,new_name):
		sql_string = "UPDATE Funcionario SET nome = %s WHERE name = %s"
		self.db.execute(sql_string,(new_name,old_name))

	def get(self,id):
		sql_string = "SELECT  * FROM Funcionario WHERE id = %s"
		self.db.execute(sql_string,(id,))
	
