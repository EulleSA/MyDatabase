from sys import path
path.append("..")
from Dao import *


class DAOFactory:
    def __init__(self,db):
        self.db = db
    
    def get_FuncionarioDAO(self):
        return PostgresqlDAO.FuncionarioDAO(self.db)

    def get_FornecedorDAO(self):
        return PostgresqlDAO.FornecedorDAO(self.db)

    def get_ProdutoDAO(self):
        return PostgresqlDAO.ProdutoDAO(self.db)